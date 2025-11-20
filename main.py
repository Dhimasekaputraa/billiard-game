import pygame
import collisions
import event
import gamestate
import graphics
import config

was_closed = False
while not was_closed:
    game = gamestate.GameState()
    game.start_pool()
    events = event.events()

    while not (events["closed"]):
        events = event.events()
        collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
        game.redraw_all()

    was_closed = events["closed"]

pygame.quit()
