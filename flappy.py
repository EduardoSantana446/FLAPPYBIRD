import pygame
from sys import exit


#Imagenes Cardenal Bird
Fondo_principal = pygame.image.load("flappybirdbg.png")

def imagenes():
    screen.blit(Fondo_principal, (0, 0))
    

pygame.init()
screen = pygame.display.set_mode((360, 640)) #Dimensiones de la pantalla
pygame.display.set_caption("CARDENAL BIRD")



#BUCLE DE JUEGO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    imagenes()        
    pygame.display.update()
