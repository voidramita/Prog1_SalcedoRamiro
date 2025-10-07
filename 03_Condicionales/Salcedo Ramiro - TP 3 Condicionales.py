## Validacion mayoria de edad

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
elif edad < 0 or edad > 110:
        print("Edad invalida.")
else:
    print("No es mayor de edad.")
    

## Validacion notas usuario

nota = int(input("Ingrese su nota: "))
if nota >= 0 and nota <= 10:
    if nota >= 6:
        print("Aprobado.")
    else:
        print("Desaprobado.")
else:
    print("Nota invalida.")


## Validacion numeros pares

num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("El numero es par.") 
else:
    print("Por favor ingrese un numero par.")


## Categorias por edad

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 12:
    print("Categoria: Niño/a.")
elif edad >= 13 and edad <= 17:
    print("Categoria: Adolescente.")
elif edad >= 18 and edad < 30:
    print("Categoria: Adulto/a joven.")
elif edad >= 30:
    print("Categoria: Adulto/a.")
else:
    print("Edad invalida.")


## Validacion longitud de contraseña

contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contrase.")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")


## Calcular moda, mediana y media. Sesgo negativo, positivo o sin sesgo

from statistics import mode, median, mean
import random

lista = []
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print("Media:", media_valor)
print("Mediana:", mediana_valor)
print("Moda:", moda_valor)

if media_valor > mediana_valor > moda_valor:
    print("Sesgo positivo o a la derecha.")
elif media_valor < mediana_valor < moda_valor:
    print("Sesgo negativo o a la izquierda.")
else:
    print("Distribución simétrica (sin sesgo).")

## Vocal con signo de exclamacion
palabra = input("Ingrese una palabra: ").strip()
if palabra[-1].lower() in "aeiou":
    texto = palabra + "!"
    print(texto)
else:
    print(palabra)

## Nombre mayusculas, minusculas y primera letra mayuscula

nombre = input("Ingrese su nombre: ")
menu = 0
while menu == 0:
    print("1. Mayusculas")
    print("2. Minusculas")
    print("3. Primera letra mayuscula")
    menu = int(input("Elija una opcion (1-3): "))
    if menu == 1:
        nombre = nombre.upper()
        print(nombre)
    elif menu == 2:
        nombre = nombre.lower()
        print(nombre)
    elif menu == 3:
        nombre = nombre.capitalize()
        print(nombre)
    else:
        print("Opcion invalida.")
        menu = 0

## Magnitud terremoto

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3.0:
    print("Terremoto muy leve.")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Terremoto leve.")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Terremoto moderado.")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Terremoto fuerte.")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Terremoto muy fuerte.")
elif magnitud >= 7.0:
    print("Terremoto extremo.")
else:
    print("Magnitud invalida.")

## Estacion segun hemisferio y mes
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = input("Ingrese el mes (1-12): ").strip()
dia = int(input("Ingrese el dia del mes (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"

elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"

elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"

else:
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print("La estación del año es:", estacion)