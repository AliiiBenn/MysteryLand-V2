from typing import Optional
import pygame as py
from enum import Enum

from .directions import Directions
from .animations import Animations

BLACK = (0, 0, 0)
ENTITY_WIDTH, ENTITY_HEIGHT = 32, 64

class ImageNotFoundForEntityError(Exception):
    pass





class ImageLoader:
    @staticmethod
    def load_image(sritesheet : py.surface.Surface, x) -> py.surface.Surface:
        
        image = py.Surface([ENTITY_WIDTH, ENTITY_HEIGHT])
        image.set_colorkey(BLACK)
        image.blit(sritesheet, (0, 0), (x, 0, ENTITY_WIDTH, ENTITY_HEIGHT))
        
        return image
    
    @classmethod
    def load_images(cls, image_path : str) -> dict[Directions, py.surface.Surface]:
        loaded_image = py.image.load(image_path).convert_alpha()
        images : dict[Directions, py.surface.Surface] = {}
        for index, direction in enumerate([Directions.RIGHT, Directions.UP, Directions.LEFT, Directions.DOWN]):
            image = cls.load_image(loaded_image, index * ENTITY_WIDTH)
            images[direction] = image
           
        return images



class EntityAnimations:
    def __init__(self, spritesheet_path : str) -> None:
        self.spritesheet = py.image.load(spritesheet_path).convert_alpha()
        self.animation_index = 0
        self.animation_speed = 1.5
        self.clock = 0.0
        
        self.image : Optional[py.surface.Surface] = None
        
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
        
    
    def change_animation(self, animation : Animations):
        self.image = self.animations[animation][self.animation_index]
        self.clock += self.animation_speed * 8
        
        if self.clock >= 100:
            self.animation_index += 1
            
            if self.animation_index >= len(self.animations[animation]):
                self.animation_index = 0
                
            self.clock = 0
            
        
    def load_images(self, y : int, start_x : int, end_x : int) -> list[py.surface.Surface]:
        images : list[py.surface.Surface] = []
        for x in range(start_x, end_x):
            image = self.load_image(x*ENTITY_WIDTH, y)
            images.append(image)
            
        return images
    
    def load_image(self, x : int, y : int):
        image = py.Surface([ENTITY_WIDTH, ENTITY_HEIGHT])
        image.set_colorkey(BLACK)
        image.blit(self.spritesheet, (0, 0), (x, y, ENTITY_WIDTH, ENTITY_HEIGHT))
        return image



class Entity(py.sprite.Sprite):
    def __init__(self, x : int, y : int, image_path : str, speed : int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        
        self.coords = py.Vector2(self.x, self.y)
        
        self.images = ImageLoader.load_images(image_path)
        self.image = py.surface.Surface([ENTITY_WIDTH, ENTITY_HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.topleft = (int(self.coords.x), int(self.coords.y))
        
        self.animations = EntityAnimations(image_path)
        
        self.direction = Directions.RIGHT
        
        self.moving = False
        
        
    def idling(self, direction : Directions) -> None:
        idling_directions = {
            Directions.RIGHT: Animations.IDLE_RIGHT,
            Directions.UP: Animations.IDLE_UP,
            Directions.LEFT: Animations.IDLE_LEFT,
            Directions.DOWN: Animations.IDLE_DOWN
            
        }
        
        self.animations.change_animation(idling_directions[direction])
        
    
    def update(self, screen : py.surface.Surface) -> None:
        pass
        
    def draw(self, screen : py.surface.Surface) -> None:
        if self.image is None:
            raise ImageNotFoundForEntityError("No image found for entity")
        
        if self.rect is None:
            self.rect = self.image.get_rect()
        
        if self.animations.image is not None:
            screen.blit(self.animations.image, self.rect)
        py.draw.rect(screen, (255, 0, 0), self.rect, 1)
        
    
            
    
    
