# button.py
import pygame
from config.setting import FONT_NAME, WHITE


class Button:
    """Simple rectangular button with hover and click detection."""

    def __init__(self, text, x, y, width, height, base_color, hover_color, text_color=WHITE, font_size=32):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font_size = font_size
        self._clicked = False

    def draw(self, surface):
        """Draw button with hover effect and centered text."""
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)

        font = pygame.font.SysFont(FONT_NAME, self.font_size)
        label = font.render(self.text, True, self.text_color)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    def is_clicked(self):
        """Return True once per click when mouse is over the button."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)[0]

        if self.rect.collidepoint(mouse_pos) and mouse_pressed:
            if not self._clicked:
                self._clicked = True
                return True
        else:
            self._clicked = False

        return False
