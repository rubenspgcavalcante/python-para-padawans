# coding=utf-8

# Faça uma função que receba um número n e que imprima uma pirâmide invertida de números:
# 1, 2, 3, ... n
# ...
# 1, 2, 3
# 1, 2
# 1

def piramide(altura):
    # Recebe as larguras das linhas em ordem crescente
    linhas = range(1, altura + 1)

    # Porém, é utilzado a ordem invertida para a piramide invertida
    for linha in linhas[::-1]:
        for base in range(1, linha + 1):
            print "%d, " % base,

        print ""

piramide(5)