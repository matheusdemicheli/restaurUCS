#-*- coding: UTF-8 -*-
from django.contrib import admin
from estabelecimento import models


class AdminSiteEstabelecimento(admin.AdminSite):
    """
    AdminSite customizado para os estabelecimentos.
    """
    site_header = 'Administração do estabelecimento'
    index_title = 'Administração do estabelecimento'
    index_template = 'admin/index_estabelecimento.html'

    def index(self, request, extra_context=None):

        extra_context = extra_context or {}
        extra_context['opts'] = models.Estabelecimento._meta
        return super().index(request, extra_context)


adminsite_estabelecimento = AdminSiteEstabelecimento(name='admin_estabelecimento')
