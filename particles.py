import pygame
import random
import math

RES_X                       = 0
RES_Y                       = 1
RESOLUTION                  = (640, 480)
BACKGROUND_COLOR            = (0,0,0)
NUMBER_PARTICLES            = 50
CONSTANT_SPEED              = 1
PARTICLE_COLOR              = (0, 255, 0)
PARTICLE_SPEED              = 50
PARTICLE_ANGLE              = math.pi
PARTICLE_FILL               = 0

TEXT_COLOR                  = (255,0,0)



def escreve(texto, x, y):
    msgSurfaceObj = fonte.render(texto, False, pygame.Color(TEXT_COLOR))
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft(x, y)
    SCREEN.blit(msgSurfaceObj, msgRectobj)

class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.thickness = PARTICLE_FILL
        self.colour = PARTICLE_COLOR
        self.speed = PARTICLE_SPEED
        self.angle = PARTICLE_ANGLE
        
    def display(self):
        pygame.draw.circle(SCREEN, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move (self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        if self.x > RESOLUTION[RES_X] - self.size:
            self.x = 2*(RESOLUTION[RES_X] - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle

        if self.y > RESOLUTION[RES_Y] - self.size:
            self.y = 2*(RESOLUTION[RES_Y] - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle



SCREEN = pygame.display.set_mode(RESOLUTION)
SCREEN.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Partoya')
fonte = pygame.font.Font('Arial.ttf', 24)


Particles = []
for n in range(NUMBER_PARTICLES):
    size = 8
    x = random.randint(size, RESOLUTION[RES_X]-size)
    y = random.randint(size, RESOLUTION[RES_Y]-size)
    particle = Particle ((x, y), size)

    if CONSTANT_SPEED:
        particle.speed = PARTICLE_SPEED
    else:
        particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)

    Particles.append(particle)



running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    escreve("oi")

    #Evento de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Desenha todas as particulas a N FPSs
    for p in Particles:
        p.move()
        p.bounce()
        p.display()
    pygame.display.flip()

    
pygame.quit()


