nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
nacionalidad = input("Ingresa tu nacionalidad: ")

if edad >=18: #el if va seguido de la condicion y dos puntos
    print("Eres mayor de edad")
else: #el else va seguido de dos puntos para decir que se hace si no se cumple la funcion del if
    print("Eres menor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")