# coding=utf-8
from cao import Cao
from pessoas.pessoa import Pessoa
from pessoas.jedi import Jedi, SabreDeLuz
from pessoas.sith import Sith
from nave import Nave

# Crie uma classe Cachorro, que não herde de ninguém e adicione a tripulação da
# nave da questão anterior, e faça com que a tripulação durma. (Duck Typing)

leia = Pessoa("Princesa Leia", 27)
luke = Jedi("Luke Skywalker", 27, SabreDeLuz("Azul", "medio"))
vader = Sith("Dart Vader", 46, SabreDeLuz("Vermelho", "medio"))
cao = Cao()

nave = Nave("X-Wing", [leia, luke, vader, cao])
nave.tripulacao_dormir()