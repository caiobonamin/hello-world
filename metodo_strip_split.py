#  -*- coding: utf-8 -*-

texto = "Caio Allan Bonamin Caio Allan Bonamin"

#imprime o valores na ordem conforme incrementando o i com + 1 
#adicionando a função .strip() remove o "\n" que pula uma linha ou ate mesmo um espaço do final da variável 

print(texto.strip())

#com a função .split() transforma uma variavel em uma lista conforme parametro passado nessa função
lista = texto.split(" ")
print(lista)

#conta quantos itens tem na var lista
conta = len(lista) 
print (conta)



