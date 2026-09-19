# Sistema de Control de Acceso a un Parqueadero Universitario
# USC - Primer Examen Parcial Lenguajes de Programacion
# No se usan listas, diccionarios, funciones ni POO.

CAPACIDAD = 30

# Cantidad de vehiculos que se intentaron registrar
N = int(input("Ingrese la cantidad de vehiculos a registrar: "))

contador = 0

while contador < N:
    contador = contador + 1

    print("\n----------------------------------------")
    print("Registro de vehiculo", contador)
    print("----------------------------------------")

    placa = input("Ingrese la placa: ")
    tipo = input("Tipo de usuario (E=Estudiante, D=Docente, V=Visitante): ").upper()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas = float(input("Horas de permanencia: "))
    print("\nDatos recibidos.")
    print("Placa:", placa)
    print("Tipo:", tipo)
    print("Hora de entrada:", hora_entrada)
    print("Horas:", horas)
