def soma(x,y):
    return x+y
def multiplicacao(x,y):
    return x*y
s = soma (5,9)
m = multiplicacao(4,7)

print("soma: ", s)
print("multiplicacao", m)

print("somando os dois valores acima recursivamente: ", soma(s,m))
print("multiplicando os dois valores acima recursivamente: ", multiplicacao(s,m))