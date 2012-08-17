from constants import *



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
            self.speed *+ MOMENTUM

    def bounce(self):
        if self.x > RESOLUTION[RES_X] - self.size:
            self.x = 2*(RESOLUTION[RES_X] - self.size) - self.x
            self.angle = - self.angle
            self.speed *= ELASTICITY

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= ELASTICITY

        if self.y > RESOLUTION[RES_Y] - self.size:
            self.y = 2*(RESOLUTION[RES_Y] - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= ELASTICITY

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= ELASTICITY

