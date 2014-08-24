# coding=utf-8

def imprime_arquivo(caminho_arq):
    arquivo = open(caminho_arq)
    print arquivo.read()
    arquivo.close()


def escreve_arquivo(nome="output.txt", texto="", append=False):
    if texto == "":
        texto = raw_input("Digite um texto: ")

    mode = "w"
    if append:
        mode = "a"

    arquivo = open(nome, mode)
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