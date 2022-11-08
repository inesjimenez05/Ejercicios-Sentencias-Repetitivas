'''
Ejercicio 12
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
al final de cada mes deposita cantidades variables de dinero; además, se quiere
saber cuánto lleva ahorrado cada mes.
'''
dineroahorrado=0
ahorro=0
mes=1

for mes in range (1,13):
    ahorro=int(input(f"Dinero depositado en el {mes} mes: "))
    dineroahorrado+=ahorro
    print (f"En el {mes}º mes, ha ahorrado {ahorro} € \n")
print (f"Al año, habrá ahorrado {dineroahorrado} €")