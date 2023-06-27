from objects import pygame, os, random, MovingObject, Object
from game_screen.screen_object import WIN, WIDTH, HEIGHT
import copy
from mouse_cursor.mouse_object import MouseObject
from mouse_cursor.mouse_data import mouse_data
from helper.__function_tracker import run_once

class PlayerObject(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.player_turn = False
        self.mouse = MouseObject({**mouse_data})
        self.source = "player/images"
        self.piece = None
        self.piece_image = []
        self.win = False
     
    def update_mouse(self):
        self.mouse.update()
        
         
    def calculate_shortest_path(self):
        pass
        
    

    # moving characters
    def moving_object(self):
        # get mouse position
        mouse_coor = pygame.mouse.get_pos()
         
        pass
 

    def print_outline(self):
        while True:
            print(self.outline)
            break
               
    def update(self): 
        self.update_mouse()
        # self.update_positions()
        
    
            
            

        
                    
        