# Menú del restaurante (nombre: precio)
menu = {
    "1": {"nombre": "Hamburguesa", "precio": 25.0},
    "2": {"nombre": "Pizza", "precio": 30.0},
    "3": {"nombre": "Ensalada", "precio": 18.0},
    "4": {"nombre": "Sopa", "precio": 12.0},
    "5": {"nombre": "Refresco", "precio": 8.0}
}

ventas_totales = 0  # Acumulador de todas las ventas del día

def mostrar_menu():
    print("\nMenú del Restaurante:")
    for clave, plato in menu.items():
        print(f"{clave}. {plato['nombre']} - Bs {plato['precio']}")

def tomar_pedido():
    global ventas_totales
    pedido = {}
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número del plato (o 'fin' para terminar): ")
        if opcion.lower() == "fin":
            break
        if opcion in menu:
            cantidad = int(input(f"¿Cuántas unidades de {menu[opcion]['nombre']}?: "))
            if opcion in pedido:
                pedido[opcion]["cantidad"] += cantidad
            else:
                pedido[opcion] = {
                    "nombre": menu[opcion]["nombre"],
                    "precio": menu[opcion]["precio"],
                    "cantidad": cantidad
                }
        else:
            print("Opción no válida. Intenta de nuevo.")
    
    if not pedido:
        print("No se hizo ningún pedido.\n")
        return

    total = 0
    print("\n Detalle del pedido:")
    for plato in pedido.values():
        subtotal = plato["precio"] * plato["cantidad"]
        total += subtotal
        print(f"- {plato['nombre']} x {plato['cantidad']} = Bs {subtotal:.2f}")
    
    iva = total * 0.13
    total_con_iva = total + iva
    print(f"Subtotal: Bs {total:.2f}")
    print(f"IVA (13%): Bs {iva:.2f}")
    print(f"Total a pagar: Bs {total_con_iva:.2f}\n")

    ventas_totales += total_con_iva

def ver_ventas_del_dia():
    print(f"Ventas totales del día: Bs {ventas_totales:.2f}\n")

def menu_principal():
    while True:
        print("Bienvenido al Restaurante")
        print("1. Hacer un pedido")
        print("2. Ver ventas totales del día")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            tomar_pedido()
        elif opcion == "2":
            ver_ventas_del_dia()
        elif opcion == "3":
            print("¡Gracias por usar el sistema del restaurante!")
            break
        else:
            print("Opción inválida, intenta nuevamente.\n")

# Ejecutar el programa
menu_principal()
