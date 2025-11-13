## Muestra el menú principal y devuelve la opción elegida
def menu():
    print("\n" + "=" * 40)
    print("         GESTIÓN DE PAÍSES")
    print("=" * 40)
    print(" [1] Buscar país")
    print(" [2] Filtrar países")
    print(" [3] Ordenar países")
    print(" [4] Estadísticas")
    print(" [5] Salir")
    print("-" * 40)
    return input("Elegí una opción --> ").strip()


## Busca un país por nombre
def buscar_pais(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    
    nombre = input("Ingresá el nombre del país: ")

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {p}")
            return
    
    print("País no encontrado.")


## Filtra países por continente usando list comprehension
def filtrar_paises(paises):
    if not paises:
        print("No hay datos cargados.")
        return

    cont = input("Ingresá el continente: ").strip()

    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]

    if not filtrados:
        print(f"No hay países en '{cont}'.")
        return

    print(f"\nPaíses en {cont}:")
    print("-" * 40)

    for p in filtrados:
        print(f"• {p['nombre']}")
        print(f"  Población: {p['poblacion']:,}".replace(",", "."))
        print(f"  Superficie: {p['superficie']:,} km²".replace(",", "."))
        print("-" * 40)


## Ordena países según criterio elegido por el usuario
def ordenar_paises(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    
    criterio = input("Criterio (nombre, poblacion, superficie): ").lower()

    if criterio not in ["nombre", "poblacion", "superficie"]:
        print("Criterio inválido. Se usa 'nombre'.")
        criterio = "nombre"

    desc = input("¿Querés orden descendente? (s/n): ").strip().lower() == "s"

    try:
        ordenados = sorted(paises, key=lambda x: x[criterio], reverse=desc)
    except Exception:
        print("Error al ordenar.")
        return

    print(f"\nPaíses ordenados por {criterio}:")
    print("-" * 40)

    for p in ordenados:
        dato = p[criterio]
        
        ## Formato prolijo si es número grande
        if criterio in ["poblacion", "superficie"]:
            dato = f"{dato:,}".replace(",", ".")

        print(f"{p['nombre']}: {dato}")


## Calcula estadísticas generales
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    total_p = sum(p["poblacion"] for p in paises)
    total_s = sum(p["superficie"] for p in paises)

    prom_p = total_p / len(paises)
    prom_s = total_s / len(paises)

    ## Conteo por continente
    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1

    print("\n" + "=" * 45)
    print("               ESTADÍSTICAS")
    print("=" * 45)

    print(f"\nPaís con mayor población: {mayor['nombre']} ({mayor['poblacion']:,})".replace(",", "."))
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']:,})".replace(",", "."))

    print(f"\nPoblación promedio: {prom_p:,.2f}".replace(",", "."))
    print(f"Superficie promedio: {prom_s:,.2f} km²".replace(",", "."))

    print("\nCantidad por continente:")
    print("-" * 40)
    for cont, cant in conteo.items():
        print(f"{cont}: {cant}")
