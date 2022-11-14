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
sueldototal=0


for num in range (1, empleados+1):
    sueldo=0
    for i in range (1, diastrabajados+1):
        horastrabajadas=int(input(f"Horas trabajadas el {i} día: por el {num} trabajador: "))
        sueldo=sueldo+(horastrabajadas*sueldohora)
        sueldosemanal=sueldo
    print(f"El sueldo semanal del empleado {num} es de {sueldo}")
    sueldototal+=sueldo


print(f"La empresa paga a la semana {sueldototal} por {empleados} empleados")