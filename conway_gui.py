import pygame
import conway_logica as con
import pickle as pk

def guardarEstado(M, filas, columnas, tamaño, nacimiento, sobrevive):
    parametros = (M, filas, columnas, tamaño, nacimiento, sobrevive)
    with open("estadoConway.pkl", "wb") as archivo:
        pk.dump(parametros, archivo)

def cargarEstado():
    with open("estadoConway.pkl", "rb") as archivo:
        return pk.load(archivo)

tam = 10
filas = 50
columnas = 50
tick = 10

textoReglas = input("a: ")
textoReglas = list(textoReglas)
textoReglas.remove("B")
textoReglas.remove("S")
separacion = textoReglas.index("/")
nacimiento = tuple(int(caracter) for caracter in textoReglas[:separacion])
sobrevive = tuple(int(caracter) for caracter in textoReglas[separacion + 1:])

def main():
    pygame.init()
    clock = pygame.time.Clock()
    M = con.generarMatrizAleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pausa = not pausa
                if keys[pygame.K_r]:
                    M = con.generarMatrizAleatoria(filas, columnas)
                if keys[pygame.K_b]:
                    M = con.generarMatrizVacia(filas, columnas)
                if keys[pygame.K_g]:
                    guardarEstado (M, filas, columnas, tam, nacimiento, sobrevive)
                if keys[pygame.K_c]:
                    M, filas, columnas, tam, nacimiento, sobrevive = cargarEstado()
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = con.transicion(M, nacimiento, sobrevive)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()


    
