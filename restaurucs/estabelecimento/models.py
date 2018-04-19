#-*- coding: UTF-8 -*-
from django_google_maps import fields as map_fields
from django.conf import settings
from django.db import models
from estabelecimento import utils


class TipoEstabelecimento(models.Model):
    """
    Representação de categorias.
    """
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """
        Meta class.
        """
        verbose_name = 'Tipo de Estabelecimento'
        verbose_name_plural = 'Tipos de Estabelecimento'

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


class Estabelecimento(models.Model):
    """
    Representação de um estabelecimento.
    """
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    descricao = models.TextField(
        verbose_name='Descrição'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    address = map_fields.AddressField(
        max_length=200,
        verbose_name='Localização'
    )
    geolocation = map_fields.GeoLocationField(
        max_length=100,
        verbose_name='Geolocalização',
        help_text=(
            'Mova o marcador no mapa para indicar a localização do '
            'estabelecimento.'
        )
    )
    tipo_estabelecimento = models.ManyToManyField(
        to=TipoEstabelecimento,
        verbose_name='Tipo de estabelecimento'
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
    telefone = models.CharField(
        max_length=11
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE,
        editable=False
    )

    class Meta:
        """
        Definições do model.
        """
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

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
        verbose_name='Dia da semana',
        choices=utils.get_choices_dias_semana()
    )
    horario_abertura = models.CharField(
        max_length=5,
        verbose_name='Horário de abertura',
        choices=utils.get_choices_horarios()
    )
    horario_encerramento = models.CharField(
        max_length=5,
        verbose_name='Horário de encerramento',
        choices=utils.get_choices_horarios()
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        editable=False,
        on_delete=models.CASCADE
    )

    class Meta:
        """
        Definições do model.
        """
        verbose_name = 'Horário de Atendimento'
        verbose_name_plural = 'Horários de Atendimento'

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return '%s: %s - %s' % (
            self.dia_semana,
            self.horario_abertura,
            self.horario_encerramento
        )


class Imagem(models.Model):
    """
    Representação de imagens do estabelecimento.
    """
    imagem = models.ImageField(
        verbose_name='Imagem'
    )
    descricao = models.TextField(
        verbose_name='Descrição'
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE,
        editable=False
    )

    class Meta:
        """
        Definições do model.
        """
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


class Midia(models.Model):
    """
    Representação de links para midias do estabelecimento.
    """
    midia = models.CharField(
        max_length=10,
        choices=[
            ('facebook', 'Facebook'),
            ('instagram', 'Instragram'),
            ('site', 'Site'),
            ('blog', 'Blog')
        ]
    )
    url = models.URLField()

    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE,
        editable=False
    )

    class Meta:
        """
        Definições do model.
        """
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'

    def __str__(self):
        """
        Representação de um objeto.
        """
        return '%s: %s' (self.midia, self.url)


class RestricaoAlimentar(models.Model):
    """
    Representação de restrições alimentares.
    """
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """
        Definições do model.
        """
        verbose_name = 'Restrição Alimentar'
        verbose_name_plural = 'Restrições Alimentares'

    def __str__(self):
        """
        Representação de um objeto.
        """
        return self.descricao


class OpcaoEstabelecimento(models.Model):
    """
    Representação de Opções de um Estabelecimento.
    """
    opcao = models.CharField(max_length=100)
    restricoes = models.ManyToManyField(RestricaoAlimentar)

    # contem_carne = models.BooleanField(
    #     default=False,
    #     verbose_name='Contém Carne?'
    # )
    # contem_leite = models.BooleanField(
    #     default=False,
    #     verbose_name='Contém Leite?'
    # )
    # contem_ovos = models.BooleanField(
    #     default=False,
    #     verbose_name='Contém Ovos?'
    # )
    # contem_gluten = models.BooleanField(
    #     default=False,
    #     verbose_name='Contém Leite?'
    # )
    # contem_mel = models.BooleanField(
    #     default=False,
    #     verbose_name='Contém Mel?'
    # )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        editable=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        """
        Definições do model.
        """
        verbose_name = ''
        verbose_name_plural = 'Horários de Atendimento'


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
#
#
# class CardapioPadrao(models.Model):
#     """
#     """
#     restaurante = models.OneToOneField(Restaurante)
#     opcoes = models.
