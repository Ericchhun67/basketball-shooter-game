# hoop.py
from pathlib import Path

import pygame
from config.setting import WIDTH, HOOP_SPEED, HOOP_SIZE, ORANGE, BLACK, WHITE, RED
from utils.paths import asset_path


def _looks_like_placeholder(surface):
    """Heuristic: detect very light (checker/white) corners -> likely placeholder."""
    w, h = surface.get_size()
    sample_points = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    light_count = 0

    for x, y in sample_points:
        r, g, b, a = surface.get_at((x, y))
        if a == 0:
            return False
        if r > 235 and g > 235 and b > 235:
            light_count += 1

    return light_count >= 3


def _has_transparency(surface, step=24):
    """Check if the surface has any transparent pixels."""
    w, h = surface.get_size()
    for y in range(0, h, step):
        for x in range(0, w, step):
            if surface.get_at((x, y)).a < 250:
                return True
    return False


def _is_light(color):
    r, g, b = color
    return r + g + b >= 680


def _remove_checker_bg(surface, tolerance=8):
    """Remove a light checkerboard background if present."""
    w, h = surface.get_size()
    sample_points = [ # corners + near-corners and edges points
        (0, 0),
        (w - 1, 0),
        (0, h - 1),
        (w - 1, h - 1),
        (5, 5),
        (w - 6, 5),
        (5, h - 6),
        (w - 6, h - 6),
    ]

    samples = [] # set a empty list to hold sampled colors and check for transparency
    for x, y in sample_points:
        r, g, b, a = surface.get_at((x, y))
        if a == 0:
            return surface  # already transparent
        samples.append((r, g, b))

    # Require at least two distinct light colors to avoid nuking white backboards.
    unique_samples = list({c for c in samples})
    if len(unique_samples) < 2 or not all(_is_light(c) for c in unique_samples):
        return surface

    result = surface.convert_alpha()
    result.lock()
    for y in range(h):
        for x in range(w):
            r, g, b, a = result.get_at((x, y))
            if a == 0:
                continue
            for sr, sg, sb in unique_samples:
                if (
                    abs(r - sr) <= tolerance
                    and abs(g - sg) <= tolerance
                    and abs(b - sb) <= tolerance
                ):
                    result.set_at((x, y), (r, g, b, 0))
                    break
    result.unlock()
    return result


def _make_hoop_surface(size):
    """Fallback hoop/backboard if the asset is missing or a placeholder."""
    surf = pygame.Surface((size, size), pygame.SRCALPHA)

    # Backboard
    board = pygame.Rect(size * 0.1, size * 0.1, size * 0.8, size * 0.6)
    pygame.draw.rect(surf, WHITE, board, border_radius=10)
    pygame.draw.rect(surf, RED, board, width=8, border_radius=10)

    inner = board.inflate(-size * 0.25, -size * 0.25)
    pygame.draw.rect(surf, WHITE, inner, border_radius=8)
    pygame.draw.rect(surf, RED, inner, width=6, border_radius=8)

    # Rim
    rim = pygame.Rect(size * 0.28, size * 0.68, size * 0.44, size * 0.12)
    pygame.draw.ellipse(surf, ORANGE, rim)
    pygame.draw.ellipse(surf, BLACK, rim, 3)

    return surf


class Hoop:
    """Hoop + backboard sprite that moves horizontally and contains a score zone."""

    SCORE_ZONE_Y = 0.70
    SCORE_ZONE_W = 0.28
    SCORE_ZONE_H = 0.035

    def __init__(self, x, y):
        # Load hoop image + backboard image with transparency handled
        hoop_path = Path(asset_path("images", "Hoop+backboard.png"))
        if hoop_path.exists():
            loaded = pygame.image.load(str(hoop_path)).convert_alpha()
            if _looks_like_placeholder(loaded) or not _has_transparency(loaded):
                self.image = _make_hoop_surface(HOOP_SIZE)
            else:
                scaled = pygame.transform.smoothscale(loaded, (HOOP_SIZE, HOOP_SIZE))
                self.image = _remove_checker_bg(scaled)
        else:
            self.image = _make_hoop_surface(HOOP_SIZE)

        # Position + movement speed
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = HOOP_SPEED # set horizontal speed

        # Define scoring zone rectangle
        self._update_score_zone()

    def _update_score_zone(self):
        zone_w = int(self.rect.width * self.SCORE_ZONE_W)
        zone_h = max(6, int(self.rect.height * self.SCORE_ZONE_H))
        zone_x = self.rect.centerx - zone_w // 2
        zone_y = self.rect.y + int(self.rect.height * self.SCORE_ZONE_Y)
        self.score_zone = pygame.Rect(zone_x, zone_y, zone_w, zone_h)
    # A method to update hoop position of the hoop
    def update(self):
        """Move hoop side to side and update score zone position."""
        self.rect.x += self.speed # move hoop horizontally

        # Bounce off left/right edges
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.speed *= -1 # reverse direction
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.speed *= -1

        # Keep score zone locked to hoop
        self._update_score_zone()
        
    # A method to draw the hoop
    def draw(self, screen):
        """Draw hoop on the screen."""
        screen.blit(self.image, self.rect)
        # draw score zone
        pygame.draw.rect(screen, (0, 255, 0), self.score_zone, 2)
    
    # A method to reset hoop position
    def reset(self):
        """Reset hoop to the center or any default position."""
        self.rect.midtop = (WIDTH // 2, self.rect.y)
        self.speed = HOOP_SPEED
        self._update_score_zone()
