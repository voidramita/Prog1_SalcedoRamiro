## Factorial de un número usando recursividad
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")

## Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese una posición: "))

print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()

## Potencia de un numero usando recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))

print(f"{b}^{e} = {potencia(b, e)}")

## Pasaje a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
print("Binario:", decimal_a_binario(num))

## Verificar si una palabra es palíndromo usando recursividad
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
print(es_palindromo(texto))


## Suma de dígitos recursiva (sin strings)
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número: "))
print("Suma de dígitos:", suma_digitos(num))

## Ejercicio bloques piramide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques:", contar_bloques(nivel))

## Contador digitos en un número recursivo
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resta = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resta, digito)
    return contar_digito(resta, digito)

num = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito a buscar: "))

print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")

