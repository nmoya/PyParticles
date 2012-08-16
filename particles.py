import pygame
import random

RES_X                       = 0
RES_Y                       = 1
RESOLUTION                  = (640, 480)
BACKGROUND_COLOR            = (0,0,0)
NUMBER_PARTICLES            = 1000
PARTICLE_COLOR              = (0, 0, 255)
PARTICLE_SPEED              = 0.01
PARTICLE_ANGLE              = 0


class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.thickness = 1
        self.colour = PARTICLE_COLOR
        self.speed = PARTICLE_SPEED
        self.angle = PARTICLE_ANGLE
        
    def display(self):
        pygame.draw.circle(SCREEN, self.colour, (self.x, self.y), self.size, self.thickness)


SCREEN = pygame.display.set_mode(RESOLUTION)
SCREEN.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Partoya')

Particles = []
for n in range(NUMBER_PARTICLES):
    size = 3
    x = random.randint(size, RESOLUTION[RES_X]-size)
    y = random.randint(size, RESOLUTION[RES_Y]-size)
    Particles.append(Particle ((x, y), size))



running = True
while running:

    #Evento de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Desenha todas as particulas a N FPSs
    for p in Particles:
        p.display()
    pygame.display.flip()

    
pygame.quit()


