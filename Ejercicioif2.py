nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18: #el if va seguido de la condicion y dos puntos
    print("Eres es mayor de edad")
else: #el else va seguido de la condicion y dos puntos
    print("Eres menor de edad")

if nacionalidad == "mexicana": #el if va seguido de la condicion y dos puntos
    print("Eres de nacionalidad mexicana")
else: 
    print("No eres de nacionalidad mexicana")
    