#-*- coding: UTF-8 -*-
"""
Declaração de ModelAdmins.
"""
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django.contrib import admin
from django.db import models as django_models
from django.forms.widgets import CheckboxSelectMultiple

from estabelecimento.admin import inlines


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


class EstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        inlines.TelefoneInline,
        inlines.HorarioAtendimentoInline,
        inlines.ImagemInline,
        inlines.MidiaInline,
        # inlines.OpcaoEstabelecimentoInline
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
