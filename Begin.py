import pygame
import Particles
import random
import math

def escreve (msg, pos):
    text = fonte.render(msg, 0, Particles.TEXT_COLOR)
    textpos = text.get_rect()
    textpos.topleft = pos
    SCREEN.blit(text, textpos)


pygame.init()
Clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(Particles.RESOLUTION)
SCREEN.fill(Particles.BACKGROUND_COLOR)
pygame.display.set_caption('Partoya - ' + str(Particles.RESOLUTION[Particles.RES_X]) + ", " + str(Particles.RESOLUTION[Particles.RES_Y]))
fonte = pygame.font.Font('lucon.ttf', 18)

#Environment(colour=(0,0,0), air_mass=0.2, elasticity=0, acceleration=0.002)
env = Particles.Environment(Particles.RESOLUTION, acceleration = 0.000)


'''
Environment options:
- Move
- Air Resistance
- Bounce
- Accelerate
- MouseMove
- Collide
- Attract
- Combine
'''
env.addFunctions(['move', 'attract', "combine"])
for p in range(100):
    #speed, density, mass, (x, y), speed, angle, colour, elasticity, air_resistance, fill
    env.addParticles(size=1, colour=(255, 255, 255))

    
running = True
while running:

    SCREEN.fill(env.colour)

    #Evento de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            Particles.MOUSEX, Particles.MOUSEY = event.pos

        #Tecla pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Particles.EFFECT = "Normal"
                Particles.EFFECT_INDEX = 0
            elif event.key == pygame.K_g:
                Particles.EFFECT = "Mouse click gravity"
                Particles.EFFECT_INDEX = 1
            elif event.key == pygame.K_p:
                Particles.EFFECT = "Paused"
                Particles.EFFECT_INDEX = 2
            elif event.key == pygame.K_c:
                if env.inList('collide') >= 0:
                    env.removeFunctions(['collide'])
                else:
                    env.addFunctions(['collide'])
    env.update()


    particles_to_remove = []
    for p in env.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = 0.4 * p.mass ** (0.5)
            del p.__dict__['collide_with']
        if p.size < 2:
            pygame.draw.rect(SCREEN, p.colour, (int(p.x), int(p.y), 2, 2))
        else:
            pygame.draw.circle(SCREEN, p.colour, (int(p.x), int(p.y)), int(p.size), 0)

    for p in particles_to_remove:
        if p in env.particles:
            env.particles.remove(p)
        

    escreve(Particles.EFFECT, (2, 2))
    escreve("FPS: " + str(Clock.get_fps()), (2,20))
    escreve("Mouse: " + str(Particles.MOUSEX) + str(Particles.MOUSEY), (10,45))
    escreve("Speed: " + str(env.particles[0].speed), (10,75))
    escreve("Nro. Particles: " + str(len(env.particles)), (10,100))
    pygame.display.flip()
    Clock.tick(1000)
    
pygame.quit()
