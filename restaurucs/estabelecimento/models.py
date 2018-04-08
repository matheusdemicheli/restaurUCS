#-*- coding: UTF-8 -*-
from django.db import models
from estabelecimento.utils import get_choices_horarios


class Estabelecimento(models.Model):
    """
    Representação de um restaurante.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    telefones = models.
    horarios = models.ManyToManyField(Horarios)
    tipo_restaurante = models.ChoiceField('')

    cardapio_padrao =


class Telefone(models.Model):
    """
    Representação dos telefones de um restaurante.
    """
    telefone = models.CharField(max_length=10)
    restaurante = models.ForeignKey(Restaurante)


class Horarios(models.Model):
    """
    Representação dos horário de funcionamento do restaurante.
    """
    estabelecimento = models.ForeignKey(Estabelecimento)
    dia_semana = models.ChoiceField(choices=[('12:00', '12:00')])
    horario_abertura = models.ChoiceField(choices=[('12:00', '12:00')])
    horario_encerramento = models.ChoiceField(choices=[('12:00', '12:00')])


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
