def menu():
    print("\n" + "=" * 40)
    print("         GESTIÓN DE PAÍSES")
    print("=" * 40)
    print(" [1] Buscar país")
    print(" [2] Filtrar países")
    print(" [3] Ordenar países")
    print(" [4] Mostrar estadísticas")
    print(" [5] Salir")
    print("-" * 40)
    opcion = input("Elegí una opción -->: ").strip()

    return opcion


def buscar_pais(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
    
    nombre = input("Ingresá el nombre del país a buscar: ")
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {p}")
            return
    print("País no encontrado.")

def filtrar_paises(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
    
    continente = input("Ingresá el continente para filtrar: ")
    
 # Filtramos los países por continente
 
    paises_filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]

    
    # Mostramos los resultados
    if paises_filtrados:
        print(f"\n Países en {continente}:")
        print("-" * 40)
        for p in paises_filtrados:
            print(f"• {p['nombre']}")
            print(f"  Población: {p['poblacion']:,}".replace(",", "."))
            print(f"  Superficie: {p['superficie']:,} km²".replace(",", "."))
            print("-" * 40)
    else:
        print(f"No se encontraron países en el continente '{continente}'.")

def ordenar_paises(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
     
    criterio = input("Ingresá el criterio de ordenamiento (nombre, poblacion, superficie): ").lower()

    if criterio not in ["nombre", "poblacion", "superficie"]:
        print("Criterio inválido. Usando 'nombre' por defecto.")
        criterio = "nombre"

    while True:
        respuesta = input("¿Querés orden descendente? (s/n): ").strip().lower()
        if respuesta in ["s", "n"]:
            orden_desc = respuesta == "s"
            break
        print("Respuesta inválida. Escribí 's' o 'n'.")

    try:
        paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=orden_desc)
    except KeyError:
        print(f"Faltan datos en algunos países para ordenar por {criterio}.")
        return
    except TypeError:
        print(f"Los datos del criterio '{criterio}' no son consistentes (ej: texto mezclado con números).")
        return

    print(f"\nPaíses ordenados por {criterio} ({'descendente' if orden_desc else 'ascendente'}):")

    # Ordenar la lista
    paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=orden_desc)
    
    # Mostrar los resultados
    print(f"\nPaíses ordenados por {criterio} ({'descendente' if orden_desc else 'ascendente'}):")
    
    if criterio in ["poblacion", "superficie"]:
        for p in paises_ordenados:
            print(f"{p['nombre']}: {p[criterio]}")
    else:
        for p in paises_ordenados:
            print(f"{p[criterio]}")


def mostrar_estadisticas(paises):

    if not paises:
        print("No hay datos disponibles.")
        return
    
    # Cálculo de estadísticas
    mayor_poblacion = max(paises, key=lambda x: x["poblacion"])
    menor_poblacion = min(paises, key=lambda x: x["poblacion"])

    total_poblacion = sum(pais["poblacion"] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)

    total_superficie = sum(pais["superficie"] for pais in paises)
    promedio_superficie = total_superficie / len(paises)
    
    # Conteo de países por continente  
    paises_por_continente = {}
    for p in paises:
        continente = p["continente"]
        paises_por_continente[continente] = paises_por_continente.get(continente, 0) + 1

    print("\n" + "=" * 45)
    print("               ESTADÍSTICAS")
    print("=" * 45)

    print(f"\nPaís con mayor población:")
    print(f"  • Nombre: {mayor_poblacion['nombre']}")
    print(f"  • Población: {mayor_poblacion['poblacion']:,}".replace(",", "."))

    print(f"\nPaís con menor población:")
    print(f"  • Nombre: {menor_poblacion['nombre']}")
    print(f"  • Población: {menor_poblacion['poblacion']:,}".replace(",", "."))

    print("\nPromedios generales:")
    print(f"  • Población promedio: {promedio_poblacion:,.2f}".replace(",", "."))
    print(f"  • Superficie promedio: {promedio_superficie:,.2f} km²".replace(",", "."))

    print("\nCantidad de países por continente:")
    print("-" * 45)
    for continente, cantidad in paises_por_continente.items():
        print(f"  {continente:<15} → {cantidad}")
    print("-" * 45)
