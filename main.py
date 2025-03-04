# Arden Boettcher
# 3/3/35
# Text Practice

import pygame
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("PLACEHOLDER")

# Setting up the clock
clock = pygame.time.Clock()

main_font = pygame.font.Font("highway-encounter.ttf", 20)

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True

def center_text(text: str, font: pygame.font.Font, color: tuple) -> tuple[pygame.Surface, pygame.Rect]:
  words = font.render(text, False, color)
  text_rect = words.get_rect()
  text_rect.center = (config.WIDTH / 2, config.HEIGHT / 2)
  return words, text_rect

def draw_text(surface: pygame.Surface, text: tuple):
  surface.blit(text[0], text[1])


# Main loop
def main():
  # The bool for the main loop
  running = True

  # Returns centered text
  text = center_text("THIS IS TEXT", main_font, config.BLACK)

  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    # Draws the text
    draw_text(screen, text)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
