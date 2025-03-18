# Arden Boettcher
# 3/3/25
# Config
from pygame import color as c

# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)


def rainbow(color: list[int], step = 1):
  hsva = c.Color(color)
  try:
    hsva.hsva = (hsva.hsva[0] + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  except ValueError:
    hsva.hsva = (hsva.hsva[0] - 360 + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  rgb = (hsva.r,  hsva.g, hsva.b)
  return rgb