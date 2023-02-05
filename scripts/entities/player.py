from typing import Optional


from .entity import Entity
from .directions import Directions
from .animations import Animations
from .errors import ImageNotFoundForEntityError

import pygame as py



class Player(Entity):
    def __init__(self, x : int, y : int, image_path : str, speed : int) -> None:
        super().__init__(x, y, image_path, speed)
        
        
    def update(self) -> None:
        if not self.moving:
            self.idling(self.direction)
        self.image = self.animations.image
        self.move()
        
    def move(self) -> None:
        keys = py.key.get_pressed()
        walk_directions = {
            Directions.RIGHT: Animations.WALK_RIGHT,
            Directions.UP: Animations.WALK_UP,
            Directions.LEFT: Animations.WALK_LEFT,
            Directions.DOWN: Animations.WALK_DOWN
        }
        
        UP_MOVING_KEYS = [keys[py.K_z], keys[py.K_UP]]
        DOWN_MOVING_KEYS = [keys[py.K_s], keys[py.K_DOWN]]
        LEFT_MOVING_KEYS = [keys[py.K_q], keys[py.K_LEFT]]
        RIGHT_MOVING_KEYS = [keys[py.K_d], keys[py.K_RIGHT]]
        
        if any(UP_MOVING_KEYS):
            self.coords.y -= self.speed
            self.direction = Directions.UP
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if any(DOWN_MOVING_KEYS):
            self.coords.y += self.speed
            self.direction = Directions.DOWN
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if any(LEFT_MOVING_KEYS):
            self.coords.x -= self.speed
            self.direction = Directions.LEFT
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
        if any(RIGHT_MOVING_KEYS):
            self.coords.x += self.speed
            self.direction = Directions.RIGHT
            self.moving = True
            self.animations.change_animation(walk_directions[self.direction])
            
            
            
        for key in [UP_MOVING_KEYS, DOWN_MOVING_KEYS, LEFT_MOVING_KEYS, RIGHT_MOVING_KEYS]:
            if any(key):
                break
        else:
            self.moving = False
            
        if self.image is None:
            raise ImageNotFoundForEntityError("No image found for entity")
            
        if self.rect is None:
            self.rect = self.image.get_rect()
            
            
        self.rect.topleft = (int(self.coords.x), int(self.coords.y))