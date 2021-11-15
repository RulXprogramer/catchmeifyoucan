import pygame
import sys
from pygame.locals import *
from random import randint

# Iniciamos la libreria
pygame.init()

# Creamos una ventana
ventana = pygame.display.set_mode((500, 400))

# Se le asigna nombre a la ventana
pygame.display.set_caption("Space Wars")

# Se crea variable que contendra el color de fondo de la ventana
colorFondo = (1, 10, 70)
# Variable que contendra el el color de la figura
colorCuadro01 = (255, 255, 255)
colorCuadro02 = (0, 0, 0)
# Variable que contendra el color del texto
colorTexto = (255, 255, 255)
# Variables de movimiento
velocidad = 15
direccion = True
posX01, posY01 = randint(1, 400), randint(1, 300)
posX02, posY02 = randint(1, 400), randint(50, 300)
lado = 40
# Variable del texto
cadena01 = "COLISION!!! en coordenada"
cadena02 = "Tiempo: "
tamaño = 20
tipoFuente = "Consolas"
# Preparacion de fuente/texto
fuente = pygame.font.SysFont(tipoFuente, tamaño)
texto01 = fuente.render(cadena01, True, colorTexto)
texto02 = fuente.render(cadena02, True, colorTexto)
# Mantiene la ventana ejecutandose
while True:
    # Colorea el fondo de la ventana
    ventana.fill(colorFondo)
    # Mostrar texto
    ventana.blit(texto01, (10, 10))
    ventana.blit(texto02, (10, 30))
    # Tiempo transcurrido desde el inicio del juego
    tiempo = pygame.time.get_ticks()/1000
    cadena02 = (f'Tiempo: {str(tiempo)}')
    texto02 = fuente.render(cadena02, True, colorTexto)
    # Dibuja los cuadrados
    cuadro01 = pygame.draw.rect(
        ventana, colorCuadro01, (posX01, posY01, lado, lado))
    cuadro02 = pygame.draw.rect(
        ventana, colorCuadro02, (posX02, posY02, lado, lado))
    # Deteccion de la colision con el otro cuadrado
    if cuadro01.colliderect(cuadro02):
        # Muestra coordenadas en consola
        print(f'COLISION!!! en coordenada {posX01} : {posY01}')
        # Muestra coordenadas en ventana
        cadena01 = (f'COLISION!!! en coordenada {posX01} : {posY01}')
        texto01 = fuente.render(cadena01, True, colorTexto)
        # Reposiciona el cuadro negro
        posX02, posY02 = randint(1, 400), randint(50, 300)
        cuadro02.left = posX02-(lado/2)
        cuadro02.top = posY02-(lado/2)
    # Movimento a traves del mouse
    posX01, posY01 = pygame.mouse.get_pos()
    # Variables para que el punto de referencia del mouse sea el centro del cuadrado
    posX01 = posX01 - (lado/2)
    posY01 = posY01 - (lado/2)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    # Mantener esta linea fuera del 'for' hace que este en constante actualizacion
    pygame.display.update()
