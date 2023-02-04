from typing import Optional
from entities import Entity



class Player(Entity):
    def __init__(self, x : int, y : int, image_path : Optional[str] = None) -> None:
        super().__init__(x, y, image_path)
        
        self.speed = 5