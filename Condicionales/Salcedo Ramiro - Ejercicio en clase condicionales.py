# Alumnos: Godoy Lucas, Salcedo Ramiro

Entrada = input("-Ingrese una fecha en formato \"Dia, DD/MM\": ")

partes = Entrada.split(",")
dia_texto = partes[0].strip()
fecha = partes[1].strip()

string_dd, string_mm = fecha.split("/")
dd = int(string_dd)
mm = int(string_mm)

dia_texto = dia_texto.lower()   # convierte a minúsculas

if (dia_texto == "lunes" or dia_texto == "martes" or dia_texto == "miercoles" or dia_texto == "jueves" or dia_texto == "viernes"):  # verifica si es un día válido
    dia = dia_texto
else: print("error")

if(dd >= 1 and dd <= 31 and mm >= 1 and mm <= 12):  # verifica si la fecha es válida
    fecha = (dd, mm)
else: print("error")

if (dia == "lunes" or dia == "martes" or dia == "miercoles"):   # verifica si es un día de examen
    examen = input("-Ingrese si hubo examen: ")
    examen = examen.lower()
    if (examen == "si"):
        cantidad_de_aprobados = int(input("Ingrese cantidad de aprobados: "))
        cantidad_de_desaprobados = int(input("Ingrese cantidad de desaprobados: "))
        promedio = cantidad_de_aprobados / (cantidad_de_aprobados + cantidad_de_desaprobados) * 100    # calcula el promedio
        print(f"Promedio de aprobados: {promedio}%")
    elif (examen == "no"):
        print("No hubo examen")
    else:
        print("Respuesta no válida")

if (dia == "jueves"):
    asistencia = int(input("-Ingrese cantidad de alumnos presentes: "))
    total_alumnos = int(input("-Ingrese cantidad total de alumnos: "))
    if(asistencia >= 0 and asistencia <= total_alumnos):

        if (asistencia > total_alumnos / 2):    # verifica si asistió la mayoría
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    else:
        print("Datos de asistencia no válidos")

if (dia == "viernes"):
    if (dd == 1 and mm == 1 or mm == 7):    # verifica si es el comienzo de un nuevo ciclo
        print("Comienzo de nuevo ciclo")
        cant_alumnos = int(input("Ingrese cantidad de alumnos: "))
        if (cant_alumnos > 0):
            pass
        else:
            print("Cantidad de alumnos no válida.")
        arancel_alumnos = float(input("Ingrese el arancel por alumno: "))
        if (arancel_alumnos > 0):
            total_arancel = cant_alumnos * arancel_alumnos
            if(total_arancel.is_integer()):     # verifica si el total es un número entero
                total_arancel = print(int(total_arancel))   # convierte a entero
            else:
                print(f"Ingreso total: {total_arancel}")
        else:
            print("Monto no válido.")
else:
    print("Inglés para viajeros")