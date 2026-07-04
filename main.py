import sys
import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from progressbar import Progressbar
from xpbar import Xpbar



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    displays = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Progressbar.containers = (displays, updatable, drawable)
    Xpbar.containers = (displays, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 1)
    level_bar = Progressbar(SCREEN_WIDTH-300, 20, 280, 20)
    xp_bar = Xpbar(SCREEN_WIDTH-295, 24.5, 0, 20, player)
    new_asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")        
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()
                    player.gain_xp(ast, shot)
                    print(f"Player-Xp = :{player.xp}")
        for ent in drawable:
            ent.draw(screen)   
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
