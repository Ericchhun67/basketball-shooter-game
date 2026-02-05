# draw_text.py
import pygame
from config.setting import FONT_NAME


def draw_text(
        surface,
        text,
        x,
        y,
        color=(255, 255, 255),
        font_size=32,
        center=False
    ):
    """
    Renders text on the screen.

    surface: pygame screen
    text: string to draw
    x, y: position
    color: text color
    font_size: size of font
    center: if True, text is centered at (x, y)
    """

    font = pygame.font.SysFont(FONT_NAME, font_size)
    render = font.render(text, True, color)

    rect = render.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    surface.blit(render, rect)