'''
Ejercicio 11
Escribe un programa que diga si un número introducido por teclado es o no
primo. Un número primo es aquel que sólo es divisible entre él mismo y la
unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
es divisible por algún otro número.
'''

def primos(numero:int):
    for i in range (2,numero):
        if (numero%i==0):
            return False
    return(True)

numero=int(input("Dime un numero: "))

if primos(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")