#-*- coding: UTF-8 -*-
"""
Admin.
"""
import nested_admin
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.db import models as django_models
from django.http import HttpResponseRedirect
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.functional import curry

from estabelecimento import models


class UserSiteAdmin(admin.AdminSite):
    """
    Site especifico para tratar acesso por usuários comuns.
    """
    site_header = 'Administração do estabelecimento'

    def index(self, request, extra_context=None):
        """
        Quando não for superuser, renderiza o template customizado.
        """
        if request.user.is_superuser:
            return super().index(request, extra_context)

        extra_context = extra_context or {}
        admin_instance = self._registry[models.Estabelecimento]

        try:
            estabelecimento = request.user.estabelecimento
        except models.Estabelecimento.DoesNotExist:
            template = admin_instance.add_view(request)
        else:
            template = admin_instance.change_view(
                request,
                str(estabelecimento.pk)
            )

        if isinstance(template, HttpResponseRedirect):
            return HttpResponseRedirect('.')

        obj = template.context_data.get('original')
        template.context_data.update({
            'usuario_comum': True,
            'forms_abas': (
                'cardapiopadrao',
                'cardapiodia_set',
                'aviso_set'
            ),
            'cardapio_padrao': obj and obj.cardapio_padrao
        })
        return template


admin.site = UserSiteAdmin()


class TelefoneInline(nested_admin.NestedTabularInline):
    """
    Inline para o model Telefone.
    """
    extra = 2
    model = models.Telefone


class HorarioAtendimentoInline(nested_admin.NestedTabularInline):
    """
    Inline para o model HorarioAtendimento.
    """
    extra = 3
    model = models.HorarioAtendimento


class ImagemInline(nested_admin.NestedTabularInline):
    """
    Inline para o model Imagem.
    """
    extra = 3
    model = models.Imagem


class MidiaInline(nested_admin.NestedTabularInline):
    """
    Inline para o model RedeSocial.
    """
    extra = 2
    model = models.Midia


class AvisoInline(nested_admin.NestedTabularInline):
    """
    Inline para o model Aviso.
    """
    extra = 3
    model = models.Aviso


class ItemCardapioPadraoInline(nested_admin.NestedTabularInline):
    """
    Inline para o model ItemCardapio.
    """
    extra = 3
    model = models.ItemCardapioPadrao

    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class ItemCardapioDiaInline(nested_admin.NestedTabularInline):
    """1
    Inline para o model ItemCardapio.
    """
    model = models.ItemCardapioDia
    classes = ['collapse']

    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_extra(self, request, obj=None, **kwargs):
        """
        Sobrescrito para definir o extra dinâmicamente.
        """
        try:
            cardapio_padrao = request.user.estabelecimento.cardapiopadrao
        except (models.Estabelecimento.DoesNotExist,
                models.CardapioPadrao.DoesNotExist):
            return 1
        return cardapio_padrao.itemcardapiopadrao_set.count()


    def get_formset(self, request, obj=None, **kwargs):
        """
        Sobrescrito para retornar valores iniciais do form.
        """
        formset = super().get_formset(request, obj, **kwargs)

        if obj and obj.pk:
            return formset

        try:
            cardapio_padrao = request.user.estabelecimento.cardapiopadrao
        except (models.Estabelecimento.DoesNotExist,
                models.CardapioPadrao.DoesNotExist):
            pass
        else:
            initial = []
            itens = cardapio_padrao.itemcardapiopadrao_set.all().order_by(
                'categoria',
                'item',
                'pk'
            )
            for item_cardapio in itens.prefetch_related('restricoes'):
                initial.append({
                    'item': str(item_cardapio.item),
                    'categoria': str(item_cardapio.categoria),
                    'restricoes': [
                        str(restricao.pk)
                        for restricao in item_cardapio.restricoes.all()
                    ],
                    'preco': str(item_cardapio.preco)
                })
            formset.__init__ = curry(formset.__init__, initial=initial)
        return formset


class CarpioPadraoInline(nested_admin.NestedStackedInline):
    """
    Inline para o model CardapioPadrao.
    """
    extra = 1
    max_num = 1
    model = models.CardapioPadrao
    inlines = [ItemCardapioPadraoInline]


class CardapioDiaInline(nested_admin.NestedStackedInline):
    """
    Inline para o model CardapioDia.
    """
    extra = 1
    model = models.CardapioDia
    inlines = [ItemCardapioDiaInline]
    fields = ('data', 'preco_buffet_quilo', 'preco_buffet_livre')

    def get_formset(self, request, obj=None, **kwargs):
        """
        Sobrescrito para retornar valores iniciais do form.
        """
        formset = super().get_formset(request, obj, **kwargs)

        try:
            cardapio_padrao = request.user.estabelecimento.cardapiopadrao
        except (models.Estabelecimento.DoesNotExist,
                models.CardapioPadrao.DoesNotExist):
            pass
        else:
            initial = models.CardapioPadrao.objects.filter(
                pk=cardapio_padrao.pk
            ).values(
                'preco_buffet_quilo',
                'preco_buffet_livre'
            )
            formset.__init__ = curry(formset.__init__, initial=initial)

        return formset


class TipoEstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model TipoEstabelecimento.
    """
    prepopulated_fields = {"slug": ("descricao",)}


class TipoServicoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model TipoServico.
    """
    prepopulated_fields = {"slug": ("descricao",)}


class RestricaoAlimentarModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model RestricaoAlimentar.
    """
    prepopulated_fields = {"slug": ("descricao",)}


class EstabelecimentoModelAdmin(nested_admin.NestedModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        TelefoneInline,
        HorarioAtendimentoInline,
        ImagemInline,
        MidiaInline,
        AvisoInline,
        CarpioPadraoInline,
        CardapioDiaInline
    ]

    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget}
    }

    class Media:
        """
        Adição de javascript.
        """
        js = (
            'js/jquery-3.3.1.min.js',
            'js/jquery.mask.min.js',
            'js/estabelecimento/admin.js',
        )

    def get_changeform_initial_data(self, request):
        """
        Sobrescrito para retornar valores iniciais do form.
        """
        return {
            'address': 'Universidade de Caxias do Sul',
            'geolocation': '-29.161442600144074,-51.15251292684479'
        }

    def save_model(self, request, obj, form, change):
        """
        Seta o usuário logado ao objeto.
        """
        if not obj.usuario_id:
            obj.usuario = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(models.TipoServico, TipoServicoModelAdmin)
admin.site.register(models.TipoEstabelecimento, TipoEstabelecimentoModelAdmin)
admin.site.register(models.RestricaoAlimentar, RestricaoAlimentarModelAdmin)
admin.site.register(models.Estabelecimento, EstabelecimentoModelAdmin)
admin.site.register(models.Telefone)
admin.site.register(models.HorarioAtendimento)
admin.site.register(models.Imagem)
admin.site.register(models.Midia)
admin.site.register(models.CardapioPadrao)
admin.site.register(models.CardapioDia)
admin.site.register(models.Aviso)
