# coding=utf-8

class Robo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.bateria = 100


    def falar(self, msg):
        if len(msg) <= self.bateria:
            self.bateria -= len(msg)
            print self.tipo + " >> " + msg


    def dormir(self):
        print "Entrando em modo de hibernação..."