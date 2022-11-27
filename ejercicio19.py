'''
Ejercicio 19
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.
'''
def menu (num:int):
    while (num!=4):
        print("1.Ver contactos")
        print("2.Añadir contactos")
        print("3.Eliminar contactos")
        print("4.Salir")
        num=int(input("Seleccionar menu: "))
    
    return(num)

numero=2
menu(numero)



