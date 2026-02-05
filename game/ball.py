# ball.py
import math
from pathlib import Path

import pygame
from config.setting import (
    WIDTH,
    HEIGHT,
    GRAVITY,
    BALL_POWER_MULTIPLIER,
    BOUNCE_DAMPING,
    BALL_SIZE,
    MAX_DRAG_DISTANCE,
    ORANGE,
    BLACK,
)
from utils.paths import asset_path


def _looks_like_placeholder(surface):
    """Heuristic: detect very light (checker/white) corners -> likely placeholder."""
    w, h = surface.get_size()
    sample_points = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    light_count = 0

    for x, y in sample_points:
        r, g, b, a = surface.get_at((x, y))
        # Transparent corners mean it's probably a proper PNG.
        if a == 0:
            return False
        if r > 235 and g > 235 and b > 235:
            light_count += 1

    return light_count >= 3


def _make_ball_surface(size):
    """Fallback ball if the asset is missing or a placeholder."""
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    center = size // 2
    radius = center - 2

    pygame.draw.circle(surf, ORANGE, (center, center), radius)
    pygame.draw.circle(surf, BLACK, (center, center), radius, 3)

    # Add simple basketball lines
    pygame.draw.line(surf, BLACK, (center, 2), (center, size - 2), 3)
    arc_rect = surf.get_rect().inflate(-size * 0.2, -size * 0.2)
    pygame.draw.arc(surf, BLACK, arc_rect, math.radians(20), math.radians(160), 3)
    pygame.draw.arc(surf, BLACK, arc_rect, math.radians(200), math.radians(340), 3)

    return surf


class Ball:
    """Ball that the player shoots using mouse drag input."""

    def __init__(self, player):
        # Load ball sprite
        ball_path = Path(asset_path("images", "ball.png"))
        if ball_path.exists():
            loaded = pygame.image.load(str(ball_path)).convert_alpha()
            if _looks_like_placeholder(loaded):
                self.image = _make_ball_surface(BALL_SIZE)
            else:
                self.image = pygame.transform.smoothscale(loaded, (BALL_SIZE, BALL_SIZE))
        else:
            self.image = _make_ball_surface(BALL_SIZE)

        # Position starts at player origin
        self.rect = self.image.get_rect(center=(player.x, player.y))

        # 
        self.vel_x = 0
        self.vel_y = 0

        # Track player origin (reset point)
        self.player = player

        # Mouse input
        self.dragging = False
        self.start_drag_pos = (0, 0)
        self.current_drag_pos = (0, 0)
    # A method to start dragging the ball
    def start_drag(self, mouse_pos):
        """Called when player clicks to start aiming."""
        # Only start drag if mouse is over the ball
        self.dragging = True # set dragging to true to indicate ball is being 
        # dragged.
        self.start_drag_pos = mouse_pos # record the position where the drag
        # started.
        self.current_drag_pos = mouse_pos
    
    # A method to launch the ball based on mouse release position
    def launch(self, mouse_release_pos):
        """Shoot the ball based on drag distance + direction."""
        if not self.dragging: # if ball is not being dragged, do nothing
            return # then exit the mehthod.
            
        # calculate drag distance and the direction of the launch.
        dx = self.start_drag_pos[0] - mouse_release_pos[0]
        dy = self.start_drag_pos[1] - mouse_release_pos[1]

        # Clamp to max drag distance for consistent power
        dist = math.hypot(dx, dy)
        if dist > MAX_DRAG_DISTANCE and dist > 0:
            scale = MAX_DRAG_DISTANCE / dist
            dx *= scale
            dy *= scale

        # Scale the launch force
        self.vel_x = dx * BALL_POWER_MULTIPLIER
        self.vel_y = dy * BALL_POWER_MULTIPLIER
        # reset dragging state
        self.dragging = False
        self.current_drag_pos = mouse_release_pos

    def update(self):
        """Apply physics to the ball each frame."""
        # If ball is being dragged, position follows mouse
        if self.dragging:
            mx, my = pygame.mouse.get_pos()
            self.current_drag_pos = (mx, my)
            self.rect.center = (mx, my)
            return

        # Apply gravity
        self.vel_y += GRAVITY

        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce on ground
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y *= -BOUNCE_DAMPING

        # Reset if ball goes too far off screen
        if self.rect.top > HEIGHT + 200 or self.rect.right < -200 or self.rect.left > WIDTH + 200:
            self.reset()

    def draw(self, screen):
        """Draw the ball."""
        screen.blit(self.image, self.rect)

    def reset(self):
        """Reset ball back to the player origin."""
        self.rect.center = (self.player.x, self.player.y)
        self.vel_x = 0
        self.vel_y = 0
        self.dragging = False
        self.current_drag_pos = self.rect.center

    def get_power_ratio(self):
        """Return current shot power ratio [0..1] while dragging."""
        if not self.dragging:
            return 0.0
        dx = self.start_drag_pos[0] - self.current_drag_pos[0]
        dy = self.start_drag_pos[1] - self.current_drag_pos[1]
        dist = math.hypot(dx, dy)
        return min(dist / MAX_DRAG_DISTANCE, 1.0)
