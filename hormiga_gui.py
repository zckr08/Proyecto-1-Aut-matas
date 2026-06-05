import pygame
import hormiga_logica as hor

tam = 10
filas = 100
columnas = 100
tick = 1000



def main():
    filaHormiga = filas // 2
    columnaHormiga = columnas // 2
    direccion = "R"
    pygame.init()
    clock = pygame.time.Clock()
    M = hor.generar_matriz(filas, columnas)
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
            M, filaHormiga, columnaHormiga, direccion  = hor.avanzar(M, filaHormiga, columnaHormiga, direccion)
        pygame.display.update()
        clock.tick(1000)
    pygame.quit()

if __name__ == "__main__":
    main()


    