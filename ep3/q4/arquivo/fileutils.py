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