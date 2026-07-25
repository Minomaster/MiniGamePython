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
current_letter = 0

size = 6
gap = 15
square_size = 25

stage = 1
level = 1

grid = []
grid_width = size * square_size + (size + 1) * gap
grid_height = size * square_size + (size + 1) * gap

start_x = (window_WIDTH - grid_width) / 2
start_y = (window_HEIGHT - grid_height) / 2

last_change = pg.time.get_ticks()

# -- CLASSES -- #
class Square():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.index = 0
    self.color = (0, 0, 255)
    self.pressed = False

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

  def color(self):

    mousePos = pg.mouse.get_pos()
    if self.create.collidepoint(mousePos):
      pg.mouse.set_cursor(pg.cursors.tri_left)
      if pg.mouse.get_pressed()[0] == 1 and self.pressed == False:
        pg.mouse.set_cursor(pg.cursors.broken_x)
        self.pressed = True
        print("GET PRESSED!")
    if pg.mouse.get_pressed()[0] == 0:
      self.pressed = False

# -- FUNCTIONS -- #

def new_round():
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

  for row in grid:
    for square in row:
      square.index = 0

new_round()

arrayColor = []

def arrayColorFunc():
  randColor = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
  return randColor

arrayColor.append(arrayColorFunc())

# -- KEEP THE GAME RUNNING + SETTINGS -- #
run = True
while run:
  current_time = pg.time.get_ticks()
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
  window.fill((95, 128, 132))

  for row in grid:
    for square in row:
      square.draw()

  if current_time - last_change >= 10:
    for row in grid:
      for square in row:
        square.color = arrayColor[random.randint(1, len(arrayColor))]
    last_change = pg.time.get_ticks()
  pg.display.flip()

# -- FOOTER -- #
pg.quit()