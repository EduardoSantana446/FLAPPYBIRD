import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mi primer juego con Pygame")

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(NEGRO)          # Fondo negro
    pygame.draw.circle(screen, AZUL, (300, 200), 50)  # Círculo azul
    pygame.display.flip()       # Actualiza la pantalla

pygame.quit()
