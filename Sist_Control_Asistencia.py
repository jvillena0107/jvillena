# Sistema de Control de Asistencia

# Paso 1: Ingreso de nombres de estudiantes (máx. 30)
estudiantes = [] #lista
estado_asistencia = {} #Diccionario

print("Registro de estudiantes (máximo 30)")
while len(estudiantes) < 30:
    nombre = input(f"Ingrese el nombre del estudiante #{len(estudiantes)+1} (o escriba 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    if nombre != "":
        estudiantes.append(nombre)
        estado_asistencia[nombre] = "Ausente"  # valor por defecto

print("\nAhora vamos a registrar la asistencia:")
# Paso 2: Registrar asistencia
for estudiante in estudiantes:
    asistencia = input(f"¿{estudiante} está presente? (s/n): ").lower()
    if asistencia == "s":
        estado_asistencia[estudiante] = "Presente"

# Paso 3: Mostrar resultados
presentes = [nombre for nombre, estado in estado_asistencia.items() if estado == "Presente"]
ausentes = [nombre for nombre, estado in estado_asistencia.items() if estado == "Ausente"]

print("\n Lista de Presentes:")
for nombre in presentes:
    print(f"- {nombre}")

print("\n Lista de Ausentes:")
for nombre in ausentes:
    print(f"- {nombre}")

# Paso 4: Calcular porcentaje de asistencia
total = len(estudiantes)
porcentaje = (len(presentes) / total) * 100 if total > 0 else 0
print(f"\n Porcentaje de asistencia: {porcentaje:.2f}%")

# Paso 5: Buscar estudiante
buscar = input("\n ¿Deseas buscar a un estudiante? (s/n): ").lower()
if buscar == "s":
    nombre_busqueda = input("Ingresa el nombre del estudiante: ")
    estado = estado_asistencia.get(nombre_busqueda, "Estudiante no encontrado.")
    print(f"{nombre_busqueda}: {estado}")
