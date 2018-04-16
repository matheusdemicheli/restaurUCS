#-*- coding: UTF-8 -*-
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django.contrib import admin
from django.db import models as django_models
from django.forms.widgets import CheckboxSelectMultiple

from estabelecimento import models


class TelefoneInline(admin.TabularInline):
    """
    Inline para o model Telefone.
    """
    model = models.Telefone


class HorarioAtendimentoInline(admin.TabularInline):
    """
    Inline para o model HorarioAtendimento.
    """
    model = models.HorarioAtendimento


class ImagemInline(admin.TabularInline):
    """
    Inline para o model Imagem.
    """
    model = models.Imagem


class MidiaInline(admin.StackedInline):
    """
    Inline para o model RedeSocial.
    """
    model = models.Midia


class EstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        TelefoneInline,
        HorarioAtendimentoInline,
        ImagemInline,
        MidiaInline
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
            # 'jquery-3.3.1.min.js',
            'jquery.mask.min.js',
            'estabelecimento/admin.js',
        )

    def get_changeform_initial_data(self, request):
        """
        Sobrescrito para retornar valores iniciais do form.
        """
        return {'geolocation': '-29.161442600144074,-51.15251292684479'}


class TipoEstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model TipoEstabelecimento.
    """
    prepopulated_fields = {"slug": ("descricao",)}


admin.site.register(models.Estabelecimento, EstabelecimentoModelAdmin)
admin.site.register(models.TipoEstabelecimento, TipoEstabelecimentoModelAdmin)
