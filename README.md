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

## Explicacion paso a paso

### 1. Variables iniciales

`CAPACIDAD` representa los 30 cupos disponibles. `N` guarda la cantidad de
vehiculos que se intentaran registrar. Como `input()` recibe texto, se usa
`int()` para convertir la respuesta en un numero entero.

Los acumuladores comienzan en cero: `total_validos` cuenta los registros
aceptados, `total_recaudado` suma los cobros y `total_horas_validas` suma las
horas de permanencia. Tambien se inicializan los contadores por tipo de
usuario y `contador`, que controla los intentos procesados.

### 2. Acumuladores

Un acumulador conserva un total mientras se repite el ciclo. Por ejemplo,
`total_validos = total_validos + 1` aumenta en uno cada vez que un vehiculo
cumple las validaciones y es aceptado.

### 3. Ciclo `while`

El ciclo usa `while contador < N and total_validos < CAPACIDAD`. Esto significa
que procesa como maximo los registros solicitados y se detiene cuando el
parqueadero llega a 30 vehiculos validos.

### 4. Uso de `contador`

`contador = contador + 1` se ejecuta al comenzar cada intento. Asi se sabe
cuantos vehiculos se han procesado y se evita superar el valor de `N`.

### 5. Lectura de datos

El programa solicita placa, tipo de usuario, hora de entrada y horas de
permanencia. La placa es texto, el tipo se convierte a mayusculas con
`.upper()`, la hora usa `int()` y la permanencia usa `float()` para permitir
valores decimales como `2.5`.

### 6. Validacion de horas

Si `horas <= 0`, el registro se rechaza. La instruccion `continue` ignora el
resto de la iteracion actual y vuelve al comienzo del ciclo para procesar el
siguiente vehiculo. Por eso el registro invalido no entra en las estadisticas.

### 7. Validacion de la hora

La hora debe estar entre 0 y 23. La condicion
`hora_entrada < 0 or hora_entrada > 23` detecta valores fuera de ese rango y
rechaza el registro.

### 8. Validacion del tipo

Los tipos validos son `E`, `D` y `V`. Si se escribe otro valor, el programa
muestra una advertencia y lo trata como visitante (`V`) por defecto.

### 9. Tarifa del estudiante

Las primeras dos horas de un estudiante son gratuitas. Si permanece mas de
dos horas, se cobra el excedente a 800 COP por hora:

```text
tarifa = (horas - 2) * 800
```

### 10. Tarifa del docente

Al docente se le cobra 500 COP por cada hora:

```text
tarifa = horas * 500
```

### 11. Tarifa del visitante

La primera hora cuesta 1500 COP y cada hora adicional cuesta 1200 COP. Para
tres horas, por ejemplo, el total es `1500 + (3 - 1) * 1200 = 3900` COP.

### 12. Descuento nocturno

La condicion `hora_entrada > 19 or hora_entrada < 6` identifica entradas
despues de las 19:00 o antes de las 6:00. Por tanto, las horas 20 y 5 tienen
descuento, mientras que 19 y 6 no lo tienen.

### 13. Calculo del descuento

Cuando la entrada es nocturna, el descuento equivale al 10 por ciento de la
tarifa:

```text
descuento = tarifa * 0.10
total_pagar = tarifa - descuento
```

### 14. Uso de `round()`

`round(total_pagar, 2)` redondea el cobro final a dos decimales. Esto evita
mostrar cantidades monetarias con demasiadas cifras decimales.

### 15. Estadisticas de registros validos

Despues de calcular el cobro, el programa incrementa `total_validos`, suma el
valor a `total_recaudado` y agrega las horas a `total_horas_validas`. Solo los
registros aceptados modifican estos acumuladores.

### 16. Promedio de horas

Al finalizar, el promedio se obtiene dividiendo las horas validas entre los
vehiculos validos:

```text
promedio_horas = total_horas_validas / total_validos
```

Si no hubo registros validos, el promedio se establece en `0.0` para evitar
una division entre cero.

### 17. Porcentaje de ocupacion

La ocupacion se calcula comparando los vehiculos validos con la capacidad:

```text
porcentaje_ocupacion = (total_validos / CAPACIDAD) * 100
```

Si entraron 15 vehiculos validos, la ocupacion es `15 / 30 * 100 = 50%`.
