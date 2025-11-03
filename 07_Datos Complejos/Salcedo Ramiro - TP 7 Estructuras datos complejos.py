## Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


## Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800



## Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


## Ejercicio 4
directorio_telefonico = {}

print("A continuación, ingrese 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del Contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    directorio_telefonico[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")

if nombre_consulta in directorio_telefonico:
    print(directorio_telefonico[nombre_consulta])
else:
    print("Contacto no encontrado.")


## Ejercicio 5
frase = input("Ingrese una frase: ")

palabras = frase.lower().replace(",", "").replace(".", "").split()

## a) Las palabras únicas (set)
palabras_unicas = set(palabras)
print(palabras_unicas)

## b) Un diccionario con la cantidad de veces que aparece cada palabra.
recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
print(recuento_palabras)


alumnos_notas = {}
numero_alumnos = 3

print(f"A continuación, ingrese los datos de {numero_alumnos} alumnos (Nombre y 3 notas).")

for i in range(numero_alumnos):
    nombre = input(f"Ingrese el nombre del Alumno {i+1}: ")
    
    nota1 = float(input("Ingrese Nota 1: "))
    nota2 = float(input("Ingrese Nota 2: "))
    nota3 = float(input("Ingrese Nota 3: "))
    
    notas = (nota1, nota2, nota3)
    alumnos_notas[nombre] = notas

for nombre, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


## Ejercicio 7
aprobados_parcial_1 = {"Juan", "Ana", "Pedro", "Sofía", "Martín"}
aprobados_parcial_2 = {"Ana", "Sofía", "Luis", "Elena", "Carlos", "Martín"}

## a) Mostrá los que aprobaron ambos parciales
ambos_parciales = aprobados_parcial_1.intersection(aprobados_parcial_2)
print(ambos_parciales)

## b) Mostrá los que aprobaron solo uno de los dos
solo_uno = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)
print(solo_uno)

## c) Mostrá la lista total de estudiantes que aprobaron al menos un parcial
al_menos_uno = aprobados_parcial_1.union(aprobados_parcial_2)
print(al_menos_uno)


## Ejercicio 8
inventario = {"leche": 15, "pan": 50, "huevo": 24}

accion = input("Acción (consultar/agregar): ").lower()
producto_ingresado = input("Ingrese nombre del producto: ").lower()

if accion == "consultar":
    if producto_ingresado in inventario:
        print(inventario[producto_ingresado])
    else:
        print("Producto no encontrado en inventario.")
elif accion == "agregar":
    unidades_ingresadas = int(input("Ingrese unidades a agregar: "))
    
    if producto_ingresado in inventario:
        ## b) Agregar unidades al stock si el producto ya existe
        inventario[producto_ingresado] += unidades_ingresadas
    else:
        ## c) Agregar un nuevo producto si no existe
        inventario[producto_ingresado] = unidades_ingresadas
    
    print(inventario)
else:
    print("Acción no válida. Ingrese 'consultar' o 'agregar'.")
## Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Entrenamiento",
    ("viernes", "18:00"): "Cena con amigos"
}

dia_consulta = input("Ingrese el día (ej: lunes): ").lower()
hora_consulta = input("Ingrese la hora (ej: 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

if clave_consulta in agenda:
    print(agenda[clave_consulta])
else:
    print("No hay evento agendado para ese día y hora.")


## Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima", "Brasil": "Brasilia"}
invertido = {}

## Construir el nuevo diccionario invirtiendo claves y valores
for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)