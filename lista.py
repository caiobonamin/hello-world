list = [1,7,3,9,5]
list2 = ["carro","moto","onibus"]
list3 = [10,"dez",True,100,"cem",False]

for i in list:
    # o metodo .sort() ordena os valores
    list.sort()
    print(i)

for i in list2:
    #aplicando o paramento (reverse=True) inverte a ordenação
    list2.sort(reverse=True)
    print(i)

for i in list3:
    #inverte a ordem da lista com a função reverse()
    list3.reverse()
    print(i)

big = [ list, list2, list3]
#print (big)