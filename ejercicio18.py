'''
Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.
'''

tiempo=0

def contarSegundos(tiempo:int):
  segundos=0
  for i in range (0,tiempo):
    segundos+=1
  return (segundos)
