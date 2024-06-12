import os
import msvcrt
import time

trabajdores = []
sueldo = 0
sueldosalud = sueldo * 0.07
sueldoafp = sueldo * 0.12

while True:
    print("""
          1. Registrar trabajador
          2. Listar todos los trabajadores
          3. Imprimir planilla de sueldos 
          4. Salir del programa """)
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Error, opcion no disponible!")
        except:
            print("Error, solo se permiten valores numericos")

    os.system("cls")

    if opc==1:
        print("Registrar trabajdor")
        #Validacion 
        while True:
            nombre = input("Ingrese nombre: ")
            if len(nombre) > 3:
                break
            else:
                print("Error, el nombre debe contener al menos 3 letras")
        while True:     
            apellido = input("Ingrese apellido: ")
            if len(apellido) > 3:
                break
            else:
                print("Error, el apellido debe contener al menos 3 letras")
        while True:
            cargo = input("Ingrese cargo: ").upper()
            if cargo == "CEO" or cargo == "DESARROLLADOR" or cargo == "ANALISTA DE DATOS":
                break
            else:
                print("Error, cargo no existente")
        while True:
            try:
                sueldo = int(input("Ingrese sueldo (BRUTO): "))
                if sueldo > 0 :
                    break
                else:
                    print("Error, el sueldo debe ser mayor a 0")
            except:
                print("Error, solo se permiten valores numericos")
        #Mensaje 
        os.system("cls")
        print("Usuario registrado!")
        time.sleep(2)
        #Diccionario
        trabajdores.append({
            "nombre": nombre,
            "apellido": apellido,
            "cargo": cargo,
            "sueldo": sueldo
        })

    elif opc==2:
        print("Listar trabajadores")
        for x in (trabajdores):
            print(f"Nombre: {x["nombre"]}, Cargo: {x["cargo"]} Sueldo Bruto: {x["sueldo"]} Desc. Salur {x["sueldosalud"]}")

    elif opc==3:
        print("Imprimir planilla")
    else:
        print("Adios!")
        break