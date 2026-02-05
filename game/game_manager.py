

import pygame
from config.setting import *
from utils.draw_text import draw_text
from game.ball import Ball
from game.hoop import Hoop
from game.player import Player
from game.background import Background


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(screen)
        self.player = Player()
        self.ball = Ball(self.player)
        self.hoop = Hoop(WIDTH // 2, 80)
        # score
        self.score = 0 
        # timer
        self.timer_start_ms = TIMER_START_SECONDS * 1000
        self.remaining_ms = self.timer_start_ms
        self.last_tick = pygame.time.get_ticks()
        self.time_up = False
        
    
    def reset(self):
        """ Reset the game state for a new game."""
        self.score = 0
        self.ball.reset()
        self.hoop.reset()
        self.remaining_ms = self.timer_start_ms
        self.last_tick = pygame.time.get_ticks()
        self.time_up = False
    
    def update(self):
        """ Update all game elements game objects."""
        self._update_timer()
        if self.time_up:
            return
        self.hoop.update()
        
        # update ball physics only if in motion
        self.ball.update()
        
        # check for scoring zone collision
        self.check_score_collision()

    def _update_timer(self):
        now = pygame.time.get_ticks()
        dt = now - self.last_tick
        self.last_tick = now
        if self.remaining_ms > 0:
            self.remaining_ms = max(0, self.remaining_ms - dt)
        if self.remaining_ms <= 0:
            self.time_up = True

    def resume_timer(self):
        """Sync timer after a pause so time doesn't jump."""
        self.last_tick = pygame.time.get_ticks()
    
    def check_score_collision(self):
        """ check if the ball is passes through the hoop"""
        if self.ball.rect.colliderect(self.hoop.score_zone):
            # increase score
            self.score += 1
            # reset ball position
            self.ball.reset()
    
    def draw(self):
        """ Draw all game elements on the screen."""
        self.background.draw()
        self.player.draw(self.screen)
        self.hoop.draw(self.screen)
        self.ball.draw(self.screen)

        # Aim guide + power meter
        power_ratio = self.ball.get_power_ratio()
        if self.ball.dragging:
            pygame.draw.line(
                self.screen,
                AIM_GUIDE_COLOR,
                self.ball.start_drag_pos,
                self.ball.current_drag_pos,
                AIM_GUIDE_WIDTH,
            )

        bar_x, bar_y = POWER_METER_POS
        bar_w, bar_h = POWER_METER_SIZE
        pygame.draw.rect(self.screen, POWER_METER_BG, (bar_x, bar_y, bar_w, bar_h))
        fill_w = int(bar_w * power_ratio)
        if fill_w > 0:
            pygame.draw.rect(self.screen, POWER_METER_FILL, (bar_x, bar_y, fill_w, bar_h))
        pygame.draw.rect(self.screen, POWER_METER_BORDER, (bar_x, bar_y, bar_w, bar_h), 2)
        draw_text(
            self.screen,
            "Power",
            bar_x,
            bar_y - 22,
            color=WHITE,
            font_size=POWER_METER_FONT_SIZE,
        )

        # Timer (top right)
        total_seconds = max(0, (self.remaining_ms + 999) // 1000)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_text = f"{minutes:02d}:{seconds:02d}"
        timer_font = pygame.font.SysFont(FONT_NAME, TIMER_FONT_SIZE)
        timer_surf = timer_font.render(time_text, True, TIMER_COLOR)
        timer_rect = timer_surf.get_rect()
        timer_rect.topright = (WIDTH - TIMER_MARGIN, TIMER_MARGIN)
        self.screen.blit(timer_surf, timer_rect)

        draw_text(
            self.screen,
            f"Score: {self.score}",
            20, 20,
            color=WHITE,
            font_size=SCORE_FONT_SIZE
        )

    def run(self):
        """Main update loop called from main.py"""
        self.update()
        self.draw()
        return self.time_up

    def handle_shot_start(self, mouse_pos):
        """Begin aiming the shot."""
        self.ball.start_drag(mouse_pos)

    def handle_shot_release(self, mouse_pos):
        """Launch the ball."""
        self.ball.launch(mouse_pos)
        
