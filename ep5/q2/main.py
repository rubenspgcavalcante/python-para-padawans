# coding=utf-8
from pessoas.pessoa import Pessoa
from pessoas.jedi import Jedi, SabreDeLuz
from pessoas.sith import Sith
from nave import Nave

# Crie uma classe Nave que contenha tripulação, uma lista de Pessoas (Lembre-se
# que um jedi, um mercenário ou mesmo um sith são pessoas) e faça com que todos
# andem pela nave.

leia = Pessoa("Princesa Leia", 27)
luke = Jedi("Luke Skywalker", 27, SabreDeLuz("Azul", "medio"))
vader = Sith("Dart Vader", 46, SabreDeLuz("Vermelho", "medio"))

nave = Nave("X-Wing", [leia, luke, vader])
nave.tripulacao_andar()