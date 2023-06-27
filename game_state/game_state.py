from objects import pygame, os, random, MovingObject, Object
from game_screen.screen_object import WIN, WIDTH, HEIGHT
import copy
from mouse_cursor.mouse_object import MouseObject
from mouse_cursor.mouse_data import mouse_data
from helper.__function_tracker import run_once
from game_screen.text import Text

class GameStateObject(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.board = None
        self.timer = None
        self.player_groups = pygame.sprite.Group()
        
        # self.global_data = {
        #     "board": self.board,
        #     "timer": self.timer,
        #     "player_groups": self.player_groups
        # }
        
    @run_once
    def generate_player(self):
        from player.player_object import PlayerObject
        
        for _ in range(2):
            player = PlayerObject()
            
            if _ == 0:
                player.player_turn = True
                player.piece = "x"
                player.piece_image = ["x_piece.png"]
            else:
                player.player_turn = False
                player.piece = "o"
                player.piece_image = ["o_piece.png"]
            
            self.player_groups.add(player)
            
               
    @run_once      
    def generate_board(self):
        from board.board import BoardObject
        
        self.board = BoardObject()
        self.board.generate_board(self.board, self.player_groups)
        
    def control_right_click(self, players, board):
        pass

    
    def congrat_winner(self):
        congrat_text = Text(
            width = 200,
            height = 40,
            size = 25,
            pos_x = self.window.get_width() // 2 - 200 // 2,
            pos_y = self.window.get_height() // 2 - 40 // 2,
            surface = self.window
        )
        
        for player in self.player_groups.sprites():
            if player.win:
                pygame.draw.rect(
                    self.window,
                    (123, 32, 12),
                    pygame.Rect(
                        self.window.get_width() // 2 - 200 // 2,
                        self.window.get_height() // 2 - 40 // 2,
                        200,
                        40
                    )
                )
                
                congrat_text.text = f"Player {player.piece.upper()} Won!"
                congrat_text.display_text()   
                     
       
    def update(self): 
        self.generate_board()
        self.generate_player()
        
        if self.board and not any([player.win for player in self.player_groups.sprites()]):
            self.board.update()
            
        self.player_groups.update()
        
        self.congrat_winner()
            
            

        
                    
        