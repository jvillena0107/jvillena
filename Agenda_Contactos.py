# Diccionario para guardar los contactos
agenda = {}

def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    agenda[nombre] = {"telefono": telefono, "correo": correo}
    print(" Contacto agregado con éxito.\n")

def listar_contactos():
    if not agenda:
        print(" No hay contactos guardados.\n")
        return
    print("\n Lista de contactos:")
    for nombre, datos in agenda.items():
        print(f"- {nombre}: Tel: {datos['telefono']}, Email: {datos['correo']}")
    print()

def buscar_contacto():
    criterio = input(" Buscar por nombre o número: ")
    encontrado = False
    for nombre, datos in agenda.items():
        if criterio == nombre["nombre"] or criterio == datos["telefono"]:
            print(f" Encontrado: {nombre['nombre']} - Tel: {datos['telefono']}, Email: {datos['correo']}\n")
            encontrado = True
            break
    if not encontrado:
        print(" Contacto no encontrado.\n")

def eliminar_contacto():
    nombre = input(" Nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f" Contacto '{nombre}' eliminado.\n")
    else:
        print(" Contacto no encontrado.\n")

def contar_contactos():
    print(f" Total de contactos guardados: {len(agenda)}\n")

def mostrar_menu():
    print(" Agenda de Contactos")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar cantidad de contactos")
    print("6. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        listar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        contar_contactos()
    elif opcion == "6":
        print(" ¡Hasta luego!")
        break
    else:
        print(" Opción inválida. Intenta de nuevo.\n")
