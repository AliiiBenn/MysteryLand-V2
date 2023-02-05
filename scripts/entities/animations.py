from enum import Enum
import pygame as py
from typing import Optional, Final

from .constants import ENTITY_WIDTH, ENTITY_HEIGHT, BLACK


class Animations(Enum):
    IDLE_RIGHT = "idle_right"
    IDLE_UP = "idle_up"
    IDLE_LEFT = "idle_left"
    IDLE_DOWN = "idle_down"
    WALK_RIGHT = "walk_right"
    WALK_UP = "walk_up"
    WALK_LEFT = "walk_left"
    WALK_DOWN = "walk_down"
    
    
    

class EntityAnimations:
    def __init__(self, spritesheet_path : str) -> None:
        self.spritesheet = py.image.load(spritesheet_path).convert_alpha()
        self.animation_index = 0
        self.animation_speed = 1.5
        self.clock = 0.0
        
        
        self.animations : dict[Animations, list[py.surface.Surface]] = {
            Animations.IDLE_RIGHT: self.load_images(64, 0, 6),
            Animations.IDLE_UP: self.load_images(64, 6, 12),
            Animations.IDLE_LEFT: self.load_images(64, 12, 18),
            Animations.IDLE_DOWN: self.load_images(64, 18, 24),
            Animations.WALK_RIGHT: self.load_images(128, 0, 6),
            Animations.WALK_UP: self.load_images(128, 6, 12),
            Animations.WALK_LEFT: self.load_images(128, 12, 18),
            Animations.WALK_DOWN: self.load_images(128, 18, 24)
        }
        
        
        self.image : py.surface.Surface = self.animations[Animations.IDLE_DOWN][0] 
        
        
    
    def change_animation(self, animation : Animations):
        CLOCK_SPEED_MULTIPLIER : Final[int] = 8
        ANIMATION_TIME_LIMIT : Final[int] = 100
        INCREMENT : Final[int] = 1
        
        
        self.image = self.animations[animation][self.animation_index]
        self.image.set_colorkey(BLACK)
        self.clock += self.animation_speed * CLOCK_SPEED_MULTIPLIER
        
        
        if self.clock >= ANIMATION_TIME_LIMIT:
            self.animation_index += INCREMENT
            
            IS_ANIMATION_FINISHED : Final[bool] = self.animation_index >= len(self.animations[animation])
            if IS_ANIMATION_FINISHED:
                self.animation_index = 0
                
            self.clock = 0
            
        
    def load_images(self, y : int, start_x : int, end_x : int) -> list[py.surface.Surface]:
        images : list[py.surface.Surface] = []
        for x in range(start_x, end_x):
            image = self.load_image(x*ENTITY_WIDTH, y)
            images.append(image)
            
        return images
    
    def load_image(self, x : int, y : int) -> py.surface.Surface:
        image = py.Surface([ENTITY_WIDTH, ENTITY_HEIGHT])
        image.set_colorkey(BLACK)
        image.blit(self.spritesheet, (0, 0), (x, y, ENTITY_WIDTH, ENTITY_HEIGHT))
        return image