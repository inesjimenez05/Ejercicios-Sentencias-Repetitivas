'''
Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
'''

numEmpleados=int(input("Numero de empleados: "))
numHoras=int(input("Horas trabajadas al dia: "))
sueldoHoras=int(input("Sueldo por hora: "))
sueldo=0
sueldototal=0
dias=int(input("Dias trabajados: "))

for num in range (0, numEmpleados):
    for i in range (0,dias):
        sueldo+=(sueldoHoras*numHoras)
    sueldototal+=sueldo

print(f"El sueldo semanal de un empleado es de {sueldo}")
print(f"La empresa ha pagado {sueldototal} por los {numEmpleados} empleados")