# coding=utf-8

def imprime_arquivo(caminho_arq):
    arquivo = open(caminho_arq)
    print arquivo.read()
    arquivo.close()


def escreve_arquivo():
    texto = raw_input("Digite um texto: ")

    arquivo = open("output.txt", "w")
    arquivo.write(texto)
    arquivo.close()


def ler_numeros(caminho_arq):
    arq = open(caminho_arq)
    texto = arq.read()
    arq.close()

    soma = 0
    for num in texto.split(","):
        soma += float(num.strip()) # É lançado ValueError se não estiver no formato correto

    return soma