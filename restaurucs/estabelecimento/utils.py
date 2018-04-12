#-*- coding:utf-8 -*-
import datetime


def get_choices_horarios():
    """
    Retorna choices de horários.
    """
    horarios = []
    horario_atual = datetime.datetime(2018, 1, 1, 8)

    while horario_atual.hour < 23:
        horario = horario_atual.strftime("%H:%M")
        horarios.append((horario, horario))
        horario_atual += datetime.timedelta(minutes=15)
    return horarios


def get_choices_dias_semana():
    """
    Retorna choices de dias da semana.
    O valores armazenados se baseam no retorno da função datetime.date.weekday.
    """
    return [
        (0, 'Segunda-Feira'),
        (1, 'Terça-Feira'),
        (2, 'Quarta-Feira'),
        (3, 'Quinta-Feira'),
        (4, 'Sexta-Feira'),
        (5, 'Sábado'),
        (6, 'Domingo')
    ]
