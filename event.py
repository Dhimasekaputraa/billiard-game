import numpy as np
import pygame


class GameEvent():
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data


def set_allowed_events():
    # only allow keypress events to avoid waisting cpu type on checking useless events
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

def events():
    closed = False
    quit = False
    pause = False
    resume = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True
            if (event.key == pygame.K_SPACE) and not pause:
                pause = True
            if (event.key == pygame.K_SPACE) and pause:
                resume = True
            if event.key == pygame.K_RETURN:
                resume = True

    return {"quit_to_main_menu": quit,
            "closed": closed,
            "clicked": pygame.mouse.get_pressed()[0],
            "mouse_pos": np.array(pygame.mouse.get_pos()),
            "pause": pause,
            "resume": resume}