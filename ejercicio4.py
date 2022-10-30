'''
Ejercicio 4
Realizar un algoritmo que pida números (se pedirá por 
teclado  la cantidad de números a introducir). El programa 
debe informar de cuantos números introducidos son mayores 
que 0, menores que 0 e iguales a 0.
'''

import random

numeros= random.randint(1,10)
numero=0
negativos=0
positivos=0
iguala0=0

print("Diga ",numeros, "numeros:")

for num in range (0,numeros):
    numero=int(input("\n"))
    
    if (numero<0):
        negativos=negativos+1
    elif (numero==0):
        iguala0=iguala0+1
    else:
        positivos=positivos+1

print ("\n Hay ",positivos, "numeros positivos, ", negativos, "numeros negativos, ", iguala0, "numeros iguales a 0")
