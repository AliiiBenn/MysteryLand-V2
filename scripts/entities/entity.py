from typing import Final, Optional
import pygame as py
from enum import Enum

from .directions import Directions
from .animations import Animations, EntityAnimations
from .constants import ENTITY_WIDTH, ENTITY_HEIGHT
from .errors import ImageNotFoundForEntityError







class Entity(py.sprite.Sprite):
    def __init__(self, x : int, y : int, image_path : str, speed : int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        
        self.coords = py.Vector2(self.x, self.y)
        
        
        # self.image = py.surface.Surface([ENTITY_WIDTH, ENTITY_HEIGHT])
        
        self.animations = EntityAnimations(image_path)
        
        self.image = self.animations.image
        self.rect = self.image.get_rect()
        
        
        self.direction = Directions.RIGHT
        
        self.moving = False
        
    def update(self) -> None:
        raise NotImplementedError("update method must be overridden")
        
        
    def idling(self, direction : Directions) -> None:
        idling_directions = {
            Directions.RIGHT: Animations.IDLE_RIGHT,
            Directions.UP: Animations.IDLE_UP,
            Directions.LEFT: Animations.IDLE_LEFT,
            Directions.DOWN: Animations.IDLE_DOWN
            
        }
        
        self.animations.change_animation(idling_directions[direction])
        
    
            
    
    
