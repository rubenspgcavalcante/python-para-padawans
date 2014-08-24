# coding=utf-8

# Faça uma versão recursiva da função da questão anterior.
def piramide(altura):
    if altura > 0:
        largura = range(1, altura + 1)

        # Imprime cada item da base separado por vírgula e espaço
        for base in largura:
            print "%d, " % base,

        # Quebra a linha e imprime a base inferior
        print ""
        piramide(altura - 1)


piramide(5)