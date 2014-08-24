# coding=utf-8

# Faça uma função que receba um número inteiro e decomponha em fatores de
# unidade, dezena, centena, milhares, etc. Ex.: (1203) imprime ( 1000 + 200 + 3)

def deco(numero):
    div = 10
    res = []
    acum = 0

    # Acumula restos por divisões de fatores de 10 e remove do último resto
    # Ex.: 243 % 100 == 43 -> 43 - 3 == 40
    for i in range(numero):
        if div < numero * 10:
            fator = (numero % div) - acum
            acum = numero % div
            div *= 10

            res.append(fator)

        else:
            break


    message = ""
    res.reverse()
    for num in res:
        if num != 0:
            message += "%d + " % num

    print message[:-3] # remove os últimos " + "


deco(1203) # 1000 + 200 + 3