import math
import pygame

# Inisialisasi pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Billiard Game")

def main(window):
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
main(window)
