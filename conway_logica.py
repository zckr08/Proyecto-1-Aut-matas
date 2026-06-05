from random import randint

def generar_matriz(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
    vecinos = []
    for filasV in range(f-1, f+2):          
        for colsV in range(c-1, c+2):       
            if not (filasV == f and colsV == c):  
                i = filasV % len(M)
                j = colsV % len(M[0])
                vecinos.append(M[i][j])
    return vecinos 

def transicion_celula(estado, vecinos):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos --> viva
    Si estado == 1 y tiene menos de 2 vecinos vivos --> muere
    Si estado == 1 y tiene más de 3 vecinos vivos --> muere
    Cualquier otra combinación, el estado sigue igual."""
    vivos = sum(vecinos)                     
    if estado == 0 and vivos == 3:           
        return 1
    elif estado == 1 and vivos < 2:          
        return 0
    elif estado == 1 and vivos > 3:          
        return 0
    else:                                    
        return estado                   
   
def transicion(M):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    nueva_M = []                             
    for f in range(len(M)):                  
        nueva_fila = []
        for c in range(len(M[0])):
            v = obtener_vecinos(M, f, c)
            nuevo_estado = transicion_celula(M[f][c], v)  
            nueva_fila.append(nuevo_estado)
        nueva_M.append(nueva_fila)
    return nueva_M                      
