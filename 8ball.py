import math
import pygame
import pymunk
import pymunk.pygame_util

# Inisialisasi pygame
pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Billiard Game")

def main(window, width, height):
    done = False
    clock = pygame.time.Clock()
    fps = 60

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Warna background
        window.fill((0, 0, 0))

        # Update tampilan
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

# main program
main(window, width, height)
