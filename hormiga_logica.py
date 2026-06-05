import colorsys as csys

def generarColores(instrucciones):
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
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[0 for c in range(columnas)] for f in range(filas)]    

def girarHormiga(M, f, c, direccion, instrucciones):
    caso0 = {"U": "R", "R": "D", "D": "L", "L": "U"}
    caso1 = {"U": "L", "L": "D", "D": "R", "R": "U"}
    direccionGiro = instrucciones[M[f][c]]
    if  direccionGiro == "R":     
        return caso0[direccion]
    else:
        return caso1[direccion]

def nuevaPosicion(filaHormiga, columnaHormiga, direccion, filas, columnas):
    if direccion == "R":
        return filaHormiga, ((columnaHormiga+1)%columnas)
    if direccion == "L":
        return filaHormiga, ((columnaHormiga-1)%columnas)
    if direccion == "U":
        return ((filaHormiga-1)%filas), columnaHormiga
    if direccion == "D":
        return ((filaHormiga+1)%filas), columnaHormiga

def avanzarHormiga(M, filaHormiga, columnaHormiga, colores):
    M[filaHormiga][columnaHormiga] = (M[filaHormiga][columnaHormiga]+1)%colores
    return M

def siguiente(M, filaHormiga, columnaHormiga, direccion, filas, columnas, colores, instrucciones):
    direccion = girarHormiga(M, filaHormiga, columnaHormiga,direccion, instrucciones)
    M = avanzarHormiga(M, filaHormiga, columnaHormiga, colores)
    filaHormiga, columnaHormiga = nuevaPosicion(filaHormiga, columnaHormiga, direccion, filas, columnas)
    return M, filaHormiga, columnaHormiga, direccion
        