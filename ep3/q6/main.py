# coding=utf-8

import time

from arquivo.fileutils import ler_numeros, escreve_arquivo

# coding=utf-8

# Na sua biblioteca de funções de arquivo, crie uma nova função que lê números de
# um arquivo texto (separados por vírgula) e retorne a soma desses números. Se
# qualquer outra coisa senão números ou vírgulas estiver presente no arquivo lance
# uma exceção ValueError informando o mal formato do arquivo.

try:
    print ler_numeros("sample.txt")

except ValueError as error:
    now = time.strftime("%Y-%m-%d")
    mensagem = "[%s] %s\n" % (now, error.message)

    escreve_arquivo("errors.log", mensagem, True)