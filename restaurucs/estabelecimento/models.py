#-*- coding: UTF-8 -*-
import datetime
from django_google_maps import fields as map_fields

from django.conf import settings
from django.db import models
from estabelecimento import utils


class TipoEstabelecimento(models.Model):
    """
    Representação dos tipos de estabelecimento.
    Ex: Restaurante, Lanchonete, Hamburgueria, Bar.
    """
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """
        Definições do Model.
        """
        verbose_name = 'Tipo de Estabelecimento'
        verbose_name_plural = 'Tipos de Estabelecimento'

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


class TipoServico(models.Model):
    """
    Representação dos tipos de serviço de um estabelecimento.
    Ex: à la carte, buffet a quilo, buffet livre.
    """
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """
        Definições do Model.
        """
        verbose_name = 'Tipo de Serviço'
        verbose_name_plural = 'Tipos de Serviço'

    def __str__(self):
        """
        Retorna a string de representação do objeto.
        """
        return self.descricao


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
    tipo_estabelecimento = models.ManyToManyField(
        to=TipoEstabelecimento,
        verbose_name='Tipo de estabelecimento'
    )
    tipo_servico = models.ManyToManyField(
        to=TipoServico,
        verbose_name='Tipo de serviço'
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
    ativo = models.BooleanField(
        default=True,
        editable=False
    )
    usuario = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False
    )

    @property
    def cardapio_padrao(self):
        """
        Retorna o cardápio padrão do estabelecimento, se houver.
        """
        try:
            return self.cardapio_set.get(data__isnull=True)
        except Cardapio.DoesNotExist:
            return None

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
    observacao = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name='Observação',
        help_text=(
            'Informe observações pertinentes ao horário de atendimento. '
            'Ex: Neste horário funcionamos apenas como Lanchonete.'
        )
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
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


class Aviso(models.Model):
    """
    Representação de avisos do estabelecimento.
    """
    aviso = models.TextField()

    data_inicio_exibicao = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='Data de início para exibição'
    )
    data_fim_exibicao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=(
            'Data de fim para exibição '
            '(deixe em branco para sempre exibir o aviso)'
        )
    )
    estabelecimento = models.ForeignKey(
        Estabelecimento,
        on_delete=models.CASCADE,
    )

    class Meta:
        """
        Meta informações da classe.
        """
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'

    def __str__(self):
        """
        Representação do objeto.
        """
        return self.aviso


class CardapioBase(models.Model):
    """
    Representação de um Cardápio.
    """
    preco_buffet_quilo = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Preço buffet (quilo)'
    )
    preco_buffet_livre = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Preço buffet (livre)'
    )
    estabelecimento = models.ForeignKey(
        to=Estabelecimento,
        on_delete=models.CASCADE
    )

    class Meta:
        """
        Meta informações da classe.
        """
        abstract = True


class CardapioPadrao(CardapioBase):
    """
    Representação do cardápio padrão de um estabelecimento.
    """

    class Meta:
        """
        Meta informações da classe.
        """
        verbose_name = 'Cardápio Padrão'
        verbose_name_plural = 'Cardápios Padrões'

    def __str__(self):
        """
        Identificação do objeto.
        """
        return 'Cardápio padrão de %s' % self.estabelecimento


class CardapioDia(CardapioBase):
    """
    Representação do cardápio de um dia específico de um estabelecimento.
    """
    data = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        """
        Meta informações da classe.
        """
        verbose_name = 'Cardápio do Dia'
        verbose_name_plural = 'Cardápios do Dia'

    def __str__(self):
        """
        Identificação do objeto.
        """
        return '%s - Cardápio do dia %s' % (self.estabelecimento, self.data)


class ItemCardapioBase(models.Model):
    """
    Representação de um item do cardápio de um Estabelecimento.
    """
    item = models.CharField(
        max_length=100
    )
    categoria = models.CharField(
        max_length=20,
        choices=[
            ('bebidas', 'Bebidas'),
            ('doces', 'Doces'),
            ('pratos_frios', 'Pratos Frios'),
            ('pratos_quentes', 'Pratos Quentes'),
            ('saladas', 'Saladas'),
            ('salgados', 'Salgados'),
            ('sobremesas', 'Sobremesas'),
            ('sopas', 'Sopas'),
        ]
    )
    restricoes = models.ManyToManyField(
        to=RestricaoAlimentar,
        blank=True,
        verbose_name='Restrições'
    )
    preco = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Preço (à la carte)'
    )

    class Meta:
        """
        Meta informações da classe.
        """
        abstract = True


class ItemCardapioPadrao(ItemCardapioBase):
    """
    Representação de um item do cardápio padrão de um Estabelecimento.
    """
    cardapio = models.ForeignKey(
        to=CardapioPadrao,
        on_delete=models.CASCADE
    )

    class Meta:
        """
        Meta informações da classe.
        """
        verbose_name = 'Item do Cardápio Padrão'
        verbose_name_plural = 'Itens do Cardápio Padrão'

    def __str__(self):
        """
        Identificação do objeto.
        """
        return self.item


class ItemCardapioDia(ItemCardapioBase):
    """
    Representação de um item do cardápio padrão de um Estabelecimento.
    """
    cardapio = models.ForeignKey(
        to=CardapioDia,
        on_delete=models.CASCADE
    )

    class Meta:
        """
        Meta informações da classe.
        """
        verbose_name = 'Item do Cardápio do Dia'
        verbose_name_plural = 'Itens do Cardápio do Dia'

    def __str__(self):
        """
        Identificação do objeto.
        """
        return self.item
