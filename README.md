Basketball Shooter 🏀
A fun, arcade-style basketball shooting game built with Python and Pygame. Test your aim and timing as you shoot basketballs into a moving hoop before time runs out!

🎮 Game Overview
Basketball Shooter is a physics-based basketball game where players drag and release to shoot basketballs at a moving hoop. The game features realistic ball physics with gravity and bouncing, a power meter to gauge shot strength, and a 10-minute countdown timer to rack up as many points as possible.
✨ Features

Intuitive Controls: Simple drag-and-shoot mechanic using mouse input
Realistic Physics: Gravity-based ball movement with bounce dynamics
Moving Target: Hoop moves horizontally to increase difficulty
Power Meter: Visual feedback showing shot power while aiming
Timer System: 10-minute countdown to challenge players
Score Tracking: Keep track of successful shots
Menu System: Main menu, pause functionality, and game over screen
Custom Graphics: Hand-crafted basketball court background and sprites

🎯 How to Play

Aim: Click and hold on the ball to start aiming
Power Up: Drag the mouse to adjust shot angle and power

Longer drag = more powerful shot
Drag direction determines shot trajectory


Shoot: Release the mouse button to launch the ball
Score: Successfully land the ball through the moving hoop to score points
Beat the Clock: Get as many baskets as possible before the timer runs out!

Controls

Mouse Click + Drag: Aim and shoot the basketball
P Key: Pause the game
Mouse Click (Menu): Navigate menus

🚀 Installation
Prerequisites

Python 3.8 or higher
Pygame library

Setup Instructions

Clone or download this repository

bash   git clone <your-repo-url>
   cd basketballshooter

Install required dependencies

bash   pip install pygame

Run the game

bash   python main.py

📁 Project Structure
basketballshooter/
│
├── main.py                 # Game entry point and main loop
│
├── config/
│   ├── __init__.py
│   └── setting.py          # Game configuration and constants
│
├── game/
│   ├── __init__.py
│   ├── ball.py             # Ball physics and shooting mechanics
│   ├── hoop.py             # Moving hoop logic
│   ├── player.py           # Player position management
│   ├── background.py       # Background rendering
│   └── game_manager.py     # Core game logic and state management
│
├── menus/
│   ├── main_menu.py        # Start screen menu
│   ├── pause_menu.py       # Pause screen menu
│   └── game_over_menu.py   # Game over screen with final score
│
├── utils/
│   ├── __init__.py
│   ├── button.py           # Reusable button component
│   ├── draw_text.py        # Text rendering utilities
│   └── paths.py            # Asset path management
│
└── assets/
    └── images/
        ├── ball.png        # Basketball sprite
        ├── Hoop+backboard.png  # Hoop and backboard sprite
        └── bg_img.png      # Background image


⚙️ Configuration
You can customize game settings in config/setting.py:

Window Size: 1240x664 pixels (default)
FPS: 60 frames per second
Physics:

Gravity: 0.45 pixels/frame²
Bounce damping: 0.7 (energy loss on bounce)
Ball power multiplier: 0.25


Gameplay:

Hoop speed: 4 pixels/frame
Timer duration: 10 minutes
Max drag distance: 220 pixels



🎨 Game States
The game uses a state machine to manage different screens:

MENU: Main menu screen
PLAYING: Active gameplay
PAUSED: Game paused (press P to resume)
GAME_OVER: Final score display with restart option

🏗️ Architecture
The game follows an object-oriented design with clear separation of concerns:

GameManager: Orchestrates game logic, physics updates, and collision detection
Ball: Handles shooting mechanics, physics simulation, and drag input
Hoop: Manages hoop movement and scoring zone
Player: Tracks player position (ball launch point)
Menus: Separate classes for each menu screen with button interactions

🛠️ Development
Adding New Features

Custom Ball Skins: Modify ball.py to load different ball sprites
Difficulty Levels: Adjust HOOP_SPEED and TIMER_START_SECONDS in settings
Power-ups: Add new game objects in the game/ directory
Sound Effects: Integrate Pygame's mixer module for audio

Code Style

Follow PEP 8 style guidelines
Use descriptive variable names
Add docstrings to classes and methods
Keep functions focused and single-purpose

🐛 Known Issues

None currently reported

📝 License
This project is open source and available for educational purposes.
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.
👨‍💻 Author
Created as a Python/Pygame learning project.
🙏 Acknowledgments

Built with Pygame
Inspired by classic arcade basketball games


Enjoy the game and happy shooting! 🏀
