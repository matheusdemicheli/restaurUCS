from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """
    Retorna a renderização do template home.html.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """
        Sobrescrito para retornar os estabelecimentos cadastrados.
        """
        contexto = super().get_context_data(**kwargs)
        contexto['estabelecimentos'] = ['teste1', 'teste2', 'teste3']
        return contexto
