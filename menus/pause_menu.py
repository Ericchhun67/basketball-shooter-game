# pause_menu.py
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


class PauseMenu:
    """Pause screen with Resume / Quit options."""

    def __init__(self, screen):
        self.screen = screen

        # Optional dim overlay (makes the background darker)
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(160)  # transparency
        self.overlay.fill((0, 0, 0))

        # Buttons
        button_w, button_h = 240, 70
        center_x = WIDTH // 2 - button_w // 2

        self.resume_button = Button(
            "RESUME",
            center_x,
            HEIGHT // 2 - 60,
            button_w,
            button_h,
            (0, 140, 255),
            (0, 180, 255)
        )

        self.quit_button = Button(
            "QUIT",
            center_x,
            HEIGHT // 2 + 60,
            button_w,
            button_h,
            (180, 0, 0),
            (255, 0, 0)
        )

    def run(self):
        """Run the pause menu loop and return selected action."""
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # ESC or P also resumes the game
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_p, pygame.K_ESCAPE):
                        return "resume"

            # Draw overlay
            self.screen.blit(self.overlay, (0, 0))

            # Title
            draw_text(
                self.screen,
                "Paused",
                WIDTH // 2,
                HEIGHT // 4,
                center=True,
                font_size=64,
                color=WHITE
            )

            # Draw buttons
            self.resume_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            # Logic
            if self.resume_button.is_clicked():
                return "resume"

            if self.quit_button.is_clicked():
                return "quit_to_menu"

            pygame.display.update()
