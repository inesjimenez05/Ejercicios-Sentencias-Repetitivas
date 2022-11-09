'''
Ejercicio 15
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.
'''

pago=5
num=0
mes=1
suma=0

for num in range (0,20):

    pago*=2
    print (f"El {mes}º mes, pagará {pago}")
    mes+=1
    suma+=pago

print (f"\n En total ha pagado {suma}")