#-*- coding: UTF-8 -*-
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django.contrib import admin
from django.db import models as django_models
from django.forms.widgets import CheckboxSelectMultiple
from django.http import HttpResponse

from estabelecimento import models


class AdminSuperUser(admin.AdminSite):
    pass


adminsite = AdminSuperUser(name='admin_superuser')


class TelefoneInline(admin.TabularInline):
    """
    Inline para o model Telefone.
    """
    extra = 2
    model = models.Telefone


class HorarioAtendimentoInline(admin.TabularInline):
    """
    Inline para o model HorarioAtendimento.
    """
    extra = 7
    model = models.HorarioAtendimento


class ImagemInline(admin.TabularInline):
    """
    Inline para o model Imagem.
    """
    model = models.Imagem


class MidiaInline(admin.TabularInline):
    """
    Inline para o model RedeSocial.
    """
    extra = 2
    model = models.Midia


class OpcaoEstabelecimentoModelAdminInline(admin.TabularInline):
    """
    """
    model = models.OpcaoEstabelecimento
    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class EstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        TelefoneInline,
        HorarioAtendimentoInline,
        ImagemInline,
        MidiaInline,
        OpcaoEstabelecimentoModelAdminInline
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
            'jquery-3.3.1.min.js',
            'jquery.mask.min.js',
            'estabelecimento/admin.js',
        )

    def get_changeform_initial_data(self, request):
        """
        Sobrescrito para retornar valores iniciais do form.
        """
        return {
            'address': 'Universidade de Caxias do Sul',
            'geolocation': '-29.161442600144074,-51.15251292684479'
        }


class TipoEstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model TipoEstabelecimento.
    """
    prepopulated_fields = {"slug": ("descricao",)}


class RestricaoAlimentarModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model RestricaoAlimentar.
    """
    prepopulated_fields = {"slug": ("descricao",)}


class OpcaoEstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model OpcaoEstabelecimento.
    """
    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


adminsite.register(models.Estabelecimento, EstabelecimentoModelAdmin)
adminsite.register(models.TipoEstabelecimento, TipoEstabelecimentoModelAdmin)
adminsite.register(models.RestricaoAlimentar, RestricaoAlimentarModelAdmin)
adminsite.register(models.OpcaoEstabelecimento, OpcaoEstabelecimentoModelAdmin)
