'''
Ejercicio 17
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados.
'''

horastrabajadas=0
diastrabajados=int(input("Días trabajados: "))
sueldo=0
empleados=int(input("Numero empleados: "))
sueldohora=int(input("Sueldo hora: "))

for i in range (1, diastrabajados+1):
    horastrabajadas=int(input(f"Horas trabajadas el {i} día:"))
    sueldo=sueldo+(horastrabajadas*sueldohora)

print("El sueldo semanal de un empleado es de ", sueldo)
print(f"La empresa paga a la semana {sueldo*empleados} por {empleados} empleados")