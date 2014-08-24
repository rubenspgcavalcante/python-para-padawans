# coding=utf-8

class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def falar(self, msg):
        print self.nome + " diz: " + msg


    def andar(self):
        print "Andando"


    def dormir(self):
        print "Zzz... Zzz..."