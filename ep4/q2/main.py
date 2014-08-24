# coding=utf-8

# Melhore a classe Jedi e faça com que um jedi tenha um ou dois sabres de luz.
# (Para o segundo sabre, utilize a notação de argumentos com valores padrão,
# usado também em funções)

from jedi import *

luke = Jedi("Luke Skywalker", 27, SabreDeLuz("Azul", "medio"))

yoda = Jedi("Mestre Yoda", 2000, SabreDeLuz("Verde", "pequeno"), SabreDeLuz("Verde", "pequeno"))