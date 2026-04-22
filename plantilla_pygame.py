# Plantilla básica para gráficos estáticos con Pygame
# Basada en la estructura de programarcadegames.com

import pygame

# --- Colores (R, G, B) ---
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
ROJO    = (255,   0,   0)
VERDE   = (  0, 255,   0)
AZUL    = (  0,   0, 255)
AMARILLO= (255, 255,   0)
NARANJA = (255, 165,   0)

# --- Inicialización de Pygame ---
pygame.init()

# --- Tamaño de la ventana ---
ANCHO = 700
ALTO  = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# --- Título de la ventana ---
pygame.display.set_caption("Mis gráficos")

# --- Bucle principal ---
hecho = False
reloj = pygame.time.Clock()

while not hecho:

    # 1) Gestión de eventos (no modificar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # 2) Fondo de la pantalla
    pantalla.fill(BLANCO)

    # -------------------------------------------------------
    # 3) DIBUJA AQUÍ TUS FIGURAS
    # -------------------------------------------------------

    # Línea: pygame.draw.line(pantalla, color, [x1, y1], [x2, y2], grosor)
    pygame.draw.line(pantalla, NEGRO, [435, 300], [550, 400], 3)
    pygame.draw.line(pantalla, NEGRO, [375, 299], [430, 400], 3)
    pygame.draw.line(pantalla, NEGRO, [700, 400], [0, 400], 5)
    pygame.draw.line(pantalla, NEGRO, [697, 450], [650, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [630, 450], [580, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [560, 450], [510, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [490, 450], [440, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [420, 450], [370, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [350, 450], [300, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [280, 450], [230, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [210, 450], [160, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [140, 450], [90, 450], 4)
    pygame.draw.line(pantalla, NEGRO, [70, 450], [20, 450], 4)
    # Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    #   grosor=0 → relleno; grosor>0 → solo borde
    pygame.draw.rect(pantalla, NARANJA, [300, 150, 150, 150], 0)
    pygame.draw.rect(pantalla, NEGRO, [300, 150, 150, 150], 2)
    pygame.draw.rect(pantalla, AZUL, [315, 165, 40, 50], 0)
    pygame.draw.rect(pantalla, ROJO, [375, 190, 60, 108], 0)
    # Elipse / círculo: pygame.draw.ellipse(pantalla, color, [x, y, ancho, alto], grosor)
    pygame.draw.ellipse(pantalla, AMARILLO, [640, -50, 150, 150], 0)
    # Polígono: pygame.draw.polygon(pantalla, color, [[x1,y1],[x2,y2],...], grosor)
    pygame.draw.polygon(pantalla, VERDE, [[280, 150], [375, 60], [470, 150]], 0)
    pygame.draw.polygon(pantalla, NEGRO, [[280, 150], [375, 60], [470, 150]], 2)  
    # Arco: pygame.draw.arc(pantalla, color, [x, y, ancho, alto], ang_inicio, ang_fin, grosor)
    #   ángulos en radianes; 0 = derecha, math.pi/2 = arriba

    
    # -------------------------------------------------------
    # 4) Actualizar pantalla (no modificar)
    # -------------------------------------------------------
    pygame.display.flip()
    reloj.tick(60)

# --- Salir de Pygame ---
pygame.quit()
