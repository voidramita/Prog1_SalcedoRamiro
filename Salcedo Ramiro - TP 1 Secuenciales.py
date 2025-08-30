print("Hola mundo!")

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

print("Ingrese sus datos personales")
nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
if (int(edad) <= 0):
    print("Ingrese una edad válida.")
    exit()
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")


print("Cálculo del área y perímetro de un círculo")
radio = input("Ingrese el radio del círculo: ")
if (float(radio) <= 0):
    print("Número inválido.")
    exit()
else:
     area = 3.14 * float(radio) ** 2
     perimetro = 2 * 3.14 * float(radio)
     print(f"El área del círculo es: {area}")
     print(f"El perímetro del círculo es: {perimetro}")

print("Conversión de segundos a horas")
segundos = input("Ingrese el tiempo en segundos: ")
if (float(segundos) <= 0):
    print("Número inválido.")
    exit()
else:
     horas = float(segundos) / 3600
     print(f"El tiempo en horas es: {horas}")

print("Tabla de multiplicar")
numero = input("Ingrese un número del 1 al 10: ")
if (int(numero) < 1 or int(numero) > 10):
    print("Número inválido.")
    exit()
else:
    print(numero, "x 1 =", int(numero) * 1)
    print(numero, "x 2 =", int(numero) * 2)
    print(numero, "x 3 =", int(numero) * 3)
    print(numero, "x 4 =", int(numero) * 4)
    print(numero, "x 5 =", int(numero) * 5)
    print(numero, "x 6 =", int(numero) * 6)
    print(numero, "x 7 =", int(numero) * 7)
    print(numero, "x 8 =", int(numero) * 8)
    print(numero, "x 9 =", int(numero) * 9)
    print(numero, "x 10 =", int(numero) * 10)

print("Ingrese 2 números , deben ser positivos.")
numero1 = int(input("Ingrese el primer número: "))
if numero1 <= 0:
    print("Número inválido.")
    # Valida que los números sean positivos
    exit()
else:
    numero2 = int(input("Ingrese el segundo número: "))
    if numero2 <= 0:
        print("Número inválido.")
        exit()
    else:
        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = numero1 / numero2
        print(f"La suma es: {suma}")
        print(f"La resta es: {resta}")
        print(f"La multiplicación es: {multiplicacion}")
        print(f"La división es: {division}")

print("Cálculo IMC")
peso = float(input("Ingrese su peso en kg: "))
if (peso <= 0):
    print("Número inválido.")
    exit()
altura = float(input("Ingrese su altura en metros: "))
if (altura <= 0):
    print("Número inválido.")
    exit()
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

print("Conversión de Celsius a Fahrenheit")
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

print("Promedio de tres números")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {promedio}")
