from typing import Optional
import pygame as py

from .directions import Directions

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
        
        self.direction = Directions.RIGHT
        
    
    def update(self, screen : py.surface.Surface) -> None:
        self.draw(screen)
        
    def draw(self, screen : py.surface.Surface) -> None:
        if self.image is None:
            raise ImageNotFoundForEntityError("No image found for entity")
        
        if self.rect is None:
            self.rect = self.image.get_rect()
        
        screen.blit(self.images[self.direction], self.rect)
        py.draw.rect(screen, (255, 0, 0), self.rect, 1)
        
    
            
    
    
