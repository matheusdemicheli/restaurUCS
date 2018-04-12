from django.contrib import admin
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


class EstabelecimentoAdmin(admin.ModelAdmin):
    """
    ModelAdmin para o model Estabelecimento.
    """
    inlines = [
        TelefoneInline,
        HorarioAtendimentoInline,
        ImagemInline
    ]


admin.site.register(models.TipoEstabelecimento)
admin.site.register(models.Estabelecimento, EstabelecimentoAdmin)
