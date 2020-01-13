#  -*- coding: utf-8 -*-

texto = "o rato roeu a roupa do rei de roma na rua"

#A função .find() com argumento de "rei" vai fazer uma busca e identificar o indice
lista = texto.find("rei")
#imprime o indice encontrado
print("encontrado na posição: ",lista)
#Agora imprime a variáevel passando o indice encontrado e salvo na variavel lista 
# o parementro [lista:] faz com que seja impresso a partir do indice até o final 
print(texto[lista:])