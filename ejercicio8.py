'''
Ejercicio 8
Escribe un programa que pida el limite inferior y superior de un 
intervalo. Si el límite inferior es mayor que el superior lo tiene 
que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos
el 0.
Cuando termine el programa dará las siguientes informaciones:
1 La suma de los números que están dentro del intervalo 
  (intervalo abierto).
2 Cuantos números están fuera del intervalo.
3 He informa si hemos introducido algún número igual a los límites 
del intervalo
'''

inferior= int(input("Di el límite inferior: \n"))
superior= int(input("Di el límite superior: \n"))
suma=0

while (inferior>superior):
    inferior= int(input("Ponga un límite inferior menor al superior: \n"))
    

numeros=int(input("Di un numero: \n"))

while (numeros!=0):
    vNumeros=[]
    vNumeros.append(numeros)
    numeros=int(input("Di un numero: \n"))

for vNumeros in range (inferior, superior):
    print ("\n",vNumeros)
