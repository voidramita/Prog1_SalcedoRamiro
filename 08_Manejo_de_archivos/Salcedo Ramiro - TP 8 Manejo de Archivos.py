import os

ARCHIVO = "productos.txt"


## Crear archivo inicial con productos si no existe
def crear_archivo_inicial_si_no_existe():
    if not os.path.exists(ARCHIVO):
        print("No existe productos.txt, creando archivo inicial...")
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            
            ## nombre,precio,cantidad
            f.write("Lapicera,120.5,30\n")
            f.write("Cuaderno,550.0,15\n")
            f.write("Goma,80.0,50\n")


## Leer archivo y cargar productos
def leer_productos():
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(",")    ## ["Lapicera", "120.5", "30"]
                if len(partes) != 3:
                    continue

                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])

                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto)
    except FileNotFoundError:
        print("No se encontró el archivo.")
    return productos


## Mostrar productos
def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print("--------------------------\n")


## Agregar productos sin eliminar existentes
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    nuevo = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(nuevo)
    print("Producto agregado a la lista.\n")


## Buscar producto por nombre
def buscar_producto(productos):
    buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = None

    for p in productos:
        if p["nombre"].lower() == buscado.lower():
            encontrado = p
            break

    if encontrado:
        print("\n-------- PRODUCTO --------")
        print(f"Nombre: {encontrado['nombre']}")
        print(f"Precio: ${encontrado['precio']}")
        print(f"Cantidad: {encontrado['cantidad']}\n")
    else:
        print("No hay resultados.\n")


## Guardar todos los productos sobrescribiendo el archivo
def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)
    print("Archivo actualizado.\n")


def main():
    crear_archivo_inicial_si_no_existe()
    productos = leer_productos()

    while True:
        print("MENÚ:")
        print("1) Mostrar productos")
        print("2) Agregar producto")
        print("3) Buscar producto por nombre")
        print("4) Guardar y salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            guardar_productos(productos)
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, probá de nuevo.\n")


if __name__ == "__main__":
    main()
