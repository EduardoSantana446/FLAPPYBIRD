import pygame
from sys import exit
import random

#Dimensiones del cardenal bird y posicionamiento
bird_x = 360/8
bird_y = 640/2
bird_ancho = 48
bird_alto = 38

class BirdPosicion(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, bird_x, bird_y, bird_ancho, bird_alto)
        self.img = img
        
        
#Dimensiones de las tuberias y posicionamiento
tubo_x = 360
tubo_y = 0
anchuraDetubo = 64
alturaDeltubo = 512

class TuberiasPosicion(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, tubo_x, tubo_y, anchuraDetubo, alturaDeltubo)
        self.img = img
        self.passed = False


#Imagenes Cardenal Bird
Fondo_principal = pygame.image.load("FondoPrincipal.jpeg")
CadenalBird = pygame.image.load("Cardenal.png")
CadenalBird = pygame.transform.scale(CadenalBird, (bird_ancho,bird_alto))
TuberiaSuperiorImagen = pygame.image.load("tuboSuperior.png")
TuberiaSuperiorImagen = pygame.transform.scale(TuberiaSuperiorImagen, (anchuraDetubo, alturaDeltubo))
TuberiaInferiorImagen = pygame.image.load("tuboInferior.png")
TuberiaInferiorImagen = pygame.transform.scale(TuberiaInferiorImagen, (anchuraDetubo, alturaDeltubo))

#logica del juego
pajaro = BirdPosicion(CadenalBird)
tuberias = []
velocidad_x = -2
velocidad_y = 0
gravedad = 0.4
score = 0
gameOver = False

def imagenes():
    screen.blit(Fondo_principal, (0, 0))
    screen.blit(pajaro.img, pajaro)
    
    for tubos in tuberias:
        screen.blit(tubos.img, tubos)
        
    textoPuntuacion = str(int(score))
    if gameOver:
        textoPuntuacion = "Game Over: " + textoPuntuacion
        
    fuenteText = pygame.font.SysFont("Comic Sans MS", 45)
    textoRenderizado = fuenteText.render(textoPuntuacion, True, "Red")
    screen.blit(textoRenderizado, (5, 0))
        
def movimiento():
    global velocidad_y, score, gameOver
    velocidad_y += gravedad             
    pajaro.y += velocidad_y                       
    pajaro.y = max(pajaro.y, 0)
    
    if pajaro.y > 640:
        gameOver = True
        return               
                                                        
    for tubos in tuberias:
        tubos.x += velocidad_x
        
        if not tubos.passed and pajaro.x > tubos.x + tubos.width:
            score += 0.5
            tubos.passed = True
            
            
        if pajaro.colliderect(tubos):
            gameOver = True
            return 
        
    while len(tuberias) > 0 and tuberias[0].x < - anchuraDetubo:
        tuberias.pop(0)
    
def creacionTuberias():
    tuberiaAleatoria_y = tubo_y - alturaDeltubo/4 - random.random() * (alturaDeltubo/2)
    espacioApertura = 640/6
    
    Tuberia_Superior = TuberiasPosicion(TuberiaSuperiorImagen)
    Tuberia_Superior.y = tuberiaAleatoria_y
    tuberias.append(Tuberia_Superior)
    
    Tuberia_Inferior = TuberiasPosicion(TuberiaInferiorImagen)
    Tuberia_Inferior.y = Tuberia_Superior.y + Tuberia_Superior.height + espacioApertura
    tuberias.append(Tuberia_Inferior)
    
    print(len(tuberias))

pygame.init()
screen = pygame.display.set_mode((360, 640)) #Dimensiones de la pantalla
pygame.display.set_caption("CARDENAL BIRD")
clock = pygame.time.Clock()

#Musica
pygame.mixer.init()
pygame.mixer.music.load("FlappyMusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Velocidad de creacion de tuberias
creacionTuberiasTiempo = pygame.USEREVENT + 0
pygame.time.set_timer(creacionTuberiasTiempo, 1600)


#BUCLE DE JUEGO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == creacionTuberiasTiempo and not gameOver:
            creacionTuberias() 
           
        if event.type == pygame.KEYDOWN:
           if event.key in (pygame.K_SPACE, pygame.K_x, pygame.K_UP):
               velocidad_y = -6
               
               # Reseteo del FlappyBird
               if gameOver: 
                   pajaro.y = bird_y
                   tuberias.clear()
                   score = 0
                   gameOver = False
    
    if not gameOver:               
       movimiento()        
       imagenes()        
       pygame.display.update()
       clock.tick(60)