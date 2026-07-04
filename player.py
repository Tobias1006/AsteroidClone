import sys
import pygame
from circleshape import CircleShape
from shot import Shot
from asteroid import Asteroid
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from constants import ASTEROID_MIN_RADIUS
from constants import LINE_WIDTH
from constants import LEVEL_DICT

class Player(CircleShape):

    def __init__(self, x: float, y: float, player_id: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.xp = 0
        self.level = 1
        self.__player_id = player_id
        self.__has_shield = False

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
        if self.__has_shield:            
            pygame.draw.circle(screen, "green", self.position, self.radius+5, LINE_WIDTH)

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
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
            
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        player_vector = unit_vector.rotate(self.rotation)
        player_vector *= (PLAYER_SPEED*dt)
        self.position += player_vector

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return
        new_shot = Shot(self.position[0], self.position[1], self)
        new_shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation))*PLAYER_SHOOT_SPEED
        if self.level > 1:
            self.shot_cooldown += (PLAYER_SHOOT_COOLDOWN_SECONDS/(0.75*self.level))
        else:
            self.shot_cooldown += PLAYER_SHOOT_COOLDOWN_SECONDS
    
    def gain_xp(self, ast: Asteroid, shot: Shot) -> None:
        if ast.radius == ASTEROID_MIN_RADIUS:
            self.xp += 3            
        elif ast.radius == ASTEROID_MIN_RADIUS*2:
            self.xp += 2
        else: self.xp += 1
        self.level_up(LEVEL_DICT)

    def level_up(self, level_dict: dict) -> None:
        needed_xp = level_dict.get(self.level)
        if needed_xp != None and self.xp >= needed_xp:
            self.level += 1
            self.xp = 0
            if not self.__has_shield and self.level > 1:
                self.__has_shield = True

    def get_hit(self, asteroid: Asteroid) -> None:
        if self.__has_shield:
            self.__has_shield = False
            asteroid.kill()            
        else:
            print("Game over!")
            sys.exit()