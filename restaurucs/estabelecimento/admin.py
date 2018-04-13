#-*- coding: UTF-8 -*-
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django import forms
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


class RedeSocialInline(admin.TabularInline):
    """
    Inline para o model RedeSocial.
    """
    model = models.RedeSocial


class EstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        TelefoneInline,
        HorarioAtendimentoInline,
        ImagemInline,
        RedeSocialInline
    ]
    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget}
    }


class TipoEstabelecimentoModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model TipoEstabelecimento.
    """
    prepopulated_fields = {"slug": ("descricao",)}


admin.site.register(models.Estabelecimento, EstabelecimentoModelAdmin)
admin.site.register(models.TipoEstabelecimento, TipoEstabelecimentoModelAdmin)
