# -- HEAD -- #
import pygame as pg
pg.init() # initialize the game

# -- WINDOW SETTINGS -- #
window = pg.display.set_mode((1440, 1080)) # make the window
pg.display.set_caption("WEEWOOWEEWOO") # set the window title

window.fill((95, 128, 132))

# -- PRE-PROCESSING -- #
stage = 1
level = 1

#grid = [
#  pg.rec
#]

#for i in grid:
  

# -- KEEP THE GAME RUNNING + SETTINGS -- #
run = True
while run:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
  pg.draw.rect(window, (0, 0, 255), (100, 100, 50, 50))
  pg.display.flip()

# -- FOOTER -- #
pg.quit()