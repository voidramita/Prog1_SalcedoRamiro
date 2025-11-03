pi = 3.14159

## Ejercicio 1
def hola_mundo():
    print("Hola Mundo!")

hola_mundo()


## Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

## Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


## Ejercicio 4
def calcular_area_circulo(radio):
    return pi * (radio ** 2)


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio


radio = float(input("Ingrese el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

## Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600


segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas.")

## Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

## Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = a / b
    else:
        division = "Ingrese un divisor distinto de cero."

    return (suma, resta, multiplicacion, division)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

## Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

## Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Equivale a {fahrenheit:.2f} °F")

## Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


num_a = float(input("Ingrese el primer número: "))
num_b = float(input("Ingrese el segundo número: "))
num_c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num_a, num_b, num_c)
print(f"El promedio es: {promedio:.2f}")