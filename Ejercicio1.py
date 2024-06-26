#Se usa el input de csacademy.com

import json
from collections import defaultdict

# Función para calcular el índice h
def calcularIndiceH(citas):
    citas.sort(reverse=True)
    h = 0
    for i, conteo in enumerate(citas, 1):
        if conteo >= i:
            h = i
        else:
            break
    return h

# Leer todos los datos de la entrada estándar
import sys
entrada = sys.stdin.read().strip()

# Dividir los datos en líneas
lineas = entrada.split('\n')

# La primera línea contiene el número de entradas (N)
n = int(lineas[0].strip())

# Validar que n esté en el rango entre 2 y 10000
if not (2 <= n <= 10000):
    raise ValueError("El número de entradas (N) debe estar entre 2 y 10000.")

# Las siguientes n líneas contienen los datos JSON
datosJson = [lineas[i].strip() for i in range(1, n + 1)]

# Parsear los datos JSON
articulos = [json.loads(dato) for dato in datosJson]

# Diccionario para almacenar autores y sus conteos de citas
autorArticulos = defaultdict(list)

# Llenar el diccionario autorArticulos con los datos de los artículos
for articulo in articulos:
    conteoCitas = articulo["citing_paper_count"]
    autores = articulo["authors"]["authors"]
    for autor in autores:
        nombreCompleto = autor["full_name"]
        autorArticulos[nombreCompleto].append(conteoCitas)

# Calcular el índice h para cada autor
autorIndiceH = {autor: calcularIndiceH(citas) for autor, citas in autorArticulos.items()}

# Ordenar los autores por índice h de manera descendente y alfabéticamente
autoresOrdenados = sorted(autorIndiceH.items(), key=lambda x: (-x[1], x[0]))

# Imprimir la lista ordenada de autores con el índice h
for autor, indiceH in autoresOrdenados:
    print(f"{autor} {indiceH}")
