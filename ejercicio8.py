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


limiteinferior=5
limitesuperior=2

def operacionesNumeros(vNum,limiteinferior,limitesuperior):
    num=0
    #SUMA, NUMEROS FUERA E IGUALES AL LIMITE
    suma=0
    fuera=0
    igualLimite=0
    vLimites= list(range(limiteinferior+1,limitesuperior))
    for num in (vNum):
        if num in vLimites:
            suma+=num
        else:
            fuera+=1
        if (num==limiteinferior or num==limitesuperior):
            igualLimite+=1

    print(f"{suma}: es la suma de los numeros dentro del intervalo, {fuera}: cantidad de numeros fuera del intervalo, {igualLimite}: cantidad de numeros iguales a los limites")


def pideNumeros ():
    listaNum= []
    num=2
    while num!=0:
        num=int(input("Introduce un numero: "))
        listaNum.append(num)

    return(listaNum)


while (limiteinferior > limitesuperior):
    try:
        limiteinferior=int(input("Escribe el valor del limite inferior: "))
        limitesuperior= int(input("Escribe el valor del limite superior: "))
    except:
        print("Escribe el valor de los limites: ")

vNum=pideNumeros()
operacionesNumeros(vNum,limiteinferior,limitesuperior)

