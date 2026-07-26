# -- HEAD -- #
import pygame as pg
import random
pg.init() # initialize the game

# -- WINDOW SETTINGS -- #
window_WIDTH = 600
window_HEIGHT = 600

window = pg.display.set_mode((window_WIDTH, window_HEIGHT)) # make the window
pg.display.set_caption("WEEWOOWEEWOO") # set the window title

# -- PRE-DEFENITIONS -- #
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = 2
gap = 15
square_size = 25

stage = 1
level = 1

grid = []

last_change = pg.time.get_ticks()
font = pg.font.SysFont(None, 22)
title_font = pg.font.SysFont(None, 32)


# -- CLASSES -- #
class Square():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.index = 0
    self.color = (0, 0, 255)
    self.impostor = False

  def draw(self):
    self.create = pg.draw.rect(
      window, 
      self.color,
      (
        start_x + self.x * (square_size + gap),
        start_y + self.y * (square_size + gap),
        square_size,
        square_size,
      )
    )
    letter = font.render(alfabet[self.index], True, (255, 255, 255))
    letter_rect = letter.get_rect(center=self.create.center)
    window.blit(letter, letter_rect)

  def update(self, event):
    global level, stage, size
    if event.type == pg.MOUSEBUTTONDOWN:
      if self.create.collidepoint(event.pos):
        if self.impostor:
          print("SUCCESS!")
          level += 1
          if level > 5:
            stage += 1
            level = 1
            size += 1
          new_round()
        else:
          print("WRONG!")

# -- FUNCTIONS -- #
def new_round():
    global grid_width, grid_height, start_x, start_y

    grid_width = size * square_size + (size + 1) * gap
    grid_height = size * square_size + (size + 1) * gap

    start_x = (window_WIDTH - grid_width) / 2
    start_y = (window_HEIGHT - grid_height) / 2

    grid.clear()

    for i in range(size):
        row = []
        for j in range(size):
            square = Square(j, i)
            row.append(square)
        grid.append(row)

    all_squares = []

    for row in grid:
        for square in row:
            all_squares.append(square)

    impostor = random.choice(all_squares)
    impostor.impostor = True

    for row in grid:
        for square in row:
            square.index = 0
new_round()

# -- KEEP THE GAME RUNNING + SETTINGS -- #
run = True

while run:
  current_time = pg.time.get_ticks()
  events = pg.event.get()

  for event in events:
    if event.type == pg.QUIT:
      run = False

  window.fill((95, 128, 132))

  title = title_font.render(f"Stage {stage}  |  Level {level}", True, (255, 255, 255))
  title_rect = title.get_rect(center=(window_WIDTH / 2, start_y - 30))
  window.blit(title, title_rect)

  for row in grid:
      for square in row:
          square.draw()
          for event in events:
              square.update(event)

  if current_time - last_change >= 1000:
    for row in grid:
      for square in row:
        if square.impostor:
          square.index += 1
          square.index %= (level + 1)
        else:
          square.index = random.randint(0, level)
    last_change = current_time
  pg.display.flip()

# -- FOOTER -- #
pg.quit()