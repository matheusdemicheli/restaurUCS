#-*- coding:utf-8 -*-
import datetime


def get_horarios():
    """
    Retorna os horários de um dia para cadastro de funcionamento do restaurante.
    """
    now = datetime.datetime(2013, 2, 9, 8, 00)
    end=now+datetime.timedelta(hours=9)

    l=[]
    while now<=end:
        l.append(now)
        now+=datetime.timedelta(minutes=15)

    print [t.strftime("%H:%M") for t in l]
