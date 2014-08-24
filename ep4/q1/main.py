# coding=utf-8

# Crie uma classe SabreDeLuz. Um sabre tem cor e tamanho. Um sabre de luz pode
# ser ligado e desligado e pode ser usado para atacar (esse método imprime o
# barulho de um sabre de luz).

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


sabre = SabreDeLuz("Azul", "medio")
sabre.ligar()
sabre.usar()