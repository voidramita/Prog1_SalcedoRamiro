## Numeros del 0 al 100, línea por línea
for i in range(101):
    print(i)

## Ingreso de numero entero y determinar cuantos digitos tiene
num = int(input("Ingrese un numero entero: "))
if num < 0:
    print("Por favor, ingrese un numero entero positivo.")
else:
    if num == 0:
        print("El numero tiene 1 digito.")
    else:
        digitos = 0
        while num > 0:
            num //= 10
            digitos += 1
        print(f"El numero tiene {digitos} digitos.")

##  Ingrese numeros, suma, excluyendo numeros ingresados
valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))
suma = 0
for i in range(valor1 + 1, valor2):
    suma += i
print(f"La suma de los numeros entre {valor1} y {valor2} es: {suma}")

## Ingrese numeros, suma consecutiva hasta que se ingrese un cero
suma_consecutiva = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    if numero == 0:
        break
    suma_consecutiva += numero
print(f"La suma de los numeros ingresados es: {suma_consecutiva}")

## Adivinar numero entre 1 y 9, mostrando intentos hasta acertar
import random
numero_secreto = random.randint(1, 9)
intentos = 0
while True:
    intento = int(input("Adivine el numero entre 1 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"Felicidades! Adivinaste el numero en {intentos} intentos.")
        break
    else:
        print("Numero incorrecto, intente de nuevo.")

## Impresión numeros pares entre 1 y 100, orden decresciente
for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

## Suma de numeros entre 0 y un numero positivo ingresado
num_positivo = int(input("Ingrese un numero entero positivo: "))
if num_positivo < 0:
    print("Por favor, ingrese un numero entero positivo.")
else:
    suma_total = sum(range(num_positivo + 1))
    print(f"La suma de todos los numeros entre 0 y {num_positivo} es: {suma_total}")

## Conteo de pares, impares, positivos y negativos en 100 numeros
positivos = 0
negativos = 0
pares = 0
impares = 0
for _ in range(100):
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")

## Ingreso 100 enteros, calcular media entre esos valores
suma_enteros = 0
for _ in range(100):
    numero = int(input("Ingrese un numero entero: "))
    suma_enteros += numero
media = suma_enteros / 100
print(f"La media de los 100 numeros ingresados es: {media}")

## Invertir un numero entero ingresado por el usuario
numero = int(input("Ingrese un numero entero: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print(f"El numero invertido es: {numero_invertido}")

