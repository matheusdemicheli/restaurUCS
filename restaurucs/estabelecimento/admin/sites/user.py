#-*- coding: UTF-8 -*-
"""
Especificação do AdminSite para usuários.
"""
from django.contrib import admin
from django.utils.safestring import mark_safe
from estabelecimento import models
from estabelecimento.admin import modeladmin


class UserAdminSite(admin.AdminSite):
    """
    Admin acessível para usuários.
    """
    site_header = 'Administração do estabelecimento'
    index_title = 'Administração do estabelecimento'
    index_template = 'useradmin/index.html'

    def index(self, request, extra_context=None):
        """
        Incrementa o extra context para renderização do template.
        """
        extra_context = extra_context or {}

        admin = modeladmin.EstabelecimentoModelAdmin(
            model=models.Estabelecimento,
            admin_site=self
        )
        template = admin.add_view(request)
        extra_context.update(template.context_data)
        return super().index(request, extra_context)


useradmin = UserAdminSite(name='useradmin')
useradmin.register(models.Estabelecimento, modeladmin.EstabelecimentoModelAdmin)
