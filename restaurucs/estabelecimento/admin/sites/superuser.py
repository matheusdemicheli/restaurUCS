#-*- coding: UTF-8 -*-
"""
Especificação do AdminSite para superusuários.
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from estabelecimento import models


class SuperAdminSite(admin.AdminSite):
    """
    Admin acessível para superusuários.
    """

    def has_permission(self, request):
        """
        Permite acesso somente para o superuser.
        """
        return bool(request.user.is_superuser)


superadmin = SuperAdminSite(name='superadmin')
superadmin.register(User)
superadmin.register(models.TipoEstabelecimento)
superadmin.register(models.Estabelecimento)
superadmin.register(models.Telefone)
superadmin.register(models.HorarioAtendimento)
