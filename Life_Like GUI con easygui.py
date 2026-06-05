from easygui import *
import pygame
import pickle as pk
import conway_logica as con

def pedirEnteroPositivo(mensaje):
    """
    Le pide al usuario un número entero positivo que se utilizara para las filas, columnas y tamaño de celdas.
    Entradas: mensaje.
    Salidas: número entero positivo.
    Restricciones: Debe ser mayor que cero.
    """
    while True:
        valor = enterbox(mensaje,"Life-Like")
        if valor is None:
            raise SystemExit
        try:
            valor = int(valor)
            if valor <= 0:
                msgbox("El número debe ser mayor que cero.","Error")
                continue
            return valor
        except Exception:
            msgbox("Debe ingresar un número entero válido.","Error")

def pedirRegla():
    """
    Le pide al usuario una regla Life-Like.
    Entradas: Ninguna.
    Salidas: nacimiento, sobrevive.
    Restricciones: Formato Bx/Sy.
    """
    while True:
        regla = enterbox("Digita la regla Life-Like\nEjemplo: B3/S23","Life-Like")
        if regla is None:
            raise SystemExit
        regla = regla.upper().replace(" ","")
        try:
            if "B" not in regla:
                raise Exception
            if "S" not in regla:
                raise Exception
            if "/" not in regla:
                raise Exception
            texto = list(regla)
            texto.remove("B")
            texto.remove("S")
            separacion = texto.index("/")
            nacimiento = tuple(int(x) for x in texto[:separacion])
            sobrevive = tuple(int(x) for x in texto[separacion + 1:])
            for n in nacimiento:
                if n < 0 or n > 8:
                    raise Exception
            for s in sobrevive:
                if s < 0 or s > 8:
                    raise Exception
            return nacimiento,sobrevive
        except Exception:
            msgbox("Formato inválido.\nEjemplo correcto: B3/S23","Error")

def guardarEstado(M,filas,columnas,tam,nacimiento,sobrevive):
    """
    Guarda el estado actual del autómata en un archivo, se activa con la tecla "G"
    Entradas: parámetros del autómata.
    Salidas: archivo pickle.
    Restricciones: nombre válido.
    """
    while True:
        nombre = enterbox("Digita un nombre para guardar tu archivo:","Guardar")
        if nombre is None:
            return
        nombre = nombre.strip()
        if nombre == "":
            msgbox("Debes ingresar un nombre.","Error")
            continue
        try:
            with open(nombre + ".pkl","wb") as archivo:
                pk.dump((M,filas,columnas,tam,nacimiento,sobrevive),archivo)
            msgbox("Simulación guardada correctamente. :)","Life-Like")
            return
        except Exception:
            msgbox("No fue posible guardar el archivo.","Error")

def cargarEstado():
    """
    Carga un estado previamente guardado, se activa con la tecla "C"
    Entradas: ninguna.
    Salidas: parámetros del autómata.
    Restricciones: archivo pickle válido.
    """
    ruta = fileopenbox("Selecciona la simulación que quieres cargar","Cargar estado","*.pkl")
    if ruta is None:
        return None
    try:
        with open(ruta,"rb") as archivo:
            return pk.load(archivo)
    except Exception:
        msgbox("El archivo seleccionado no es válido.","Error")
        return None

def main():

    msgbox("¡Bienvenido a Life-Like!\n \n Hecho por Zack Rojas y Jose Oviedo","Life-Like")
    filas = pedirEnteroPositivo("Digita la cantidad de filas")
    columnas = pedirEnteroPositivo("Digita la cantidad de columnas")
    tam = pedirEnteroPositivo("Digita el tamaño de las celdas")
    nacimiento,sobrevive = pedirRegla()
    pygame.init()
    tick = 10
    clock = pygame.time.Clock()
    M = con.generarMatrizAleatoria(filas,columnas)
    w = columnas * tam
    h = filas * tam
    window = pygame.display.set_mode((w,h))
    pygame.display.set_caption("Life-Like")
    pausa = False
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                elif event.key == pygame.K_r:
                    M = con.generarMatrizAleatoria(filas,columnas)
                elif event.key == pygame.K_b:
                    M = con.generarMatrizVacia(filas,columnas)
                elif event.key == pygame.K_g:
                    guardarEstado(M,filas,columnas,tam,nacimiento,sobrevive)
                elif event.key == pygame.K_c:
                    datos = cargarEstado()
                    if datos is not None:
                        ( M,filas,columnas,tam,nacimiento,sobrevive) = datos
                        w = columnas * tam
                        h = filas * tam
                        window = pygame.display.set_mode((w,h))
                elif event.key == pygame.K_ESCAPE:
                    loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    f = y // tam
                    c = x // tam
                    if 0 <= f < filas and 0 <= c < columnas:
                        M[f][c] = (M[f][c] + 1) % 2
        window.fill((0,0,0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    pygame.draw.rect(window,(0,255,128),(c*tam,f*tam,tam,tam))
        if not pausa:
            M = con.transicion(M,nacimiento,sobrevive)
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()

if __name__ == "__main__":
    main()

