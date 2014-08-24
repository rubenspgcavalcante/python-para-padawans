# coding=utf-8

# Faça a versão recursiva da questão anterior.

def deco(numero):
    size = len(str(numero))
    div = 10 ** (size - 1)

    resto =  numero % div

    if size > 1:
        print "%d +" % (numero - resto),
        deco(resto)

    else:
        print numero - resto,


deco(1203) # 1000 + 200 + 3
