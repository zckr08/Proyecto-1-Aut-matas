import colorsys as csys

def generarColores(instrucciones):
    """
    Genera una lista de colores RGB distribuidos uniformemente según la cantidad de instrucciones.
    Entradas: instrucciones (int) cantidad de colores a generar.
    Salidas: lista de tuplas (r, g, b) con valores entre 0 y 255.
    Restricciones: instrucciones debe ser un entero positivo.
    """
    colores = []
    for color in range(instrucciones):
        h = color/instrucciones
        r,g,b = csys.hls_to_rgb(h, 0.85, 1.0)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        colores.append((r,g,b))
    return colores

def generar_matriz(filas, columnas):
    """
    Retorna una matriz con todos los valores en cero, representando celdas en estado inicial.
    Entradas: filas (int), columnas (int).
    Salidas: matriz de dimensiones filas x columnas con todos los valores en 0.
    Restricciones: filas y columnas deben ser enteros positivos.
    """
    return [[0 for c in range(columnas)] for f in range(filas)]

def girarHormiga(M, f, c, direccion, instrucciones):
    """
    Retorna la nueva dirección de la hormiga según el color de la celda actual y las instrucciones.
    Entradas: M (matriz), f (int) fila actual, c (int) columna actual, direccion (str) dirección actual, instrucciones (str) secuencia de L y R.
    Salidas: nueva dirección de la hormiga (str): "U", "D", "L" o "R".
    Restricciones: direccion debe ser "U", "D", "L" o "R". instrucciones debe contener solo "L" y "R".
    """
    caso0 = {"U": "R", "R": "D", "D": "L", "L": "U"}
    caso1 = {"U": "L", "L": "D", "D": "R", "R": "U"}
    direccionGiro = instrucciones[M[f][c]]
    if direccionGiro == "R":
        return caso0[direccion]
    else:
        return caso1[direccion]

def nuevaPosicion(filaHormiga, columnaHormiga, direccion, filas, columnas):
    """
    Calcula la nueva posición de la hormiga según su dirección con wrap-around.
    Entradas: filaHormiga (int), columnaHormiga (int), direccion (str), filas (int), columnas (int).
    Salidas: tupla (filaHormiga, columnaHormiga) con la nueva posición.
    Restricciones: direccion debe ser "U", "D", "L" o "R". filas y columnas deben ser positivos.
    """
    if direccion == "R":
        return filaHormiga, ((columnaHormiga+1)%columnas)
    if direccion == "L":
        return filaHormiga, ((columnaHormiga-1)%columnas)
    if direccion == "U":
        return ((filaHormiga-1)%filas), columnaHormiga
    if direccion == "D":
        return ((filaHormiga+1)%filas), columnaHormiga

def avanzarHormiga(M, filaHormiga, columnaHormiga, colores):
    """
    Cambia el color de la celda actual al siguiente color de forma cíclica.
    Entradas: M (matriz), filaHormiga (int), columnaHormiga (int), colores (int) cantidad total de colores.
    Salidas: matriz M actualizada con el nuevo color en la celda actual.
    Restricciones: filaHormiga y columnaHormiga deben ser índices válidos dentro de M.
    """
    M[filaHormiga][columnaHormiga] = (M[filaHormiga][columnaHormiga]+1)%colores
    return M

def siguiente(M, filaHormiga, columnaHormiga, direccion, filas, columnas, colores, instrucciones):
    """
    Ejecuta un paso completo de la hormiga: gira, cambia el color de la celda y avanza.
    Entradas: M (matriz), filaHormiga (int), columnaHormiga (int), direccion (str), filas (int), columnas (int), colores (int), instrucciones (str).
    Salidas: tupla (M, filaHormiga, columnaHormiga, direccion) con el estado actualizado.
    Restricciones: direccion debe ser "U", "D", "L" o "R". instrucciones debe contener solo "L" y "R".
    """
    direccion = girarHormiga(M, filaHormiga, columnaHormiga, direccion, instrucciones)
    M = avanzarHormiga(M, filaHormiga, columnaHormiga, colores)
    filaHormiga, columnaHormiga = nuevaPosicion(filaHormiga, columnaHormiga, direccion, filas, columnas)
    return M, filaHormiga, columnaHormiga, direccion