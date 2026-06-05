# Estadisticas de una Lista de Numeros
# Actividad 2 - Ejercicio 3

# Lista donde se guardarán los numeros
numeros = []

# Pedir 10 numeros al usuario
print("\n=== INGRESA 10 NUMEROS ENTEROS ===")
for i in range(10):
    numero = int(input(f"Numero {i + 1}: "))
    numeros.append(numero)

# 1. Mostrar la lista completa
lista_formateada = "[" + ",".join(str(n) for n in numeros) + "]"
print(f"\nLista: {lista_formateada}")

# 2. Encontrar el numero mayor (sin usar max())
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num

print(f"Mayor: {mayor}")

# 3. Encontrar el numero menor (sin usar min())
menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num

print(f"Menor: {menor}")

# 4. Calcular la suma total
suma = 0
for num in numeros:
    suma = suma + num

print(f"Suma: {suma}")

# 5. Calcular el promedio
promedio = suma / len(numeros)
print(f"Promedio: {promedio}")

# 6. Contar cuantos numeros son pares
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares = pares + 1

print(f"Pares: {pares}")

# 7. Contar cuantos numeros son impares
impares = 0
for num in numeros:
    if num % 2 != 0:
        impares = impares + 1

print(f"Impares: {impares}")

# 8. Lista con numeros mayores al promedio
mayores_al_promedio = []
for num in numeros:
    if num > promedio:
        mayores_al_promedio.append(num)

mayores_formateada = "[" + ",".join(str(n) for n in mayores_al_promedio) + "]"
print(f"Mayores al promedio:")
print(mayores_formateada)
