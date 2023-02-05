from dataclasses import dataclass
import pygame as py
import pytmx, pyscroll

from entities.player import Player



@dataclass
class Map:
    name : str
    walls : list
    group : pyscroll.group.PyscrollGroup
    tmx_data : pytmx.TiledMap
    
    
class MapGetter:
    @staticmethod
    def get(maps : dict[str, Map], name : str) -> Map:
        return maps[name]
    
    
    
class MapManager:
    def __init__(self, screen : py.surface.Surface, player : Player) -> None:
        self.screen = screen
        self.player = player
        
        self.maps : dict[str, Map] = {}
        self.current_map = "world"
        
        self.register_map("world")
        
        
    def update(self) -> None:
        self.get_group().update()
        
        
    def register_map(self, name : str) -> None:
        tmx_data = pytmx.load_pygame(f"maps/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 1.5
        
        group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=0)
        
        group.add(self.player)
        
        self.maps[name] = Map(name, [], group, tmx_data)
        
        
    def get_map(self) -> Map:
        return self.maps[self.current_map]
    
    def get_group(self) -> pyscroll.PyscrollGroup:
        return self.get_map().group
    
    def draw(self) -> None:
        self.get_group().draw(self.screen)
        
        if self.player.rect is None:
            return
        self.get_group().center(self.player.rect.center)