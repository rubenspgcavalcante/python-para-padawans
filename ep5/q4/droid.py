# coding=utf-8

from pessoa import Pessoa
from robo import Robo

class Droid(Robo, Pessoa):
    def __init__(self, tipo, idade):
        Robo.__init__(self, tipo)
        Pessoa.__init__(self, tipo, idade)