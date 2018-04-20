#-*- coding: UTF-8 -*-
"""
Especificação do AdminSite para usuários.
"""
from django.contrib import admin
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.template import RequestContext
from django.template.loader import render_to_string

from estabelecimento import models
from estabelecimento.admin import modeladmin


class UserAdminSite(admin.AdminSite):
    """
    Admin acessível para usuários.
    """
    site_header = 'Administração do estabelecimento'
    index_template = 'useradmin/index.html'

    def _renderizar_forms(self, request):
        """
        Renderiza os formulários utilizados no index.
        """
        html_forms = []

        # Estabelemcimento.
        admin_instance = modeladmin.EstabelecimentoModelAdmin(
            model=models.Estabelecimento,
            admin_site=self
        )
        template = admin_instance.add_view(request)

        renderizacao = render_to_string(
            'useradmin/change_form_content.html', template.context_data
        )
        html_forms.append(renderizacao)

        # Cardápio Padrão.
        # admin_instance = modeladmin.C
        return html_forms, template.context_data

    def index(self, request, extra_context=None):
        """
        Incrementa o extra context para renderização do template.
        """
        extra_context = extra_context or {}
        html_forms, context_data = self._renderizar_forms(request=request)
        extra_context['html_forms'] = html_forms
        extra_context.update(context_data)
        return super().index(request, extra_context)


useradmin = UserAdminSite(name='useradmin')
useradmin.register(models.Estabelecimento, modeladmin.EstabelecimentoModelAdmin)
useradmin.register(models.CardapioPadrao)
useradmin.register(models.CardapioDia)
