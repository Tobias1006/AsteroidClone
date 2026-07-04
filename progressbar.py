import pygame
from rectshape import RectShape
from constants import LINE_WIDTH

class Progressbar(RectShape):
    def __init__(self, left_corner: float, top_corner: float, width: float, height: float) -> None:
        super().__init__(left_corner, top_corner, width, height)
        self.left_corner = left_corner
        self.top_corner = top_corner
        self.width = width
        self.height = height
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "white", (self.left_corner, self.top_corner, self.width, self.height) , LINE_WIDTH)

