# coding=utf-8
from jedi import SabreDeLuz
from sith import Sith

# Crie uma classe Sith que herda da classe já vista Jedi. Sobrecarregue o método
# usar_forca para que imprima a mensagem “Come to the dark side!”

vader = Sith("Darth Vader", 40, SabreDeLuz("Vermelho", "medio"))
vader.usar_forca()