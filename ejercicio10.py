'''
Ejercicio 10
Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''
tabla=0

def tablas (num):
    for i in range (0, 11):
        print (f"{num}*{i}={num*i}")
    return tablas

for num in range (1,6):
    print (tablas)
    
