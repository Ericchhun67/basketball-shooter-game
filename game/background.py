# background.py
import pygame
from config.setting import WIDTH, HEIGHT
from utils.paths import asset_path

# A class to manage the background image and scrolling and drawing
class Background:
    """Handles the court background image and optional scrolling."""

    def __init__(self, screen):
        self.screen = screen

        # Load + scale background image
        self.image = pygame.image.load(asset_path("images", "bg_img.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))

        # Optional scrolling properties
        self.scroll_x = 0
        self.scroll_speed = 0  # set to >0 if you want camera-like motion

    def update(self):
        """Update background scrolling (optional)."""
        if self.scroll_speed > 0:
            self.scroll_x -= self.scroll_speed
            if self.scroll_x <= -WIDTH:
                self.scroll_x = 0

    def draw(self):
        """Draw the background to the screen."""
        # Static (non-scrolling)
        if self.scroll_speed == 0:
            self.screen.blit(self.image, (0, 0))
            return

        # Scrolling (draw twice for wrap effect)
        self.screen.blit(self.image, (self.scroll_x, 0))
        self.screen.blit(self.image, (self.scroll_x + WIDTH, 0))
