## Se importan las librerías y funciones necesarias
import csv
import os
from funciones_opciones import menu, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

## Crea el archivo si no existe para asegurar formato correcto
def inicializar_archivo():
    if not os.path.exists("paises.csv"):
        with open("paises.csv", "w", newline='', encoding='utf-8-sig') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

## Lee el CSV y convierte cada fila en un diccionario
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
                ## Manejo simple por si un registro viene corrupto
                print(f"Error en los datos del país: {fila['nombre']}. Se omite.")
    return paises

## Bucle principal del programa
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
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

## Inicializa archivo y ejecuta el programa
inicializar_archivo()
main()
