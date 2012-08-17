import pygame
import Particles
from constants import *

pygame.init()
Clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(RESOLUTION)
SCREEN.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Partoya - ' + str(RESOLUTION[RES_X]) + ", " + str(RESOLUTION[RES_Y]))
fonte = pygame.font.Font('lucon.ttf', 18)


env = Particles.Environment(RESOLUTION)
env.addParticles(5)

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
    for p in env.particles:
        pygame.draw.circle(SCREEN, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)



    #Desenha todas as particulas a N FPSs
    '''for i, p in enumerate(Particles):
        p.dicFunctions[str(EFFECT_INDEX)]()     #Aplica a funcao de movimentacao do efeito selecionado. Default = move.
        p.bounce()
        if PARTICLE_COLLISION:
            for part2 in Particles[i+1:]:
                collide (p, part2)
        
        p.display()'''

    escreve(EFFECT, (2, 2))
    escreve("FPS: " + str(Clock.get_fps()), (2,20))
    escreve("Speed: " + str(Particles[0].speed), (10,45))
    pygame.display.flip()
    Clock.tick(1000)
    
pygame.quit()
