# Sistema de Control de Calificaciones
# Actividad 2 - Ejercicio 1

# Lista donde se guardarán los estudiantes
estudiantes = []

# Capturar información de 5 estudiantes
print("=== REGISTRO DE ESTUDIANTES ===")
for i in range(5):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("Nombre: ")
    calificacion = int(input("Calificacion: "))

    # Crear diccionario por estudiante y agregarlo a la lista
    estudiante = {"nombre": nombre, "calificacion": calificacion}
    estudiantes.append(estudiante)

# Mostrar todos los estudiantes registrados
print("\n=== REPORTE DE CALIFICACIONES ===\n")
for est in estudiantes:
    print(f"{est['nombre']} - {est['calificacion']}")

# Calcular el promedio general
suma = 0
for est in estudiantes:
    suma = suma + est["calificacion"]

promedio = suma / len(estudiantes)
print(f"\nPromedio General: {promedio}")

# Encontrar la calificacion mas alta y el alumno que la obtuvo
mejor_calificacion = estudiantes[0]["calificacion"]
mejor_alumno = estudiantes[0]["nombre"]

for est in estudiantes:
    if est["calificacion"] > mejor_calificacion:
        mejor_calificacion = est["calificacion"]
        mejor_alumno = est["nombre"]

print(f"\nMejor Alumno:")
print(f"{mejor_alumno} - {mejor_calificacion}")

# Contar cuantos estudiantes aprobaron (calificacion >= 70)
aprobados = 0
for est in estudiantes:
    if est["calificacion"] >= 70:
        aprobados = aprobados + 1

print(f"\nAlumnos aprobados: {aprobados}")
