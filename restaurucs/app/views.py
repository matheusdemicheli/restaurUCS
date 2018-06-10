from django.shortcuts import render
from django.views.generic.base import TemplateView
from estabelecimento.models import Estabelecimento


class IndexView(TemplateView):
    """
    Retorna a renderização da tela inicial do aplicativo.
    """
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        """
        Sobrescrito para retornar os estabelecimentos cadastrados.
        """
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = 'restaurUCS'
        contexto['estabelecimentos'] = Estabelecimento.objects.all()
        contexto['incluir_head'] = True
        return contexto


class HomeEstabelecimentoView(TemplateView):
    """
    Retorna a renderização da tela inicial de um estabelecimento.
    """
    template_name = 'pages/estabelecimento/index.html'

    def get_context_data(self, pk, **kwargs):
        """
        Sobrescrito para retornar informações de um estabelecimento.
        """
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = Estabelecimento.objects.get(pk=pk)
        contexto['estabelecimento'] = Estabelecimento.objects.get(pk=pk)
        return contexto
