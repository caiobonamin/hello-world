#  -*- coding: utf-8 -*-

texto = "CaioAllanBonamin"

#conta quantos caracteres tem na variavel texto
conta = len(texto) 

print (conta)

#imprime o valores na ordem conforme incrementando o i com + 1 
#adicionando a função .lower() ou .upper() na variével, altera a formatação

i = 0 
while i < conta:
    print(texto[i].upper(), texto[i].lower())
    i += 1



