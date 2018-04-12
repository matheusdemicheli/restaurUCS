#-*- coding: UTF-8 -*-
from django.conf import settings
from django.db import models
from estabelecimento import utils


class TipoEstabelecimento(models.Model):
    """
    Representação de categorias.
    """
    slug = models.SlugField(
        max_length=50,
        editable=False
    )
    descricao = models.CharField(
        max_length=50,
        verbose_name=u'Descrição'
    )

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


class Estabelecimento(models.Model):
    """
    Representação de um estabelecimento.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name=u'Descrição')
    localizacao = models.TextField(verbose_name=u'Localização')
    tipo_estabelecimento = models.ManyToManyField(
        to=TipoEstabelecimento,
        verbose_name=u'Tipo de estabelecimento'
    )
    usuario = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.nome


class Telefone(models.Model):
    """
    Representação dos telefones de um restaurante.
    """
    telefone = models.CharField(max_length=10)
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.telefone


class HorarioAtendimento(models.Model):
    """
    Representação dos horário de funcionamento do restaurante.
    """
    dia_semana = models.PositiveSmallIntegerField(
        verbose_name=u'Dia da semana',
        choices=utils.get_choices_dias_semana()
    )
    horario_abertura = models.CharField(
        max_length=5,
        verbose_name=u'Horário de abertura',
        choices=utils.get_choices_horarios()
    )
    horario_encerramento = models.CharField(
        max_length=5,
        verbose_name=u'Horário de encerramento',
        choices=utils.get_choices_horarios()
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        editable=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return u'%s: %s - %s' % (
            self.dia_semana,
            self.horario_abertura,
            self.horario_encerramento
        )


class Imagem(models.Model):
    """
    Representação de imagens do estabelecimento.
    """
    imagem = models.ImageField(verbose_name=u'Imagem')
    descricao = models.TextField(verbose_name=u'Descrição')
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


# class Aviso(models.Model):
#     """
#     Avisos sobre o estabelecimento.
#     """
#     aviso = models.TextField()
#     estabelecimento = models.ForeignKey(Estabelecimento, editable=False)


# class Categoria(models.Model):
#     """
#     """
#
#
# class Opcao(models.Model):
#     """
#     """
#     nome = models.CharField(max_length=100)
#     imagem = models.ImageField()
#     contem_leite = models.BooleanField()
#     contem_carne = models.BooleanField()
#     contem_ovos = models.BooleanField()
#     contem_gluten = models.BooleanField()
#     contem_mel = models.BooleanField()
#
#
# class CardapioPadrao(models.Model):
#     """
#     """
#     restaurante = models.OneToOneField(Restaurante)
#     opcoes = models.
