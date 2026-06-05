from easygui import *
import pygame
import pickle as pk
import conway_logica as con
import hormiga_logica as hor



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

def regla_hormiga():
    """
    Esta función le pide al usuario una secuencia para la Hormiga de Langton
    Entradas: Ninguna
    Salidas: La secuencia que elige el usuario para la hormiga
    Restricciones: La secuencia debe ser un str formado por "L" y "R"
    """
    while True:
        regla = enterbox("Digita la secuencia de la hormiga\nEjemplos: LR, RLR, LLRR","Hormiga de Langton")
        if regla is None:
            raise SystemExit
        regla = regla.upper().replace(" ", "")
        if regla == "":
            msgbox("Debes ingresar al menos una letra.","Error")
            continue
        if not all(letra in ("L", "R") for letra in regla):
            msgbox("La secuencia solo puede contener las letras L y R.","Error")
            continue
        return regla

def guardarEstado(datos):
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
                pk.dump(datos,archivo)
            msgbox("Simulación guardada correctamente :)","Guardar")
            return
        except Exception as e:
            msgbox(str(e),"ERROR")

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
    except Exception as e:
        msgbox(str(e), "ERROR AL CARGAR")
        #msgbox("El archivo seleccionado no es válido.","Error")
        return None

def main():

    msgbox("¡Bienvenido al simulador de Autómatas Celulares!\n \n Hecho por Zack Rojas y Jose Oviedo","Life-Like")
    tipo_automata = choicebox("Seleccione el autómata que desea utilizar", title= "Autómatas Celiulares", choices=["Life-Like", "Hormiga de Langton"]) 
    if tipo_automata == None:
        raise SystemExit
    elif tipo_automata == "Life-Like":
        nacimiento, sobrevive = pedirRegla()
    else:
        instrucciones = regla_hormiga()
    filas = pedirEnteroPositivo("Digita la cantidad de filas")
    columnas = pedirEnteroPositivo("Digita la cantidad de columnas")
    tam = pedirEnteroPositivo("Digita el tamaño de las celdas")
    pygame.init()
    if tipo_automata == "Life-Like":
        tick = 10
    else:
        tick = 700
    clock = pygame.time.Clock()
    if tipo_automata == "Life-Like":
        M = con.generarMatrizAleatoria(filas,columnas)
    else:
        M = hor.generar_matriz(filas, columnas)
        colores = hor.generarColores(len(instrucciones))
        filaHormiga = filas // 2
        columnaHormiga = columnas // 2
        direccion = "U"
    w = columnas * tam
    h = filas * tam
    window = pygame.display.set_mode((w,h))
    pygame.display.set_caption("Autómatas Celulares")
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
                    if tipo_automata == "Life-Like":
                        M = con.generarMatrizAleatoria(filas,columnas)
                    else:
                        M = hor.generar_matriz(filas,columnas)
                        filaHormiga = filas // 2
                        columnaHormiga = columnas // 2
                        direccion = "U"
                        
                elif event.key == pygame.K_b:
                    if tipo_automata == "Life-Like":
                        M = con.generarMatrizVacia(filas,columnas)
                    else:
                        M = hor.generar_matriz(filas,columnas)
                        filaHormiga = filas // 2
                        columnaHormiga = columnas // 2
                        direccion = "U"
                        
                elif event.key == pygame.K_g:
                    if tipo_automata == "Life-Like":
                        guardarEstado(("Life-Like",M,filas,columnas,tam,nacimiento,sobrevive))
                    else:
                         guardarEstado(("Hormiga",M,filas,columnas,tam,instrucciones,filaHormiga,columnaHormiga,direccion))
                    pygame.event.clear()
                         
                elif event.key == pygame.K_c:
                    datos = cargarEstado()
                    pygame.event.clear()
                    if datos is not None:
                        tipoGuardado = datos[0]
                        if tipoGuardado == "Life-Like":
                            (_,M,filas,columnas,tam,nacimiento,sobrevive)=datos
                            tipo_automata = "Life-Like"
                            tick = 10
                        else:
                            (_,M,filas,columnas,tam,instrucciones,filaHormiga,columnaHormiga,direccion)=datos
                            colores = hor.generarColores(len(instrucciones))
                            tipo_automata = "Hormiga de Langton"
                            tick = 700
                            w = columnas * tam
                            h = filas * tam
                            window=pygame.display.set_mode((w, h))
                        
                        
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
                if tipo_automata == "Life-Like":
                    if M[f][c] == 1:
                        pygame.draw.rect(window,(0,255,128),(c*tam,f*tam,tam,tam))
                else:
                    if M[f][c] != 0:
                        pygame.draw.rect(window, colores[M[f][c]-1],(c*tam,f*tam,tam,tam))
        if not pausa:
            if tipo_automata == "Life-Like":
                M=con.transicion(M, nacimiento, sobrevive)
            else:
                (M,filaHormiga,
                 columnaHormiga,
                 direccion) = hor.siguiente(M,filaHormiga,columnaHormiga,direccion,filas,columnas,len(instrucciones),instrucciones) 
                
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()

if __name__ == "__main__":
    main()

