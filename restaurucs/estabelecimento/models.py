#-*- coding: UTF-8 -*-
from django.conf import settings
from django.db import models
from estabelecimento.utils import get_choices_horarios


class TipoEstabelecimento(models.Model):
    """
    Representação de categorias.
    """
    descricao = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, editable=False)


class HorarioAtendimento(models.Model):
    """
    Representação dos horário de funcionamento do restaurante.
    """
    dia_semana = models.ChoiceField(choices=[('12:00', '12:00')])
    horario_abertura = models.ChoiceField(choices=[('12:00', '12:00')])
    horario_encerramento = models.ChoiceField(choices=[('12:00', '12:00')])


class Estabelecimento(models.Model):
    """
    Representação de um restaurante.
    """
    nome = models.CharField(max_length=100)
    localizacao = models.CharField()
    descricao = models.TextField()
    horarios_atendimento = models.ManyToManyField(HorarioAtendimento)
    tipo_estabelecimento = models.ManyToManyField(TipoEstabelecimento)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)


class Telefone(models.Model):
    """
    Representação dos telefones de um restaurante.
    """
    telefone = models.CharField(max_length=10)
    estabelecimento = models.ForeignKey(Estabelecimento)


class Categoria(models.Model):
    """
    """


class Opcao(models.Model):
    """
    """
    nome = models.CharField(max_length=100)
    imagem = models.ImageField()
    contem_leite = models.BooleanField()
    contem_carne = models.BooleanField()
    contem_ovos = models.BooleanField()
    contem_gluten = models.BooleanField()
    contem_mel = models.BooleanField()


class CardapioPadrao(models.Model):
    """
    """
    restaurante = models.OneToOneField(Restaurante)
    opcoes = models.
