# coding=utf-8

class SabreDeLuz:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho
        self.ligado = False


    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print "Zuuum!"


    def desligar(self):
        if self.ligado:
            self.ligado = False
            print "Xiiu"


    def usar(self):
        if self.ligado:
            print "Vrummmmmm"


class Jedi:
    def __init__(self, nome, idade, sabre1, sabre2=None):
        self.nome = nome
        self.idade = idade
        self.forca = 100

        self.sabre1 = sabre1
        self.sabre2 = sabre2


    def __str__(self):
        return self.nome + " de " + str(self.idade) + " anos"


    def falar(self, msg):
        print self.nome + " diz: " + msg


    def cansado(self):
        return self.forca <= 0


    def dormir(self):
        self.forca += 50
        print "Zzz... Zzz..."


    def usar_forca(self):
        if not self.cansado():
            self.forca -= 10
            print "Usando a forca!!!"
            return True

        else:
            print "Estou cansado!"
            return False


    def atacar(self):
        print self.nome + " ataca:"
        if not self.sabre1.ligado:
            self.sabre1.ligar()
            self.sabre1.usar()

        if self.sabre2 is not None and not self.sabre2.ligado:
            self.sabre2.ligar()
            self.sabre2.usar()
