#-*- coding: UTF-8 -*-
"""
Declaração de Inlines.
"""
from django.contrib import admin
from django.db import models as django_models
from django.forms.widgets import CheckboxSelectMultiple
from estabelecimento import models


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
    extra = 3
    model = models.Imagem


class MidiaInline(admin.TabularInline):
    """
    Inline para o model RedeSocial.
    """
    extra = 2
    model = models.Midia


class OpcaoEstabelecimentoInline(admin.TabularInline):
    """
    Inline para o model OpcaoEstabelecimento.
    """
    extra = 3
    model = models.OpcaoEstabelecimento

    formfield_overrides = {
        django_models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
