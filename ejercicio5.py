'''
Ejercicio 5
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
en caso contrario, el programa termina cuando se introduce un espacio.
'''

caracter=input("Introduce un caracter: \n")

while (caracter!= " " ):

    if (caracter== "a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u"):
        print ("VOCAL")
    else:
        print ("NO VOCAL")
        
    caracter=input("Introduce un caracter: \n")