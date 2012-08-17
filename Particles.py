import math
import random
import constants
from constants import *

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
		#self.elasticity = PARTICLE_ELASTICITY
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

		
class Environment:
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
        self.particles = []

        self.colour = BACKGROUND_COLOR
        self.mass_of_air = AIR_MASS
        self.elasticity = ELASTICITY
		
	def addParticles(self, n=200, **kargs):	#kargs eh um dicionario
		for i in range(n):
			size = kargs.get('size', random.randint(2, 15))
			density = kargs.get('density', random.randint(1, 20))
			mass = kargs.get('mass', density*size**2)
			x = kargs.get('x', random.uniform(size, self.width-size))
			y = kargs.get('y', random.uniform(size, self.height-size))

			p = Particle((x, y), size, mass)
			p.speed = kargs.get('speed', random.random())
			p.angle = kargs.get('angle', random.uniform(0, math.pi*2))
			p.colour = kargs.get('colour', PARTICLE_COLOR)
			p.air_resistance = kargs.get('air_resistance', (p.mass/(p.mass + self.mass_of_air)) ** p.size)
			p.thickness = kargs.get('fill', PARTICLE_FILL)
			self.particles.append(p)
	
	def update(self):
		for i, particle in enumerate(self.particles):
			particle.move()
			self.bounce(particle)
			if PARTICLE_COLLISION:
				for particle2 in self.particles[i+1:]:
					collide(particle, particle2)
				
				
	def bounce(self, particle):
		if particle.x > self.width - particle.size:  #DIREITA
			particle.x = 2*(self.width - particle.size) - particle.x
			particle.angle = - particle.angle
			particle.speed *= particle.mass / (self.elasticity + particle.mass)

		elif self.x < particle.size:                    #ESQUERDA
			particle.x = 2*particle.size - particle.x
			particle.angle = - particle.angle
			particle.speed *= particle.mass / (self.elasticity + particle.mass)

		if particle.y > self.height - particle.size:  #BAIXO
			particle.y = 2*(self.height - particle.size) - particle.y
			particle.angle = math.pi - particle.angle
			particle.speed *= particle.mass / (self.elasticity + particle.mass)

		elif particle.y < particle.size:                    #CIMA
			particle.y = 2*particle.size - particle.y
			particle.angle = math.pi - particle.angle
			particle.speed *= particle.mass / (self.elasticity + particle.mass)