import json
import os
fichero = "baseDatos.json"
baseDatos = []

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def asignarId(idd):
    with open(fichero, "r") as file:
        data = json.load(file)
    
    if len(data) > 0:
        for i in data:
            if i["id"] == idd:
                idd += 1
                break
            else:
                idd = idd
                break
    else:
        idd = 1
    return idd
        
def printBaseDatos():
    limpiarConsola()
    with open(fichero, "r") as file:
        dato = json.load(file)
    print("[  Contactos  ]")
    if len(dato) > 0:
        with open(fichero, "r") as file:
            data = json.load(file)
            try:
                for i in data:
                    print(f"""\n   {i["name"]} (ID: {i["id"]}) 
    - Telefono: {i["phone"]}
    - Email: {i["email"]}
                    """)
                input("Continuar...")
            except Exception as e:
                print(f"Error Inesperado\n{e}")
                input("Continuar...")
    else:
        print(f"\nAun no tienes contactos.. pinche antisocial\n")
        input("Continuar...")

def addContact():
    limpiarConsola()
    print("[  Añadir Contacto  ]")
    with open(fichero, "r") as file:
        baseDatos = json.load(file)
    id = asignarId(1)
    name = input("Asignar nombre:  ")
    phone = int(input("Asignar Telefono: "))
    email = input("Asignar Email: ")
    
    if len(baseDatos) == 0:
        with open(fichero, "w") as file:
            baseDatos.append({"id": id, "name": name, "phone": phone, "email": email})
            json.dump(baseDatos, file, indent=2)
            print("Contacto añadido!..")
            input("Continuar...")    
    elif len(baseDatos) > 0:
        for i in baseDatos:
            if i["phone"] == phone:
                print("Error: Al parecer ya tienes un contacto con ese numero..")
                input("Continuar...")
                del baseDatos[len(baseDatos) - 1]
                break
            else:
                baseDatos.append({"id": id, "name": name, "phone": phone, "email": email})
                with open(fichero, "w") as file:
                    json.dump(baseDatos, file, indent=2)
                print("Contacto añadidooo!..")
                input("Continuar...")
                break
def updateContact():
    limpiarConsola()
    
    while True:
        print("[  Actualizar Contacto  ]\n")
        print(" 1. Cambiar Nombre\n 2. Cambiar Telefono\n 3. Cambiar Email\n 4. Regresar")
        opcion = int(input("Ingresar opcion"))
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("Opcion no valida.")

menu = """

    █░█░█ █░█ ▄▀█ ▀█▀ █▀ ▄▀█ █▀█ █▀█
    ▀▄▀▄▀ █▀█ █▀█ ░█░ ▄█ █▀█ █▀▀ █▀▀
    
    1. Crear contacto.
    2. Mostrar contactos.
    3. Actualizar contactos.
    4. Eliminar contacto.
    5. Cerrar whatsapp.

"""

while True:
    limpiarConsola()
    print(menu)
    opcion = int(input("Ingresar opcion: "))

    if opcion == 1:
        addContact()
    elif opcion == 2:
        printBaseDatos()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass


