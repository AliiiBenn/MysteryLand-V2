from typing import Optional


from .entity import Entity
from .directions import Directions

import pygame as py



class Player(Entity):
    def __init__(self, x : int, y : int, image_path : str, speed : int) -> None:
        super().__init__(x, y, image_path, speed)
        
        
    def update(self, screen : py.surface.Surface) -> None:
        self.draw(screen)
        self.move()
        
    def move(self) -> None:
        keys = py.key.get_pressed()
        
        if keys[py.K_z]:
            self.coords.y -= self.speed
            self.direction = Directions.UP
            
        if keys[py.K_s]:
            self.coords.y += self.speed
            self.direction = Directions.DOWN
            
        if keys[py.K_q]:
            self.coords.x -= self.speed
            self.direction = Directions.LEFT
            
        if keys[py.K_d]:
            self.coords.x += self.speed
            self.direction = Directions.RIGHT
            
        if self.image is None:
            raise ValueError("No image found for entity")
            
        if self.rect is None:
            self.rect = self.image.get_rect()
            
            
        self.rect.topleft = (int(self.coords.x), int(self.coords.y))