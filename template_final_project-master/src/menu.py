import pygame
import pygame_menu

class Controller: 
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        
        self.state = "START"
        
def mainloop(self):
    while True:
        if self.state == "START":
            self.startloop()
        elif self.state == "GAME":
            self.gameloop()
        elif self.state == "END":
            self.endloop()
            
def startloop(self):
    self.meu = pygame_menu.Menu("Start Screen", self.width-20, self.height/2)
    self.menu.add.label("Click Anywhere to Start the Game", max_char=-1, font_size=14)
    #NEED TO MAKE MY BUTTONS
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
    
    