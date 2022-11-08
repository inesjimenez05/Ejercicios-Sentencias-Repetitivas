'''
Ejercicio 14
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra
en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
Realizar un programa para determinar en qué kilómetro de esa carretera se
encontrarán.
'''

d1=70
d2=150
d=d2-d1

while (d>0):
    d1=d1+1
    d2=d2-1
    d=d2-d1


print ("\n Se cruzarán en el kilometro: ",d2)

