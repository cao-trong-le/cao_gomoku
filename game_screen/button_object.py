import pygame

pygame.font.init()
# print(pygame.font.get_fonts())

class Button:
    def __init__(
            self, 
            text: str = "", 
            size: int = 10, 
            font: str = "freesansbold.ttf",
            color = (0, 0, 0),
            background = (255, 255, 255),
            source = "game_screen/images",
            image = None,
            bold: bool = False,
            italic: bool = False,
            pos_x: int = 0, 
            pos_y: int = 0,
            width: int = 0,
            height: int = 0,
            surface = None
        ):
        
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font, self.size)
        self.color = color
        self.bg_color = background
        self.source = source
        self.image = image
        self.bold = bold
        self.italic = italic
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.surface = surface
        
    def button_hitbox(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        
    def draw_button(self):
        pygame.draw.rect(self.surface, self.bg_color, self.button_hitbox())
        
        if self.text != None:
            self.draw_text()
            
    def draw_text(self):
        text_surf = self.font.render(self.text, True, self.color, self.bg_color)
        text_rect = text_surf.get_rect(topleft=(self.pos_x + 10, self.pos_y + 10))
        self.surface.blit(text_surf, text_rect)
        
    def draw_image(self):
        pass
        
    def hovering_effect(self):
        pass
    
    def button_on_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_hitbox().collidepoint(event.pos):
                print("OK")
                return True
        return False
    