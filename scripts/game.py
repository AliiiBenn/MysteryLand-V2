import pygame as py

from entities import Player
from maps.maps import MapManager


def create_player(x : int, y : int, image_path : str, speed : int, group : py.sprite.Group) -> Player:
    player = Player(x, y, image_path, speed)
    group.add(player)
    return player


def add_new_entity(x : int, y : int, image_path : str, speed : int, entity_type ,group : py.sprite.Group) -> Player:
    entity = entity_type(x, y, image_path, speed)
    group.add(entity)
    return entity


class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 600))
        self.clock = py.time.Clock()
        self.entities = py.sprite.Group()
        
        self.player = create_player(400, 300, "assets/player.png", 5, self.entities)
        
        self.map_manager = MapManager(self.screen, self.player)
        
    
    def update(self) -> None:
        self.set_background()
        self.map_manager.update()    
        self.map_manager.draw()
        
        
    def set_background(self) -> None:
        self.screen.fill((0, 140, 0))
        
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            
            
            self.update()
            
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    
            
        py.quit()
            
            
            