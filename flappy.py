import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("FLAPPY BIRD")

# Colores
AZUL = (0, 0, 0)
BLANCO = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(AZUL)          # Fondo negro
    pygame.draw.circle(screen, BLANCO, (300, 200), 50)  # Círculo azul
    pygame.display.flip()       # Actualiza la pantalla

pygame.quit()
