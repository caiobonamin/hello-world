#  -*- coding: utf-8 -*-
var_string = "Resultado: "
var_num = 10
#comentarios
print("phyton")

print("conta de 4-2: ",4-2)

print("modulo 10%3: ", 10%3)

print(var_string, var_num - (var_num*5))
print("valor de var_num",var_num)
if var_num < 5:
    print(" a var é menor que 15")
else:
    print("var_num é maior =(")
print('File "' + var_string + '" Being Processed.')




import os
import urllib2

def check_in():

    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://whatismyip.org').read()
    print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)