from random import randint
from copy import deepcopy as dc
import pickle as pk

def generarMatrizAleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0,1) for c in range(columnas)] for f in range(filas)]

def generarMatrizVacia(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[0 for c in range(columnas)] for f in range(filas)]       

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
    filas = len(M)
    cols = len(M[0])
    e = [M[(f-1)%filas][(c-1)%cols], M[(f-1)%filas][c%cols],M[(f-1)%filas][(c+1)%cols],
         M[(f)%filas][(c-1)%cols],M[(f)%filas][(c+1)%cols],
         M[(f+1)%filas][(c-1)%cols], M[(f+1)%filas][c%cols],M[(f+1)%filas][(c+1)%cols]]
    return e

def transicion_celula(estado, vecinos, nacimiento, sobrevive):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos --> viva
    Si estado == 1 y tiene menos de 2 vecinos vivos --> muere
    Si estado == 1 y tiene más de 3 vecinos vivos --> muere
    Cualquier otra combinación, el estado sigue igual."""
    v = vecinos.count(1)
    if estado == 0 and v in nacimiento:
        return 1
    elif estado == 1 and v in sobrevive:
        return 1
    else:
        return 0


def transicion(M, nacimiento, sobrevive):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    MN = dc(M)
    for filas in range(len(M)):
        for columnas in range(len(M[0])):
            MN[filas][columnas] = transicion_celula(M[filas][columnas], obtener_vecinos(M, filas, columnas), nacimiento, sobrevive)
    return MN


def guardarEstado(M, filas, columnas, tamaño, nacimiento, sobrevive):
    parametros = (M, filas, columnas, tamaño, nacimiento, sobrevive)
    with open("estadoConway.pkl", "wb") as archivo:
        pk.dump(parametros, archivo)