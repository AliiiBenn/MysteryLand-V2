from typing import Optional


from .entity import Entity
from .directions import Directions
from .animations import Animations

import pygame as py



class Player(Entity):
    def __init__(self, x : int, y : int, image_path : str, speed : int) -> None:
        super().__init__(x, y, image_path, speed)
        
        
    def update(self, screen : py.surface.Surface) -> None:
        if not self.moving:
            self.idling(self.direction)
        self.draw(screen)
        self.move()
        
    def move(self) -> None:
        keys = py.key.get_pressed()
        walk_directions = {
            Directions.RIGHT: Animations.WALK_RIGHT,
            Directions.UP: Animations.WALK_UP,
            Directions.LEFT: Animations.WALK_LEFT,
            Directions.DOWN: Animations.WALK_DOWN
        }
        
        if keys[py.K_z]:
            self.coords.y -= self.speed
            self.direction = Directions.UP
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if keys[py.K_s]:
            self.coords.y += self.speed
            self.direction = Directions.DOWN
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if keys[py.K_q]:
            self.coords.x -= self.speed
            self.direction = Directions.LEFT
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if keys[py.K_d]:
            self.coords.x += self.speed
            self.direction = Directions.RIGHT
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
            
        if all(not key for key in keys):
            self.moving = False
            
        if self.image is None:
            raise ValueError("No image found for entity")
            
        if self.rect is None:
            self.rect = self.image.get_rect()
            
            
        self.rect.topleft = (int(self.coords.x), int(self.coords.y))