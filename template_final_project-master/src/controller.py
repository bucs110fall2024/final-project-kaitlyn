import pygame
import pygame_menu
from imagebutto_model import ImageButton
from order import Order


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.width, self.height = pygame.display.get_window_size()
        self.state = "START"
        
        self.order = Order()
        self.buttons = [
            ImageButton("../assets/sea_plate.png", 50, 100, 500, 500),
            ImageButton("../assets/rice_plate.png", 50, 50, 500, 500),
            ImageButton("../assets/salmon_plate.png", 10, 50, 500, 500),
            ImageButton("../assets/mentaiko_plate.png", 10, 60, 500, 500),
            ImageButton("../assets/plum_plate.png", 10, 70, 500, 500),
            ImageButton("../assets/temp_plate.png", 10, 80, 500, 500),
            ImageButton("../assets/done_button.png", 50, 125, 500, 500)  
        ]
        
        self.grey = (128,128,128)
        self.plate_image = pygame.image.load("../assets/plate.png")
        self.plate_image = pygame.transform.scale(self.plate_image, (500,500)) #size of image
        
        #rice and seaweed load
        self.food_images = {
            "sea_plate": pygame.image.load("../assets/seaweed.png"),
            "rice_plate": pygame.image.load("../assets/rice_triangle.png"),
        }
        
        # together images/onigiris
        self.composite_image = {
            ("rice_plate", "sea_plate"):
                pygame.image.load("../assets/plain_onigiri.png"),
            ("rice_plate", "sea_plate", "mentaiko_plate"):
                pygame.image.load("../assets/mentaiko_onigiri.png"),
            ("rice_plate", "sea_plate", "plum_plate.png"):
                pygame.image.load("../assets/plum_onigiri.png"),
            ("rice_plate", "sea_plate", "salmon_plate.png"):
                pygame.image.load("../assets/salmon_onigiri.png"),
            ("rice_plate", "sea_plate", "temp_plate.png"):
                pygame.image.load("../assets/tempura_onigiri.png")
        }
        
        self.player_selections = []
        self.menu = pygame_menu.Menu("Start Screen", self.width-20, self.height/2)
        self.menu.add.label("Click Anywhere to Start the Game", max_char=-1, font_size=14)
        self.menu.add.button('Start', self.start_game, align=pygame_menu.locals.ALIGN_CENTER)

    def mainloop(self):
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()

    def startloop(self):
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
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
                    
            self.screen.fill(self.grey)
            self.screen.blit(msg, (10, 10))
            pygame.display.flip()

    def gameloop(self):
        current_order = self.order.generate_order()
        correct_combination = self.order.get_correct_combination()
        font = pygame.font.Font(None, 36)
        order_text = font.render(current_order, True, (255, 255, 255))
        incorrect_text = font.render("Incorrect item! Try again.", True, (255, 0, 0))
        correct_text = font.render("Correct!", True, (0, 255, 0))

        
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'END'
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    for button in self.buttons:
                        if button.is_clicked(event):
                            food_item = button.image_path.split('/')[-1].split('.')[0]
                        if button.image_path == "../assets/done_button.png":
                            if self.check_combination(self.player_selections, correct_combination):
                                self.screen.blit(correct_text, (10, 50))
                            else:
                                self.screen.blit(incorrect_text, (10, 50))
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            self.state = "END"
                        else:
                            self.player_selections.append(food_item)
                            print(f"Player selected: {food_item}")
                            if self.check_combination(self.player_selections, correct_combination):
                                self.state = "END"
                            elif len(self.player_selections) == len(correct_combination):
                                if not self.check_combination(self.player_selections, correct_combination):
                                    self.screen.blit(incorrect_text, (10, 50))
                                    pygame.display.flip()
                                    pygame.time.wait(2000)
                                    self.player_selections = []

            
            self.screen.fill((self.grey))
            self.screen.blit(order_text, (10, 10))
            
            self.screen.blit(self.plate_image, (450,100)) #position for image
            
            composite_key = tuple(sorted(self.player_selections))
            if composite_key in self.composite_image:
                self.screen.blit(self.composite_image[composite_key], (150,50))
            else:
                for i, food_item in enumerate(self.player_selections):
                    if food_item in self.food_images:
                        self.screen.blit(self.food_images[food_item], (150 + i * 100,50))
            
            for button in self.buttons:
                button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

    def check_combination(self, player_selections, correct_combination):
        return tuple(player_selections) == correct_combination

    def start_game(self):
        self.state = "GAME"
        self.player_selections = []
        
def main():
    game = Controller()
    game.mainloop()

if __name__ == "__main__":
    main()
