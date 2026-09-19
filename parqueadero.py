# Sistema de Control de Acceso a un Parqueadero Universitario
# USC - Primer Examen Parcial Lenguajes de Programacion
# No se usan listas, diccionarios, funciones ni POO.

CAPACIDAD = 30

# Cantidad de vehiculos que se intentaron registrar
N = int(input("Ingrese la cantidad de vehiculos a registrar: "))

# Acumuladores de estadisticas
total_validos = 0
total_recaudado = 0.0
total_horas_validas = 0.0

cantidad_estudiantes = 0
cantidad_docentes = 0
cantidad_visitantes = 0

contador = 0

while contador < N and total_validos < CAPACIDAD:
    contador = contador + 1

    print("\n----------------------------------------")
    print("Registro de vehiculo", contador)
    print("----------------------------------------")

    placa = input("Ingrese la placa: ")
    tipo = input("Tipo de usuario (E=Estudiante, D=Docente, V=Visitante): ").upper()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas = float(input("Horas de permanencia: "))

    if horas <= 0:
        print("ERROR: las horas de permanencia deben ser mayores que cero.")
        print("El registro fue rechazado.")
        continue

    if hora_entrada < 0 or hora_entrada > 23:
        print("ERROR: la hora de entrada debe estar entre 0 y 23.")
        print("El vehiculo no se cuenta en las estadisticas.")
        continue

    tipo_original = tipo
    if tipo != "E" and tipo != "D" and tipo != "V":
        print("ADVERTENCIA: tipo de usuario no reconocido.")
        print("Se tratara como VISITANTE por defecto.")
        tipo = "V"

    if tipo == "E":
        cantidad_estudiantes = cantidad_estudiantes + 1

        if horas <= 2:
            tarifa = 0.0
        else:
            tarifa = (horas - 2) * 800.0

    elif tipo == "D":
        cantidad_docentes = cantidad_docentes + 1
        tarifa = horas * 500.0

    else:
        cantidad_visitantes = cantidad_visitantes + 1

        if horas <= 1:
            tarifa = horas * 1500.0
        else:
            tarifa = 1500.0 + (horas - 1) * 1200.0

    total_validos = total_validos + 1
    total_recaudado = total_recaudado + tarifa
    total_horas_validas = total_horas_validas + horas

    print("\nRegistro aceptado.")
    print("Placa:", placa)
    print("Tipo:", tipo)
    print("Horas:", horas)
    if tipo_original != tipo:
        print("Tipo ingresado:", tipo_original, "(convertido a Visitante)")
    print("Tarifa:", round(tarifa, 2), "COP")
