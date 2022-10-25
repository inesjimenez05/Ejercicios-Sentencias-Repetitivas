'''
Ejercicio 3
Algoritmo que pida números hasta que se introduzca un cero. 
Debe imprimir la suma y la media de todos los números 
introducidos
'''

num=int(input("Di un numero \n"))
suma=0 
media=0
numero=1

while (num!=0):
    suma= num+suma
    numero=numero+1
    print (suma)
    num=int(input("Di un numero: \n"))
    print (suma/numero)
