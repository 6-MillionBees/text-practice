# Arden Boettcher
# 3/3/35
# Text Practice

import pygame
import config
pygame.init()


def game_init() -> pygame.Surface:
  # Setting up the window
  screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
  pygame.display.set_caption("PLACEHOLDER")
  return screen

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True

def check_pos(pos):
  if pos[0] <= 0:
    pos[0] = 0
  if pos[0] >= config.WIDTH:
    pos[0] = config.WIDTH
  if pos[1] <= 0:
    pos[1] = 0
  if pos[1] >= config.HEIGHT:
    pos[1] = config.HEIGHT

def draw_text(surface: pygame.Surface, font: pygame.font.Font, words: str, pos: tuple, color: tuple, centered = False, alias = False, degrees = 0) -> None:
  text = font.render(words, alias, color)
  text.set_colorkey(config.BLACK)
  text = pygame.transform.rotate(text, degrees)

  text_rect = text.get_rect(topleft=pos)

  if centered:
    text_rect = text.get_rect(center=pos)

  surface.blit(text, text_rect)
  return text, text_rect


# Main loop
def main():
  screen = game_init()

  # The bool for the main loop
  running = True

  # Setting up the clock
  clock = pygame.time.Clock()

  main_font = pygame.font.Font("highway-encounter.ttf", 20)

  degrees = 0

  text_pos = [config.WIDTH / 2, config.HEIGHT / 2]

  while running:

    degrees += 1

    # Call events / update running
    running = main_events()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      text_pos[1] -= 5
    if keys[pygame.K_DOWN]:
      text_pos[1] += 5
    if keys[pygame.K_LEFT]:
      text_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
      text_pos[0] += 5

    check_pos(text_pos)

    # Fills window
    screen.fill(config.BLACK)

    # Draws the text
    draw_text(screen, main_font, "text", text_pos, config.WHITE, centered = True, alias = True, degrees = degrees)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
