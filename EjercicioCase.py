name = []
lastName = []
age = []
email = []
password = []
confirmPassword = {}
opcion = 0
birthday = []

while True:
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
        name.append(input("Ingresa tu nombre: "))
        lastName.append(input("Ingresa tu apellido: "))
        age.append(int(input("Ingresa tu edad: ")))
        birthday.append(input("Ingresa tu fecha de nacimiento: "))
        email.append(("Ingresa tu correo electronico: "))
        password.append(("Ingresa tu contraseña: "))
        confirmPassword.append(input("Confirme tu contraseña: "))
        print ("Usuario registrado exitosamente, con el ID. " + str(len)(name) - 1)
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
      name.append(input("Ingresa tu nombre: "))
      lastName.append(input("Ingresa tu apellido: "))
      age.append(int(input("Ingresa tu edad: ")))
      birthday.append(input("Ingresa tu fecha de nacimiento: "))
      email.append(input("Ingresa tu correo electronico: "))
      password.append(input("Ingresa tu contraseña: "))
    case 5:
      print("¡Hasta luego!")
      break
    case _:
      print("Opción no válida")