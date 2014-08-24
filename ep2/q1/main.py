# coding=utf-8

# Faça uma função soma e utilize-a para fazer uma função multiplicação.
def soma(a, b):
    return a + b


def mult(a, b):
    acum = 0
    for i in range(a):
        acum = soma(acum, b)

    return acum

print soma(5, 4) # 9

print mult(5, 4) # 20
