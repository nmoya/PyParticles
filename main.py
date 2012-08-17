import pygame
import random
from constants import *

def escreve (msg, pos):
    text = fonte.render(msg, 0, TEXT_COLOR)
    textpos = text.get_rect()
    textpos.topleft = pos
    SCREEN.blit(text, textpos)

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x, y)                                       #Hipotenusa: Entre (x, y) e (0, 0) http://www.petercollingridge.co.uk/sites/files/peter/Graph%20of%20vector%20addition.jpg
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)

def collide(p1, p2):    #http://www.petercollingridge.co.uk/pygame-physics-simulation/collisions
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    distance = math.hypot(dx, dy)
    
    if distance < p1.size + p2.size:
        if COLLISION_WITH_MASS:
            angle = math.atan2(dy, dx) + 0.5 * math.pi
            total_mass = p1.mass + p2.mass

            (p1.angle, p1.speed) = addVectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass), (angle, 2*p2.speed*p2.mass/total_mass))
            (p2.angle, p2.speed) = addVectors((p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass), (angle+math.pi, 2*p1.speed*p1.mass/total_mass))

            overlap = 0.5*(p1.size + p2.size - distance+1)
            p1.x += math.sin(angle)*overlap
            p1.y -= math.cos(angle)*overlap
            p2.x -= math.sin(angle)*overlap
            p2.y += math.cos(angle)*overlap

        else:
            tangent = math.atan2(dy, dx)
            p1.angle = 2*tangent - p1.angle
            p2.angle = 2*tangent - p2.angle
            (p1.speed, p2.speed) = (p2.speed, p1.speed)

            #Evitando que duas particulas se grudem:
            angle = 0.5 * math.pi + tangent
            p1.x += math.sin(angle)
            p1.y -= math.cos(angle)
            p2.x -= math.sin(angle)
            p2.y += math.cos(angle)

        #Perda de energia com colisao
        p1.speed *= ENERGY_LOSS_COLLISION
        p2.speed *= ENERGY_LOSS_COLLISION                

class Particle:
    def __init__(self, (x, y), size, mass = 1):
        self.x = x
        self.y = y
        self.size = size
        self.thickness = PARTICLE_FILL
        self.colour = PARTICLE_COLOR
        self.speed = PARTICLE_SPEED
        self.angle = PARTICLE_ANGLE
        self.mass = mass
        self.air_resistance = (self.mass/(self.mass + AIR_MASS))
        self.dicFunctions = {"0": self.move				#Dicionario para diferentes funcoes de movimentacao das particulas.
        ,"1": self.moveGravity
        ,"2": self.pause}
		
    def display(self):
        pygame.draw.circle(SCREEN, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def pause(self):
        pass

    def moveGravity(self):
        pass
    
    def move (self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), GRAVITY)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        if SIZE_PROPORTIONAL:
            self.speed *= (1-self.size/10000)
        else:
            self.speed *= self.air_resistance

    def bounce(self):
        if self.x > RESOLUTION[RES_X] - self.size:  #DIREITA
            self.x = 2*(RESOLUTION[RES_X] - self.size) - self.x
            self.angle = - self.angle
            self.speed *= self.mass / (ELASTICITY + self.mass)

        elif self.x < self.size:                    #ESQUERDA
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= self.mass / (ELASTICITY + self.mass)

        if self.y > RESOLUTION[RES_Y] - self.size:  #BAIXO
            self.y = 2*(RESOLUTION[RES_Y] - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.mass / (ELASTICITY + self.mass)

        elif self.y < self.size:                    #CIMA
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.mass / (ELASTICITY + self.mass)


pygame.init()
Clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(RESOLUTION)
SCREEN.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Partoya - ' + str(RESOLUTION[RES_X]) + ", " + str(RESOLUTION[RES_Y]))
fonte = pygame.font.Font('lucon.ttf', 18)

Particles = []
for n in range(PARTICLE_NUMBER):
    size = PARTICLE_SIZE
    if CONSTANT_X != False: x = CONSTANT_X
    else: x = random.randint(size, RESOLUTION[RES_X]-size)
    if CONSTANT_Y != False: y = CONSTANT_Y
    else: y = random.randint(size, RESOLUTION[RES_Y]-size)

    density = random.randint(1, 20)
    if CONSTANT_MASS: mass = PARTICLE_MASS
    else: mass = density*size**2
    
    particle = Particle ((x, y), size, mass)
    
    if not CONSTANT_COLOR: particle.colour = (PARTICLE_COLOR[0], PARTICLE_COLOR[1]-density*10, PARTICLE_COLOR[2])

    if CONSTANT_SPEED: particle.speed = PARTICLE_SPEED
    else: particle.speed = random.random()

    if CONSTANT_ANGLE != False: particle.angle = CONSTANT_ANGLE
    else: particle.angle = random.uniform(0, math.pi*2)

    Particles.append(particle)

running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    
    #Evento de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            MOUSEX, MOUSEY = event.pos

        #Tecla pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                EFFECT = "Normal"
                EFFECT_INDEX = 0
            elif event.key == pygame.K_g:
                EFFECT = "Mouse click gravity"
                EFFECT_INDEX = 1
            elif event.key == pygame.K_p:
                EFFECT = "Paused"
                EFFECT_INDEX = 2
            elif event.key == pygame.K_c:
                PARTICLE_COLLISION = not PARTICLE_COLLISION
                

    #Desenha todas as particulas a N FPSs
    for i, p in enumerate(Particles):
        p.dicFunctions[str(EFFECT_INDEX)]()     #Aplica a funcao de movimentacao do efeito selecionado. Default = move.
        p.bounce()
        if PARTICLE_COLLISION:
            for part2 in Particles[i+1:]:
                collide (p, part2)
        
        p.display()

    escreve(EFFECT, (2, 2))
    escreve("FPS: " + str(Clock.get_fps()), (2,20))
    escreve("Speed: " + str(Particles[0].speed), (10,45))
    pygame.display.flip()
    Clock.tick(1000)
    
pygame.quit()


