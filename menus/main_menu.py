

# the main menu for the basketball shooter game
import sys
from pathlib import Path

# Ensure project root is on sys.path when running this file directly.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pygame
from config.setting import *
from utils.button import Button
from utils.draw_text import draw_text
from utils.paths import asset_path

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        
        # load and scale background image
        self.bg_image = pygame.image.load(asset_path("images", "bg_img.png")).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))
        # create buttons
        button_w, button_h = 240, 70
        center_x = WIDTH // 2 - button_w // 2
        
        self.play_button = Button("play", center_x, HEIGHT // 2 - 60, button_w,
                                    button_h, (0, 180, 0), (0, 255, 0))
                                    
        self.quit_button = Button("quit", center_x, HEIGHT // 2 + 60, 
            button_w, button_h, (180, 0, 0), (255, 0, 0))
    
    
    
    def run(self):
        """Run the main menu loop and return the next state."""
        menu_running = True

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Draw background
            self.screen.blit(self.bg_image, (0, 0))

            # Title text
            draw_text(
                self.screen,
                "Basketball Shooter",
                WIDTH // 2,
                HEIGHT // 4,
                center=True,
                font_size=64,
                color=WHITE
            )

            # Draw buttons
            self.play_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            # Button logic
            if self.play_button.is_clicked():
                return "start_game"

            if self.quit_button.is_clicked():
                pygame.quit()
                exit()

            pygame.display.update()
        
        
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    menu = MainMenu(screen)
    menu.run()
