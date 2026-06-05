# Inventario de Productos
# Actividad 2 - Ejercicio 2

# Lista donde se guardarán los productos
inventario = []

# Variable para controlar el menu
opcion = 0

while opcion != 5:
    # Mostrar el menu
    print("\n=== MENU DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Calcular valor total del inventario")
    print("5. Salir")

    opcion = int(input("\nElige una opcion: "))

    # Opcion 1 - Agregar producto
    if opcion == 1:
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio: "))
        cantidad = int(input("Cantidad disponible: "))

        # Crear diccionario del producto y agregarlo a la lista
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")

    # Opcion 2 - Mostrar inventario
    elif opcion == 2:
        if len(inventario) == 0:
            print("El inventario esta vacio.")
        else:
            print("\n=== INVENTARIO ===")
            for prod in inventario:
                print(f"\n{prod['nombre']}")
                print(f"Precio: {prod['precio']}")
                print(f"Cantidad: {prod['cantidad']}")

    # Opcion 3 - Buscar producto
    elif opcion == 3:
        nombre_buscar = input("Nombre del producto a buscar: ")
        encontrado = False

        for prod in inventario:
            # Comparar en minusculas para que no importe si esta en mayusculas
            if prod["nombre"].lower() == nombre_buscar.lower():
                print(f"\nProducto encontrado:")
                print(f"Nombre: {prod['nombre']}")
                print(f"Precio: {prod['precio']}")
                print(f"Cantidad: {prod['cantidad']}")
                encontrado = True

        if encontrado == False:
            print("Producto no encontrado.")

    # Opcion 4 - Calcular valor total del inventario
    elif opcion == 4:
        if len(inventario) == 0:
            print("El inventario esta vacio.")
        else:
            valor_total = 0
            print("\n=== VALOR DEL INVENTARIO ===")

            for prod in inventario:
                valor_producto = prod["precio"] * prod["cantidad"]
                print(f"{prod['nombre']}: {prod['precio']} x {prod['cantidad']} = {valor_producto}")
                valor_total = valor_total + valor_producto

            print(f"\nValor total del inventario: {valor_total}")

    # Opcion 5 - Salir
    elif opcion == 5:
        print("Hasta luego!")

    # Opcion invalida
    else:
        print("Opcion invalida, intenta de nuevo.")

