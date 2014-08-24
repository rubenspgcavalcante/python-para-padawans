# coding=utf-8
from arquivo.fileutils import ler_numeros

# coding=utf-8

# Na sua biblioteca de funções de arquivo, crie uma nova função que lê números de
# um arquivo texto (separados por vírgula) e retorne a soma desses números. Se
# qualquer outra coisa senão números ou vírgulas estiver presente no arquivo lance
# uma exceção ValueError informando o mal formato do arquivo.

print ler_numeros("sample.txt")