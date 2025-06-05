import json
import os
fichero = "baseDatos.json"
baseDatos = []


def printLista():
    with open(fichero, "r") as file:
        dato = json.load(file)
    if len(dato) > 0:
        with open(fichero, "r") as file:
            data = json.load(file)
            try:
                for i in data:
                    print(f"""\n   {i["name"]} (ID: {i["id"]}) 
        - Telefono: {i["phone"]}
        - Email: {i["email"]}
                        """)
            except Exception as e:
                print(f"Error Inesperado\n{e}")

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def asignarId(idd):
    with open(fichero, "r") as file:
        data = json.load(file)
    
    if len(data) > 0:
        for i in data:
            if i["id"] == idd:
                idd += 1
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
                print("Contacto añadido!..")
                input("Continuar...")
                break

def updateContact():
    limpiarConsola()
    
    while True:
        limpiarConsola()
        with open(fichero, "r") as file:
            baseDatos = json.load(file)
        print("[  Actualizar Contacto  ]\n")
        print(" 1. Cambiar Nombre\n 2. Cambiar Telefono\n 3. Cambiar Email\n 4. Regresar")
        opcion = int(input("\nIngresar opcion: "))
        if opcion == 1:
            limpiarConsola()
            printLista()
            id = int(input("Ingresar ID del contacto: "))
            for i in range(len(baseDatos)):
                if baseDatos[i]["id"] == id:
                    name = input("Ingresar nuevo nombre: ")
                    baseDatos[i]["name"] = name
                    print(baseDatos[i])
                    with open(fichero, "w") as file:
                        json.dump(baseDatos, file, indent=2)
                    print("Nombre actualizado correctamente.")
                    input("Continuar...")
                    break
                elif baseDatos[i]["id"] != id and i == len(baseDatos):
                    print(f"El ID({id}) ingresado no pertenece a ningun contacto.")
                    input("Continuar...")
                    break

        elif opcion == 2:
            limpiarConsola()
            printLista()
            id = int(input("Ingresar ID del contacto: "))
            
            if len(baseDatos) > 0:
                print(baseDatos)
                for i in baseDatos:
                    if i["id"] == id:
                        phone = int(input("Ingresar nuevo telefono: "))
                        for x in baseDatos:
                            if x["phone"] != phone and x != len(baseDatos):
                                x["phone"] = phone
                                with open(fichero, "w") as file:
                                    json.dump(baseDatos, file, indent=2)
                                print("Telefono actualizado correctamente.")
                                input("Continuar...")
                                break
                            else:
                                print("Error: Al parecer ya tienes un contacto con ese numero..")
                                input("Continuar...")    
                                break
                    elif i["id"] != id and i == len(baseDatos):
                        print(f"El ID({id}) ingresado no pertenece a ningun contacto.")
                        input("Continuar...")
                        break

        elif opcion == 3:
            limpiarConsola()
            printLista()
            id = int(input("Ingresar ID del contacto: "))
            for i in baseDatos:
                if i["id"] == id:
                    email = input("Ingresar nuevo email: ")
                    i["email"] = email
                    with open(fichero, "w") as file:
                        json.dump(baseDatos, file, indent=2)
                    print("Email actualizado correctamente.")
                    input("Continuar...")
                    break
                elif i["id"] != id and i == len(baseDatos):
                    print(f"El ID({id}) ingresado no pertenece a ningun contacto.")
                    input("Continuar...")
                    break
        elif opcion == 4:
            break
        else:
            print("Opcion no valida.")

def deleteContact():
    limpiarConsola()
    print("[  Eliminar Contacto  ]")
    printLista()
    with open(fichero, "r") as file:
        baseDatos = json.load(file)
    id = int(input("Ingresar ID del contacto a eliminar: "))
    if len(baseDatos) > 0:
        for i in range(len(baseDatos)):
            if baseDatos[i]["id"] == id:
                del baseDatos[i]
                with open(fichero, "w") as file:
                    json.dump(baseDatos, file, indent=2)
                print("Contacto eliminado correctamente.")
                input("Continuar...")
                break
            elif i == len(baseDatos) - 1:
                print(f"El ID({id}) ingresado no pertenece a ningun contacto.")
                input("Continuar...")
                break
    else:
        print("No hay contactos para eliminar.")
        input("Continuar...")

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
    with open(fichero, "r") as file:
        baseDatos = json.load(file)

    limpiarConsola()
    print(menu)
    opcion = int(input("Ingresar opcion: "))

    if opcion == 1:
        addContact()
    elif opcion == 2:
        printBaseDatos()
    elif opcion == 3:
        if len(baseDatos) > 0:
            updateContact()
        else:
            limpiarConsola
            print("No hay contactos para actualizar.")
            input("Continuar...")
    elif opcion == 4:
        if len(baseDatos) > 0:
            deleteContact()
        else:
            limpiarConsola
            print("No hay contactos para eliminar.")
            input("Continuar...")
    elif opcion == 5:
        limpiarConsola()
        print("Vuelva pronto!")
        break
    else:
        pass


