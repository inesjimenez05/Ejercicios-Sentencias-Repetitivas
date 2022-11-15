'''
Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.
'''
import time
h=0
m=0
s=0

for h in range (24):
  for m in range (60):
    for s in range(60):
      for i in range (0,7):
        print ()
      time.sleep(1)
      print(f"{h}:{m}:{s}")
    
