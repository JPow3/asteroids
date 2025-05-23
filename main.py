# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants as c
import player as p

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = p.Player((c.SCREEN_WIDTH/2), (c.SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()