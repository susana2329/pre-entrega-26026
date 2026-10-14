# Revisado con IA

productos = []

while True:
    print("=" * 40)
    print("Sistema de gestion de productos")
    print("=" * 40)
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegi una opcipn (1-5): ").strip()

    if opcion == "1":
        print("--- Agregar producto ---")

        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip()
        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresa solo numeros positivos.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)
        print("Producto agregado.")

    elif opcion == "2":
        print("--- Lista de productos ---")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID: {i+1}\n-Nombre: {productos[i][0]}\n-Categoría: {productos[i][1]}\n-Precio: ${productos[i][2]}")

    elif opcion == "3":
        print("--- Buscar producto ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print("Error: escribi algo para buscar.")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"ID: {i+1}\n-Nombre: {productos[i][0]}\n-Categoría: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("No se encontro ningun resultado.")
            else:
                print(f"Productos encontrados: {encontrado}")

    elif opcion == "4":
        print("--- Eliminar producto ---")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")

            id_eliminar = input("Numero de producto a eliminar: ").strip()

            while not id_eliminar.isdigit():
                print("Error: ingresa un numero.")
                id_eliminar = input("Numero de producto a eliminar: ").strip()

            posicion = int(id_eliminar) - 1

            if posicion < 0 or posicion >= len(productos):
                print("Error: ese numero de producto no existe.")
            else:
                eliminado = productos.pop(posicion)
                print(f"Se elimino el producto: {eliminado[0]}")

    elif opcion == "5":
        print("Gracias por usar nuestro sistema")
        break

    else:
        print("Opción no valida. Tenés que elegir entre (1-5).")