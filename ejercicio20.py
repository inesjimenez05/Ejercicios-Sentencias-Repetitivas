'''
Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar
'''
numeros=int(input("Cantidad nº primos: "))
vNum=[]

def primos(num:int):
    for i in range (2,num):
        if (num%i==0):
            return(False)
    return(True)

for i in range (1,numeros+1):
    if primos(i):
        vNum.append(i)

print(vNum)