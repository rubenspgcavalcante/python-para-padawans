# coding=utf-8
from jedi import Jedi

class Sith(Jedi):
    def __init__(self, nome, idade, sabre1, sabre2=None):
        super(Sith, self).__init__(nome, idade, sabre1, sabre2)


    def usar_forca(self):
        self.forca -= 10
        print "Come to the dark side..."