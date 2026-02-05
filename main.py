import sys
from pathlib import Path

# Ensure project root is on sys.path when running from outside the folder.
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pygame

from config.setting import WIDTH, HEIGHT, FPS, TITLE

# menu imports
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from menus.game_over_menu import GameOverMenu

from game.game_manager import GameManager
success, failure = pygame.init()
print(f"init:{success}, failed: {failure}")

# handle pygame init errors
try:
    # set up the game window
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    # set window title
    pygame.display.set_caption(TITLE)
    # set window icon app
    
    # set up the clock for FPS
    clock = pygame.time.Clock()
except Exception as e:
    # display error message and exit
    print(f"Error during pygame init: {e}")
    sys.exit()
    
    
# Game States to manage different screens
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"    
    
    
    
def main():
    # initialize game components to manage different states
    main_menu = MainMenu(SCREEN)
    pause_menu = PauseMenu(SCREEN)
    game_over = GameOverMenu(SCREEN)
    game_manager = GameManager(SCREEN)

  

    state = STATE_MENU # start at main menu to begin the game loop 
    running = True # Set running to true to start the game loop
    
    while running:
        # handle global events (quit, pause, shooting triggered in manager)
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                running = False 
                sys.exit()
                
            # gameplay shooting handle
            if state == STATE_PLAYING:
                # handle shooting events 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # start shot charge and aim using mouse position
                    game_manager.handle_shot_start(event.pos)
                # release to shoot
                if event.type == pygame.MOUSEBUTTONUP:
                    game_manager.handle_shot_release(event.pos)
                # handle pause event
                if event.type == pygame.KEYDOWN:
                    # press P to pause the game
                    if event.key == pygame.K_p:
                        print("Game Paused")
                        state = STATE_PAUSED
        
        # menu statements
        if state == STATE_MENU:
            # display main menu
            next_state = main_menu.run()
            # check for state change and reset game if starting new game
            if next_state == "start_game":
                # reset game state for new game
                game_manager.reset()
                state = STATE_PLAYING
        
        elif state == STATE_PLAYING:
            # update and draw game elements
            time_up = game_manager.run()
            if time_up:
                state = STATE_GAME_OVER
            
        # Pause state handled in event loop
        elif state == STATE_PAUSED:
            # display pause menu
            next_state = pause_menu.run()
            if next_state == "resume":
                game_manager.resume_timer()
                state = STATE_PLAYING
            elif next_state == "quit_to_menu":
                state = STATE_MENU
        
        elif state == STATE_GAME_OVER:
            next_state = game_over.run(game_manager.score)
            if next_state == "restart":
                game_manager.reset()
                state = STATE_PLAYING
            elif next_state == "quit":
                state = STATE_MENU
        
        # flip display + limit FPS
        pygame.display.flip()
        clock.tick(FPS)
            

if __name__ == "__main__":
    main()
