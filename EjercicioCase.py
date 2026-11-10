name = ""
lastName = ""
age = 0
email = ""
password = ""
confirmPassword = ""
opcion = 0
birthday = ""

print("Bienvenido al sistema de registro de usuarios")
print("------MENU PRINCIPAL------")
print("1. Registrar usuario")
print("2. Ver informacion del usuario")
print("3. Borrar información del usuario")
print("4. Modificar información del usuario")
print("5. Salir")
print("--------------------------")
opcion = int(input("Seleccione una opción: "))

match opcion: #Aqui inicia el match, que es una validación de caso

    case 1:
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ")
        age = int(input("Ingresa tu edad: "))
        birthday = input("Ingresa tu fecha de nacimiento: ")
        email = input("Ingresa tu correo electronico: ")
        password = input("Ingresa tu contraseña: ")
        confirmPassword = input("Confirme tu contraseña: ")
    case 2:
      print  ("Nombre: ", name, "Edad: ", age, "Fecha de nacimiento:", birthday, "Correo electronico: ", email, "Contraseña: ", password)
    case 3:
      name = ""
      lastName = ""
      age = 0
      birthday = ""
      email = ""
      password = ""
    case 4:
      name = input("Ingresa tu nombre: ")
      lastName = input("Ingresa tu apellido: ")
      age = int(input("Ingresa tu edad: "))
      birthday = input("Ingresa tu fecha de nacimiento: ")
      email = input("Ingresa tu correo electronico: ")
      password = input("Ingresa tu contraseña: ")
    case 5:
      print("¡Hasta luego!")
    case _:
      print("Opción no válida")