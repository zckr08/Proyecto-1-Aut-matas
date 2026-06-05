def generar_matriz(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[0 for c in range(columnas)] for f in range(filas)]    

def nuevaDirección(M, f, c, direccion):
    caso0 = {"U": "R", "R": "D", "D": "L", "L": "U"}
    caso1 = {"U": "L", "L": "D", "D": "R", "R": "U"}
    if  M[f][c] == 0:     
        return caso0[direccion]
    else:
        return caso1[direccion]

def nuevaPosicion(filaHormiga, columnaHormiga, direccion):
    if direccion == "R":
        return filaHormiga, columnaHormiga+1
    if direccion == "L":
        return filaHormiga, columnaHormiga-1
    if direccion == "U":
        return filaHormiga-1, columnaHormiga
    if direccion == "D":
        return filaHormiga+1, columnaHormiga

def transicion(M, filaHormiga, columnaHormiga):
    if M[filaHormiga][columnaHormiga] == 0:
        M[filaHormiga][columnaHormiga] = 1
    elif M[filaHormiga][columnaHormiga] == 1:
        M[filaHormiga][columnaHormiga] = 0
    return M

def avanzar(M, filaHormiga, columnaHormiga, direccion):
    direccion = nuevaDirección(M, filaHormiga, columnaHormiga, direccion)
    M = transicion(M, filaHormiga, columnaHormiga)
    filaHormiga, columnaHormiga = nuevaPosicion(filaHormiga, columnaHormiga, direccion)
    return M, filaHormiga, columnaHormiga, direccion
        