import pygame as py



class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 600))
        self.clock = py.time.Clock()
        
        
    def set_background(self) -> None:
        self.screen.fill((0, 140, 0))
        
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            
            self.set_background()
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    
            
        py.quit()
            
            
            