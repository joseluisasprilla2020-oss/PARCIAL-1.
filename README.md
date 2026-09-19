# Sistema de Control de Acceso a un Parqueadero Universitario

## Descripcion

Este proyecto simula el registro de vehiculos en un parqueadero universitario
con capacidad maxima de 30 cupos.

El sistema recibe la placa, tipo de usuario, hora de entrada y horas de permanencia.
Permite registrar estudiantes, docentes y visitantes, calcular sus tarifas,
aplicar el descuento nocturno y mostrar estadisticas finales.

## Reglas implementadas

- Capacidad maxima: 30 vehiculos validos.
- Estudiante: primeras 2 horas gratis; despues $800 COP por hora adicional.
- Docente: $500 COP por hora.
- Visitante: primera hora a $1500 COP y cada hora adicional a $1200 COP.
- Descuento nocturno del 10% si la entrada es despues de las 19:00 o antes de las 6:00.
- Hora de entrada valida: de 0 a 23.
- Horas de permanencia: deben ser mayores que cero.
- Un tipo diferente de E, D o V se trata como visitante y genera una advertencia.
- El cobro se redondea a 2 decimales.

## Restricciones del parcial

El programa se desarrolla sin listas, diccionarios, funciones definidas por el usuario ni POO.
Se utilizan variables, tipos de datos, operadores, decisiones y repeticion.

## Ejecucion

Ejecutar:

```bash
python parqueadero.py
```

## Autor

Nombre del estudiante: ______________________________
