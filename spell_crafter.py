import pygame as pg

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spell Crafter")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
           running = False

    screen.fill(BLACK)
    pg.display.flip()
