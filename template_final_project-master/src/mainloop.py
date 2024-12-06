import pygame
from imagebutto_model import ImageButton
from order import Order

def mainloop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    order = Order()
    buttons = [
        ImageButton("sea_plate.png", 50, 400, 100, 100),
        ImageButton("rice_plate.png", 200, 400, 100, 100),
        ImageButton("salmon_plate.png", 350, 400, 100, 100),
        ImageButton("mentaiko_plate.png", 500, 400, 100, 100),
        ImageButton("plum_plate.png", 650, 400, 100, 100),
        ImageButton("temp_plate.png", 750, 400, 100, 100)  # Adjusted position
    ]
    
    player_selections = []
    
    state = "START"
    current_order = order.generate_order()
    correct_combination = order.get_correct_combination()
    font = pygame.font.Font(None, 36)
    order_text = font.render(current_order, True, (255, 255, 255))
    incorrect_text = font.render("Incorrect item! Try again.", True, (255, 0, 0))

    while state != "END":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'END'
            elif event.type == pygame.MOUSEBUTTONDOWN and state == "START":
                state = "GAME"
            elif state == "GAME":
                for button in buttons:
                    if button.is_clicked(event):
                        food_item = button.image_path.split('.')[0]
                        player_selections.append(food_item)
                        print(f"Player selected: {food_item}")
                        if check_combination(player_selections, correct_combination):
                            state = "END"
                        elif len(player_selections) == len(correct_combination):
                            if not check_combination(player_selections, correct_combination):
                                screen.blit(incorrect_text, (10, 50))
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                player_selections = []

        screen.fill((0, 0, 0))
        if state == "START":
            screen.blit(order_text, (10, 10))
        elif state == "GAME":
            screen.blit(order_text, (10, 10))
            for button in buttons:
                button.draw(screen)
        pygame.display.flip()

    pygame.quit()

def check_combination(player_selections, correct_combination):
    return tuple(player_selections) == correct_combination
