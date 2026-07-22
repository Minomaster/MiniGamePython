# -- HEAD -- #
import pygame as pg
pg.init() # initialize the game

# -- WINDOW SETTINGS -- #

window_WIDTH = 600
window_LENGTH = 600

window = pg.display.set_mode((window_WIDTH, window_LENGTH)) # make the window
pg.display.set_caption("WEEWOOWEEWOO") # set the window title

# -- PRE-PROCESSING -- #

class Square():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.pressed = False

  def make(self):
    self.create = pg.draw.rect(
      window, 
      (0, 0, 255),
      (window_WIDTH/2 + 80*self.x, window_LENGTH/2 + 80*self.y, 25, 25)
    )
    mousePos = pg.mouse.get_pos()
    if self.create.collidepoint(mousePos):
      pg.mouse.set_cursor(pg.cursors.tri_left)
      if pg.mouse.get_pressed()[0] == 1 and self.pressed == False:
        pg.mouse.set_cursor(pg.cursors.broken_x)
        self.pressed = True
        print("GET PRESSED!")
    if pg.mouse.get_pressed()[0] == 0:
      self.pressed = False


stage = 1
level = 1

grid = []
size = 7

for i in range(size):
  row = []
  for j in range(size):
    square = Square(j, i)
    row.append(square)
  grid.append(row)

# -- KEEP THE GAME RUNNING + SETTINGS -- #
run = True
while run:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
  window.fill((95, 128, 132))
  for row in grid:
    for square in row:
      square.make()
  pg.display.flip()

# -- FOOTER -- #
pg.quit()