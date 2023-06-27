from objects import pygame, os, random, MovingObject, Object
from game_screen.screen_object import WIN, WIDTH, HEIGHT
import copy
from mouse_cursor.mouse_object import MouseObject
from mouse_cursor.mouse_data import mouse_data
from helper.__function_tracker import run_once


class BoardObject(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.pos_x = 0
        self.pos_y = 0
        # self.rect.x = 0
        # self.rect.y = 0
        self.width_grids = 15
        self.height_grids = 15
        self.grids = []
        self.tiles_group = pygame.sprite.Group()
    
    @run_once 
    def generate_board(self, board, players):
        for x in range(self.width_grids):
            self.grids.append([])
            
            for y in range(self.height_grids):
                grid = TileObject()
                grid.pos_x = x * grid.width
                grid.pos_y = y * grid.height
                grid.board = board
                grid.players = players
                grid.coor = (x, y)
                
                self.tiles_group.add(grid)
                self.grids[x].append("")
                
        print(len(self.grids))
        
    def check_win_condition(self, tile_coor, piece):  
        # check diagonal line
        return any([
            self.check_row(tile_coor, piece),
            self.check_col(tile_coor, piece),
            self.check_right_dia(tile_coor, piece),
            self.check_left_dia(tile_coor, piece)
        ])
        
    def check_row(self, tile_coor, piece):
        row = 1
        x_l, y_l, stop_l = tile_coor[0], tile_coor[1], True
        x_r, y_r, stop_r = tile_coor[0], tile_coor[1], True
        
        # check row
        while stop_l or stop_r:
            if stop_l:
                x_l -= 1
                
                if x_l >= 0: 
                    if self.grids[x_l][y_l] == piece:
                        row += 1
                    else:
                        stop_l = False
                else:
                    stop_l = False
                        
            if stop_r:
                x_r += 1
                    
                if x_r < self.width_grids:
                    if self.grids[x_r][y_r] == piece:
                        row += 1
                    else:
                        stop_r = False
                else:
                    stop_r = False
                    
        if row == 5:
            return True
        
        return False
                
    def check_col(self, tile_coor, piece):
        col = 1
        x_l, y_l, stop_l = tile_coor[0], tile_coor[1], True
        x_r, y_r, stop_r = tile_coor[0], tile_coor[1], True
        
        while stop_l or stop_r:
            if stop_l:
                y_l -= 1
                
                if y_l >= 0 and self.grids[x_l][y_l] == piece:
                    col += 1
                else:
                    stop_l = False
                        
            if stop_r:
                y_r += 1
                
                if y_r < self.height_grids and self.grids[x_r][y_r] == piece:
                    col += 1
                else:
                    stop_r = False
                        
        if col == 5:
            return True

        return False
                                
    def check_right_dia(self, tile_coor, piece):
        right_dia = 1
        x_l, y_l, stop_l = tile_coor[0], tile_coor[1], True
        x_r, y_r, stop_r = tile_coor[0], tile_coor[1], True
        
        while stop_l or stop_r:
            if stop_l:
                x_l, y_l = x_l + 1, y_l - 1
                
                if x_l < self.width_grids and y_l >= 0 and self.grids[x_l][y_l] == piece:
                    right_dia += 1
                else:
                    stop_l = False
                    
            if stop_r:
                x_r, y_r = x_r - 1, y_r + 1        
                        
                if x_r >= 0 and y_r < self.height_grids and self.grids[x_r][y_r] == piece:
                    right_dia += 1
                else:
                    stop_r = False
                    
        if right_dia == 5:
            return True
        
        return False
                      
    def check_left_dia(self, tile_coor, piece):
        left_dia = 1
        x_l, y_l, stop_l = tile_coor[0], tile_coor[1], True
        x_r, y_r, stop_r = tile_coor[0], tile_coor[1], True
        
        while stop_l or stop_r:
            if stop_l:
                x_l, y_l = x_l - 1, y_l - 1
                
                if x_l >= 0 and y_l >= 0 and self.grids[x_l][y_l] == piece:
                    left_dia += 1
                else:
                    stop_l = False
                    
            if stop_r:
                x_r, y_r = x_r + 1, y_r + 1        
                        
                if x_r < self.height_grids and y_r < self.height_grids and self.grids[x_r][y_r] == piece:
                    left_dia += 1
                else:
                    stop_r = False
                    
        if left_dia == 5:
            return True
        
        return False
           
    def render_board(self):
        # self.tiles_group.draw(self.window)
        self.tiles_group.update()
               
    def update(self): 
        self.render_board()
        
        
class TileObject(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.pos_x = 0
        self.pos_y = 0
        # self.rect.x = 0
        # self.rect.y = 0
        self.height = 40
        self.width = 40
        self.source = "board/images"
        self.image = ["blank_tile.png"]
        self.image_changed = True
        
        self.coor = (0, 0)
        
        self.board = None
        self.players = None
        

    def on_click(self):

        left_click = pygame.mouse.get_pressed(3)[0]
        mouse_pos = pygame.mouse.get_pos()
        
        if left_click and self.rect.collidepoint(mouse_pos):
            if self.board and self.board.grids[self.coor[0]][self.coor[1]] == "":
                for player in self.players.sprites():
                    if player.player_turn:
                        self.board.grids[self.coor[0]][self.coor[1]] = player.piece
                        self.image = [player.piece_image[0]]
                        self.image_changed = True
                        if self.board.check_win_condition(self.coor, player.piece):
                            player.win = True
                        player.player_turn = False
                    else:
                        player.player_turn = True
     
        
    def update(self):
        self.handle_image()
        self.rendering_object()
        self.hitbox()
        self.update_positions()
        self.on_click()  

        
                    
        