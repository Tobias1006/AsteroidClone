import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None :
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt) -> None :
        self.position += (self.velocity*dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vel_ast_1 = self.velocity.rotate(angle)
            vel_ast_2 = self.velocity.rotate(-angle)
            new_radius = self.radius-ASTEROID_MIN_RADIUS
            new_ast_1 = Asteroid(self.position[0],self.position[1], new_radius)
            new_ast_2 = Asteroid(self.position[0],self.position[1], new_radius)
            new_ast_1.velocity = vel_ast_1*1.2
            new_ast_2.velocity = vel_ast_2*1.2
