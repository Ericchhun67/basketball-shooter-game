# 🏀 Basketball Shooter Game

A fun and challenging 2D basketball shooting game built with Python and Pygame! Test your shooting skills by aiming and launching the ball at a moving hoop. Score as many baskets as you can before time runs out!

## 🎮 Features

- **Intuitive Mouse Controls** – Click and drag to aim, release to shoot
- **Physics-Based Gameplay** – Realistic ball physics with gravity and bounce effects
- **Moving Hoop Challenge** – The hoop moves horizontally to increase difficulty
- **Power Meter** – Visual indicator showing your shot power
- **Aim Guide** – Trajectory line to help you line up the perfect shot
- **Timed Mode** – 10-minute timer adds urgency to your gameplay
- **Score Tracking** – Keep track of your successful baskets
- **Menu System** – Main menu, pause menu, and game over screen

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ericchhun67/basketball-shooter-game.git
   cd basketball-shooter-game
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Start the Game** – Click the "Play" button on the main menu
2. **Aim Your Shot** – Click and drag the basketball to set your shot direction and power
3. **Shoot** – Release the mouse button to launch the ball toward the hoop
4. **Score Points** – Successfully get the ball through the hoop to earn points
5. **Beat the Clock** – Score as many baskets as possible before time runs out!

## 🕹️ Controls

| Action | Control |
|--------|---------|
| Aim & Charge Shot | Click and drag |
| Shoot | Release mouse button |
| Pause Game | Press `P` |
| Navigate Menus | Mouse click |

## 📁 Project Structure

```
basketball-shooter-game/
├── main.py              # Entry point and game loop
├── config/
│   └── setting.py       # Game configuration and constants
├── game/
│   ├── ball.py          # Ball physics and rendering
│   ├── hoop.py          # Hoop movement and collision
│   ├── player.py        # Player position reference
│   ├── background.py    # Background rendering
│   └── game_manager.py  # Core game logic and state
├── menus/
│   ├── main_menu.py     # Main menu screen
│   ├── pause_menu.py    # Pause menu screen
│   └── game_over_menu.py # Game over screen
├── utils/
│   ├── button.py        # Reusable button component
│   ├── draw_text.py     # Text rendering utilities
│   └── paths.py         # Asset path management
└── assets/
    └── images/          # Game sprites and backgrounds
```

## ⚙️ Configuration

Game settings can be customized in `config/setting.py`:

- **Window Settings** – Screen width, height, FPS
- **Physics** – Gravity, ball power, bounce damping
- **Gameplay** – Hoop speed, timer duration, ball size

## 📜 License

This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.

---

**Enjoy the game and happy shooting! 🏀**