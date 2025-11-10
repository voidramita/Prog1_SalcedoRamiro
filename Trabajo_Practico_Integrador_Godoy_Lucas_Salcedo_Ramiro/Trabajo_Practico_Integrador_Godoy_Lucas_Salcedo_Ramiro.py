import csv
import os

from funciones_opciones import menu, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

def inicializar_archivo():
    if not os.path.exists("paises.csv"):
        with open("paises.csv", "w", newline='', encoding='utf-8-sig') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "continente", "poblacion", "superficie"])

def leer_csv(ruta):
    paises = []
    with open(ruta, "r", newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                paises.append(fila)
            except ValueError:
                print(f"Error al convertir datos del país: {fila['nombre']}. Se omite este registro.")
    return paises


def main():

    paises = leer_csv("paises.csv")

    while True:
        opcion = menu()
        if opcion == "1":
            buscar_pais(paises)
        elif opcion == "2":
            filtrar_paises(paises)
        elif opcion == "3":
            ordenar_paises(paises)
        elif opcion == "4":
            mostrar_estadisticas(paises)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

inicializar_archivo()
main()