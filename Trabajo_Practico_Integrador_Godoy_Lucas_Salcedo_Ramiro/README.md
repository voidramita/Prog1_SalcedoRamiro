# Gestión de Países en Python  
### Trabajo Práctico Integrador – Programación I
Autores: Lucas Godoy – Ramiro Salcedo  
Profesora: Cinthia Rigoni  
---
## Contenido del proyecto
### -> Informe_Teorico.pdf 
### -> README.md

## /Código/
### -> main.py
### -> funciones_opciones.py
### -> paises.csv
--- 

## Descripción del programa
Este proyecto implementa un sistema en Python para gestionar y analizar información de países almacenados en un archivo CSV.  
Permite realizar búsquedas, filtros, ordenamientos y estadísticas generales sobre población, superficie y continentes.

El programa fue desarrollado aplicando listas, diccionarios, funciones, modularización, estructuras condicionales, bucles y manejo de archivos, de acuerdo con los requerimientos del Trabajo Práctico Integrador de la asignatura.

## Funcionalidades principales
- Buscar un país por nombre.  
- Filtrar por continente.  
- Ordenar por nombre, población o superficie (ascendente y descendente).  
- Mostrar estadísticas generales:  
  - País con mayor población.  
  - País con menor población.  
  - Promedio de población.  
  - Promedio de superficie.  
  - Cantidad de países por continente.  

---

## Requisitos técnicos
- Python 3.x  
- Archivo paises.csv ubicado en el mismo directorio  
- Módulos estándar utilizados: csv, os  

---

## Estructura del programa
## /Código/
### -> main.py
### -> funciones_opciones.py
### -> paises.csv
--- 

## Ejemplos de uso

### Ejemplo 1 – Búsqueda

Ingresá el nombre del país a buscar: Argentina
País encontrado: {'nombre': 'Argentina', 'continente': 'América', 'poblacion': 45376763, 'superficie': 2780400}

### Ejemplo 2 – Filtrado por continente
Ingresá el continente para filtrar: Europa

Países en Europa:
España — Población: 47.450.795 — Superficie: 505.990 km²
Francia — Población: 65.312.000 — Superficie: 643.801 km²

### Ejemplo 3 – Ordenamiento
Ingresá el criterio de ordenamiento: poblacion
¿Querés orden descendente? (s/n): s

Países ordenados por población (descendente):
China: 1.412.600.000
India: 1.366.400.000
Estados Unidos: 331.900.000


## Participación de los integrantes
El trabajo fue realizado en conjunto por ambos integrantes. Todas las funciones del programa fueron desarrolladas, revisadas y probadas de manera colaborativa, compartiendo las decisiones técnicas durante todo el proyecto.