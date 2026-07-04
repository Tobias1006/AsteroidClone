import pygame
from progressbar import Progressbar
from player import Player
from rectshape import RectShape
from constants import LEVEL_DICT

class Xpbar(RectShape):
    def __init__(self, left_corner: float, top_corner: float, width: float, height: float, player: Player) -> None:
        super().__init__(left_corner, top_corner, height, width)
        self.player = player
        self.levels = LEVEL_DICT
        self.left_corner = left_corner
        self.top_corner = top_corner
        self.height = height
        self.width = width
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.width >= 0:
            xp_rect = pygame.Rect(self.left_corner, self.top_corner, self.width, self.height)
            screen.fill("white", xp_rect)

    def update(self, dt):        
        if self.player.level <= 5:
            needed_xp = self.levels[self.player.level]
            self.width = (270/needed_xp)*self.player.xp
        else: self.width = 270
    
