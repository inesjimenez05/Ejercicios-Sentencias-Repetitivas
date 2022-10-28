'''
Ejercicio 3
Algoritmo que pida números hasta que se introduzca un cero. 
Debe imprimir la suma y la media de todos los números 
introducidos
'''

num=int(input("Di un numero \n"))
suma=0 
media=0
numero=0

while (num!=0):
    suma= num+suma
    numero=numero+1
    num=int(input("Di un numero: \n"))

print ("La suma es", suma)
print ("La media es",suma/numero)