from typing import Optional
import pygame as py


class ImageNotFoundForEntityError(Exception):
    pass


class ImageLoader:
    @staticmethod
    def load_images(image_path : str) -> dict[str, py.surface.Surface]:
        loaded_image = py.image.load(image_path).convert_alpha()
        images : dict[str, py.surface.Surface] = {}
        for index, direction in enumerate(["right", "up", "left", "down"]):
            image = py.Surface([32, 64])
            image.set_colorkey((0, 0, 0))
            image.blit(loaded_image, (0, 0), (index*32, 0, 32, 64))
            images[direction] = image
           
        return images


class Entity(py.sprite.Sprite):
    def __init__(self, x : int, y : int, image_path : str) -> None:
        super().__init__()
        self.x = x
        self.y = y
        
        self.coords = py.Vector2(self.x, self.y)
        
        self.images = ImageLoader.load_images(image_path)
        self.image = py.surface.Surface([30, 46])
        self.rect = self.image.get_rect()
        
        self.direction = "right"
        
    
    def update(self, screen : py.surface.Surface) -> None:
        self.draw(screen)
        
    def draw(self, screen : py.surface.Surface) -> None:
        if self.image is None:
            raise ImageNotFoundForEntityError("No image found for entity")
        screen.blit(self.images[self.direction], self.coords)
        
    def move(self):
        pass
    
    
