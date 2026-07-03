import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
from constants import PLAYER_TURN_SPEED
from constants import LINE_WIDTH

class Player(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += (PLAYER_TURN_SPEED*dt)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        player_vector = unit_vector.rotate(self.rotation)
        player_vector *= (PLAYER_SPEED*dt)
        self.position += player_vector