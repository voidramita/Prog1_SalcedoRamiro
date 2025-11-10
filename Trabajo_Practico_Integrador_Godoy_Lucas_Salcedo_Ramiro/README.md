# README

## Descripción del programa
Este programa permite gestionar y analizar información de países a partir de un archivo CSV previamente cargado. Ofrece opciones para buscar países, filtrarlos por continente, ordenarlos según diferentes criterios y mostrar estadísticas generales sobre la población y superficie. Está diseñado para ser fácil de usar desde la consola.

## Instrucciones de uso
1. Ejecutá el programa en Python.
2. Asegurate de tener el archivo CSV con los datos de países en el mismo directorio o en la ruta configurada.
3. El menú principal te permitirá:
   - Cargar datos desde el archivo.
   - Buscar un país por nombre.
   - Filtrar países por continente.
   - Ordenar países por nombre, población o superficie.
   - Ver estadísticas generales.
   - Salir del programa.
4. Ingresá la opción correspondiente según lo que quieras hacer.

## Ejemplos de entradas y salidas
**Ejemplo 1: Búsqueda de país**
Entrada:
```
Ingresá el nombre del país a buscar: Argentina
```
Salida:
```
País encontrado: {'nombre': 'Argentina', 'continente': 'América', 'poblacion': 45376763, 'superficie': 2780400}
```

**Ejemplo 2: Filtrado por continente**
Entrada:
```
Ingresá el continente para filtrar: Europa
```
Salida:
```
Países en Europa:
----------------------------------------
• España
  Población: 47.450.795
  Superficie: 505.990 km²
----------------------------------------
• Francia
  Población: 65.312.000
  Superficie: 643.801 km²
----------------------------------------
```

**Ejemplo 3: Ordenamiento**
Entrada:
```
Ingresá el criterio de ordenamiento (nombre, poblacion, superficie): poblacion
¿Querés orden descendente? (s/n): s
```
Salida:
```
Países ordenados por poblacion (descendente):
China: 1.412.600.000
India: 1.366.400.000
Estados Unidos: 331.900.000
...
```

## Participación de los integrantes
Ambos integrantes del grupo trabajaron de manera conjunta en todas las funciones del programa. No hubo división de tareas: cada parte del código fue desarrollada, revisada y probada por los dos al mismo tiempo, colaborando de forma constante durante todo el proyecto.