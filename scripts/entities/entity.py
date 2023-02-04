from typing import Optional
import pygame as py


class ImageNotFoundForEntityError(Exception):
    pass


class ImageLoader:
    @staticmethod
    def load_image(image_path : Optional[str] = None) -> py.surface.Surface:
        if image_path is None:
            size = (50, 50)
            return py.Surface(size)
        
        return py.image.load(image_path)


class Entity(py.sprite.Sprite):
    def __init__(self, x : int, y : int, image_path : Optional[str] = None) -> None:
        super().__init__()
        self.x = x
        self.y = y
        
        self.coords = py.Vector2(self.x, self.y)
        
        self.image = ImageLoader.load_image(image_path)
        self.rect = self.image.get_rect()
        
    
    def update(self, screen : py.surface.Surface) -> None:
        self.draw(screen)
        
    def draw(self, screen : py.surface.Surface) -> None:
        if self.image is None:
            raise ImageNotFoundForEntityError("No image found for entity")
        screen.blit(self.image, self.coords)
        
    def move(self):
        pass
    
    
