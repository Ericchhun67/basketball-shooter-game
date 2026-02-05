# player.py
from pathlib import Path

import pygame
from config.setting import WIDTH, HEIGHT, ORANGE
from utils.paths import asset_path

# Player class to manage the launch position for shooting the ball
class Player:
    """Player launch position for shooting the ball."""

    def __init__(self):
        # Starting launcher position
        self.x = WIDTH // 2
        self.y = HEIGHT - 80   # slightly above bottom of screen

        # Optional small sprite or marker to show launch point
        marker_path = Path(asset_path("images", "player_marker.png"))
        if marker_path.exists():
            self.image = pygame.image.load(str(marker_path)).convert_alpha()
        else:
            # Fallback: draw a simple marker so the game still runs without the asset
            self.image = pygame.Surface((36, 36), pygame.SRCALPHA)
            pygame.draw.circle(self.image, ORANGE, (18, 18), 16)
            pygame.draw.circle(self.image, (255, 255, 255), (18, 18), 16, 2)

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        """Draw the player’s launch point."""
        screen.blit(self.image, self.rect)

    def update(self):
        """If you later want moving launch positions, handle here."""
        pass
