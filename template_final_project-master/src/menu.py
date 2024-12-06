import pygame
import pygame_menu

class Controller: 
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        self.width, self.height = pygame.display.get_window_size()
        
        self.state = "START"
        self.button_rect = pygame.Rect(300, 400, 200, 50)
    
    def mainloop(self):
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            
    def startloop(self):
        self.menu = pygame_menu.Menu("Start Screen", self.width-20, self.height/2)
        self.menu.add.label("Click Anywhere to Start the Game", max_char=-1, font_size=14)
        self.menu.add.button(
            'Start',
            self.start_game,
            align=pygame_menu.locals.ALIGN_CENTER
        )
    
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "GAME"
            
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()
    
    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You may quit any time by closing the program", True, "yellow")
        
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
            self.screen.blit(msg, (10, 10))
            pygame.display.flip()
        
    def gameloop(self):  
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'END'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.state = "END"
                        
            self.screen.fill((0, 0, 0))  
            self.draw_button()  
            pygame.display.flip()  

        pygame.quit()
        
    def draw_button(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)
        font = pygame.font.Font(None, 50)
        text = font.render("End Game", True, (0, 0, 0))
        self.screen.blit(text, (self.button_rect.x + 20, self.button_rect.y + 10))

    def start_game(self):
        self.state = "GAME"

