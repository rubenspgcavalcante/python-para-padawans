# coding=utf-8

from jedi import *

# Implemente um método atacar na classe Jedi, em que seu jedi utilizará seu(s) sabre(s).
luke = Jedi("Luke Skywalker", 27, SabreDeLuz("Azul", "medio"))
luke.atacar()

yoda = Jedi("Mestre Yoda", 2000, SabreDeLuz("Verde", "pequeno"), SabreDeLuz("Verde", "pequeno"))
yoda.atacar()