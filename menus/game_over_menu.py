# game_over_menu.py
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


class GameOverMenu:
    """Displays final score and Restart/Quit options."""

    def __init__(self, screen):
        self.screen = screen

        # Load background for game over (optional)
        bg_path = Path(asset_path("images", "game_over_bg.png"))
        if not bg_path.exists():
            bg_path = Path(asset_path("images", "bg_img.png"))
        self.bg_image = pygame.image.load(str(bg_path)).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))

        # Buttons
        button_w, button_h = 240, 70
        center_x = WIDTH // 2 - button_w // 2

        self.restart_button = Button(
            "RESTART",
            center_x,
            HEIGHT // 2,
            button_w,
            button_h,
            (0, 200, 0),
            (0, 255, 0)
        )

        self.quit_button = Button(
            "QUIT",
            center_x,
            HEIGHT // 2 + 120,
            button_w,
            button_h,
            (180, 0, 0),
            (255, 0, 0)
        )

    def run(self, final_score):
        """Main loop for game-over screen."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Draw background
            self.screen.blit(self.bg_image, (0, 0))

            # Title
            draw_text(
                self.screen,
                "Game Over",
                WIDTH // 2,
                HEIGHT // 4,
                center=True,
                font_size=72,
                color=WHITE
            )

            # Final score
            draw_text(
                self.screen,
                f"Score: {final_score}",
                WIDTH // 2,
                HEIGHT // 3,
                center=True,
                font_size=48,
                color=WHITE
            )

            # Buttons
            self.restart_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            # Logic
            if self.restart_button.is_clicked():
                return "restart"

            if self.quit_button.is_clicked():
                return "quit"

            pygame.display.update()
