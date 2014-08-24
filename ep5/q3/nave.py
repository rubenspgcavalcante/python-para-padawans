# coding=utf-8

class Nave:
    def __init__(self, tipo, tripulacao):
        self.tipo = tipo
        self.tripulacao = tripulacao


    def tripulacao_andar(self):
        for tripulante in self.tripulacao:
            tripulante.andar()


    def tripulacao_dormir(self):
        for tripulante in self.tripulacao:
            tripulante.dormir()