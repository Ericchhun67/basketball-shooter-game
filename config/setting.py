

WIDTH = 1240 # Width of the game window
HEIGHT = 664 # Height of the game window
FPS = 60
TITLE = "Basketball Shooter" # Game window title


# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# gameplay Physics
GRAVITY = 0.45 # pixels per frame squared
BALL_POWER_MULTIPLIER = 0.25 # power multiplier for shooting
BOUNCE_DAMPING = 0.7 # energy loss on bounce


# Hoop Movement
HOOP_SPEED = 4 # hoop horizontal speed in pixels per frame 

# Hoop size (scaled square image)
HOOP_SIZE = 420

# Score settings
FONT_NAME = "arial" # font for score display
SCORE_FONT_SIZE = 32 # font size for score display

# Ball settings
BALL_SIZE = 80  # pixel size for the ball sprite

# Aim guide + power meter
MAX_DRAG_DISTANCE = 220  # pixels, used to cap shot power
AIM_GUIDE_COLOR = (255, 255, 255)
AIM_GUIDE_WIDTH = 3

POWER_METER_POS = (20, 60)
POWER_METER_SIZE = (200, 16)
POWER_METER_BG = (30, 30, 30)
POWER_METER_FILL = (0, 200, 255)
POWER_METER_BORDER = (255, 255, 255)
POWER_METER_FONT_SIZE = 18

# Game timer
TIMER_START_SECONDS = 10 * 60  # 10 minutes
TIMER_FONT_SIZE = 28
TIMER_COLOR = (255, 255, 255)
TIMER_MARGIN = 20
