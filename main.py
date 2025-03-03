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



# Main loop
def main():
  # The bool for the main loop
  running = True

  text = main_font.render("THIS IS TEXT", False, config.BLACK)
  text_rect = text.get_rect()
  text_rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    screen.blit(text, text_rect)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
