## Ejercicio 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

## Ejercicio 2
mis_elementos = ["computadora", "teclado", "raton", "monitor", "webcam"]
penultimo_elemento = mis_elementos[-2]
print(f"El penultimo elemento es: {penultimo_elemento}")

## Ejercicio 3
lista_vacia = []
lista_vacia.append("alto")
lista_vacia.append("medio")
lista_vacia.append("bajo")
print(f"Lista: {lista_vacia}")

## Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(f"Lista modificada: {animales}")

## Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(f"Resultado: {numeros}")


## Ejercicio 6
numeros_con_salto = list(range(10, 31, 5))
dos_primeros = numeros_con_salto[0:2]
print(f"Los dos primeros numeros son: {dos_primeros}")

## Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ferrari"
autos[2] = "tesla"
# Imprimir la lista para verificar la modificación
print(f"Lista modificada: {autos}")

## Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(f"Dobles: {dobles}")

## Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
 ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(f"Lista final: {compras}")

## Ejercicio 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(f"Lista: {lista_anidada}")