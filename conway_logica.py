from random import randint
from copy import deepcopy as dc
import pickle as pk

def generarMatrizAleatoria(filas, columnas):
    """
    Retorna una matriz con valores enteros aleatorios de 0 o 1.
    Entradas: filas (int), columnas (int).
    Salidas: matriz de dimensiones filas x columnas con valores 0 o 1.
    Restricciones: filas y columnas deben ser enteros positivos.
    """
    return [[randint(0,1) for c in range(columnas)] for f in range(filas)]

def generarMatrizVacia(filas, columnas):
    """
    Retorna una matriz con todos los valores en cero.
    Entradas: filas (int), columnas (int).
    Salidas: matriz de dimensiones filas x columnas con todos los valores en 0.
    Restricciones: filas y columnas deben ser enteros positivos.
    """
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
    """
    Retorna una lista con los estados de los 8 vecinos de la célula en la posición f, c usando vecindario de Moore con wrap-around.
    Entradas: M (matriz), f (int) fila de la célula, c (int) columna de la célula.
    Salidas: lista de 8 enteros con los estados de los vecinos.
    Restricciones: M debe ser una matriz rectangular no vacía. f y c deben ser índices válidos.
    """
    filas = len(M)
    cols = len(M[0])
    e = [M[(f-1)%filas][(c-1)%cols], M[(f-1)%filas][c%cols],M[(f-1)%filas][(c+1)%cols],
         M[(f)%filas][(c-1)%cols],M[(f)%filas][(c+1)%cols],
         M[(f+1)%filas][(c-1)%cols], M[(f+1)%filas][c%cols],M[(f+1)%filas][(c+1)%cols]]
    return e

def transicion_celula(estado, vecinos, nacimiento, sobrevive):
    """
    Retorna el nuevo estado de una célula según las reglas Life-Like (Bx/Sy).
    Entradas: estado (int) 0 o 1, vecinos (list) estados de los 8 vecinos, nacimiento (tuple) dígitos B, sobrevive (tuple) dígitos S.
    Salidas: nuevo estado de la célula (0 o 1).
    Restricciones: estado debe ser 0 o 1. nacimiento y sobrevive deben contener enteros entre 0 y 8.
    """
    v = vecinos.count(1)
    if estado == 0 and v in nacimiento:
        return 1
    elif estado == 1 and v in sobrevive:
        return 1
    else:
        return 0

def transicion(M, nacimiento, sobrevive):
    """
    Aplica la función de transición a todas las células de la matriz y retorna la nueva matriz.
    Entradas: M (matriz), nacimiento (tuple) dígitos B, sobrevive (tuple) dígitos S.
    Salidas: nueva matriz con el estado siguiente del autómata.
    Restricciones: M debe ser una matriz rectangular no vacía con valores 0 o 1.
    """
    MN = dc(M)
    for filas in range(len(M)):
        for columnas in range(len(M[0])):
            MN[filas][columnas] = transicion_celula(M[filas][columnas], obtener_vecinos(M, filas, columnas), nacimiento, sobrevive)
    return MN

def guardarEstado(M, filas, columnas, tamaño, nacimiento, sobrevive):
    """
    Guarda el estado completo del autómata en un archivo pickle.
    Entradas: M (matriz), filas (int), columnas (int), tamaño (int), nacimiento (tuple), sobrevive (tuple).
    Salidas: archivo estadoConway.pkl en disco.
    Restricciones: requiere permisos de escritura en el directorio actual.
    """
    parametros = (M, filas, columnas, tamaño, nacimiento, sobrevive)
    with open("estadoConway.pkl", "wb") as archivo:
        pk.dump(parametros, archivo)