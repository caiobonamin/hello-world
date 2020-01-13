
# -*- coding: utf-8 -*-
#Modos
# r - read only
# w - write reescreve o arquivo do zero
# a - read and write - adiciona no final do arquivo
# r+ - read and write
# w+ - escrita apagando conteudo do arquico
# a+ - read and write atualizando o arquivo

#lendo arquivos
#read() le o arquivo inteiro
#readline() le uma linha
#readlines() le o arquivo e armazena em uma lista

#variável para chamar o arquivo
arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

print(linhas)