
'''Ejercicio 13
Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el
sueldo que recibirá por las horas trabajadas.
'''
horas=int(input("Total de horas trabajadas: "))
sueldohora=int(input("Cual es el sueldo por hora?:"))
sueldo=0
horastrabajadas=0

for num in range (0,6):
    sueldo=sueldo+(horas*sueldohora)
    horastrabajadas=horas+horastrabajadas

print(f"El sueldo es de {sueldo}")
print(f"Las horas trabajadas son de {horastrabajadas}")
