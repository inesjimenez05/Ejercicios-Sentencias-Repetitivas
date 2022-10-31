'''
Ejercicio 7
Realizar una algoritmo que muestre la tabla de multiplicar de un
número introducido por teclado
'''

numero=int(input("Di un numero: \n"))

for num in range (0,11):
    print(numero,"*", num, "=", num*numero)