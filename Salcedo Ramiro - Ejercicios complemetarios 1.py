numero1 = 2
numero2 = 2.5
print("numero 1:", numero1)
print("numero 2:", numero2)

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
div = numero1 / numero2
print("suma:", suma)
print("resta:", resta)
print("multiplicacion:", multi)
print("division:", div)
# Operaciones e impresión en pantalla

nombre0 = "ramiro"
precio = 9.99
descuento = 0.20
precio_final = precio - (precio * descuento)
print(f"Precio con descuento: {precio_final}")
# Impresion de precio con descuento

cadena = "buendia"
longitud = len(cadena)
precio = int(9.99)
print(f"Precio en entero: {precio}")

nombre1 = "Ramiro"
apellido1 = "Salcedo"
nombre_completo1 = f'{nombre1}, {apellido1}'
print(nombre_completo1)
# Impresion del nombre completo en una sola variable

edad = 21 + 5 - 10
altura = 1.75 * 4 / 3
print(f"Edad: {edad}, Altura: {altura}")

mayusnombre = "RAMIRO"
mayusapellido = "SALCEDO"
minusnombre = mayusnombre.lower()
minusapellido = mayusapellido.lower()
# Declaracion variables en minuscula

print(f"Nombre en mayuscula: {mayusnombre}, {mayusapellido}")
print(f"Nombre en minuscula: {minusnombre}, {minusapellido}")
primera_en_mayusN = minusnombre.capitalize()
primera_en_mayusA = minusapellido.capitalize()
# Metodo para capitalizar la primera letra

print(f"Nombre con primera letra en mayuscula: {primera_en_mayusN}, {primera_en_mayusA}")
