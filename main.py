# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame as p
import constants as c
import player as pl

def main():
    p.init()
    screen = p.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = p.time.Clock()
    dt = 0

    updatable = p.sprite.Group()
    drawable = p.sprite.Group()

    pl.Player.containers = (updatable, drawable)

    player = pl.Player((c.SCREEN_WIDTH/2), (c.SCREEN_HEIGHT/2))


    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        p.Surface.fill(screen, color="black")
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        p.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()