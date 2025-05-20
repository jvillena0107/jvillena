import random

def jugar():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    print("\n ¡Bienvenido al juego del número secreto!")
    print(" Adivina el número entre 1 y 10.")

    while True:
        try:
            intento = int(input(" Ingresa tu intento: "))
            intentos += 1

            if intento < numero_secreto:
                print(" Demasiado bajo. Intenta un número más grande.")
            elif intento > numero_secreto:
                print(" Demasiado alto. Intenta un número más pequeño.")
            else:
                print(f" ¡Felicidades! Adivinaste el número en {intentos} intentos.\n")
                break
        except ValueError:
            print(" Ingresa solo números, por favor.")

def iniciar_juego():
    while True:
        jugar()
        reiniciar = input(" ¿Quieres jugar otra vez? (s/n): ").lower()
        if reiniciar != "s":
            print(" ¡Gracias por jugar! Hasta la próxima.")
            break

# Ejecutar el juego
iniciar_juego()
