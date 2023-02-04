import pygame as py

from entities import Player


class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 600))
        self.clock = py.time.Clock()
        self.entities = py.sprite.Group()
        
        self.player = Player(100, 100, "assets/player.png", 5)
        self.entities.add(self.player)
        
        
    def set_background(self) -> None:
        self.screen.fill((0, 140, 0))
        
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            
            self.set_background()
            
            for entity in self.entities:
                entity.update(self.screen)
            
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    
            
        py.quit()
            
            
            