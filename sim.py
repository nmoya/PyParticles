import pygame
import Particles
import random
from constants import *

def escreve (msg, pos):
    text = fonte.render(msg, 0, TEXT_COLOR)
    textpos = text.get_rect()
    textpos.topleft = pos
    SCREEN.blit(text, textpos)

pygame.init()
Clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(RESOLUTION)
SCREEN.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Partoya - ' + str(RESOLUTION[RES_X]) + ", " + str(RESOLUTION[RES_Y]))
fonte = pygame.font.Font('lucon.ttf', 18)

#Environment(colour=(0,0,0), air_mass=0.2, elasticity=0, acceleration=0.002)
env = Particles.Environment(RESOLUTION, air_mass = 0)
'''addParticles(size=[2,10]
            ,mass=[1,20]*size**2
            ,x
            ,y
            ,speed = [0, 1]
            ,angle=[0-360]
            ,colour = verde
            ,air_resistance = (p.mass/(p.mass + self.mass_of_air)) ** p.size)
            ,thickness = 0
'''

env.addFunctions(['move', 'bounce', 'attract', 'combine'])
for p in range(200):
    p_mass = random.randint(10,20)
    p_size = 0.4 * p_mass ** (0.5)

    env.addParticles(size=p_size
                 ,mass=p_mass
                 ,elasticity=0.9
                 ,speed=0.5)

running = True
while running:

    SCREEN.fill(env.colour)

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
    env.update()
    '''for p in env.particles:
        pygame.draw.circle(SCREEN, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)
    '''
    particles_to_remove = []
    for p in env.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = 0.4 * p.mass ** (0.5)
            del p.__dict__['collide_with']
        p.move()
        if p.size < 2:
            pygame.draw.rect(SCREEN, p.colour, (int(p.x), int(p.y), 2, 2))
        else:
            pygame.draw.circle(SCREEN, p.colour, (int(p.x), int(p.y)), int(p.size), 0)

    for p in particles_to_remove:
        if p in env.particles:
            env.particles.remove(p)
        


    escreve(EFFECT, (2, 2))
    escreve("FPS: " + str(Clock.get_fps()), (2,20))
    escreve("Nro. Particles: " + str(len(env.particles)), (10,45))
    pygame.display.flip()
    Clock.tick(1000)
    
pygame.quit()
