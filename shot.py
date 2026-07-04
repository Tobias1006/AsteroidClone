import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: int, y: int, player_id):
        super().__init__(x, y, SHOT_RADIUS)
        self.player_id = player_id

    def draw(self, screen) -> None :
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt) -> None :
        self.position += (self.velocity*dt)