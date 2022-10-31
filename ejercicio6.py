'''
Ejercicio 6
Escribir un programa que imprima todos los números pares entre dos 
números que se le pidan al usuario
'''
num1=int(input("Di un numero: \n"))
num2=int(input("Di otro numero: \n"))

for num in range (num1,num2):
   
    if (num%2==0):
        print ("\n",num)
