import math
import numpy as np
import pygame


# fonts need to be initialised before using
def get_default_font(size):
    font_defualt = pygame.font.get_default_font()
    return pygame.font.Font(font_defualt, size)


def set_max_resolution():
    infoObject = pygame.display.Info()
    global resolution
    global white_ball_initial_pos
    resolution = np.array([infoObject.current_w, infoObject.current_h])
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, 0]) * [0.25, 0.5]

# window settings
fullscreen = False
# fullscreen resolution can only be known after initialising the screen
if not fullscreen:
    resolution = np.array([1000, 500])
window_caption = "Pool"
fps_limit = 60

# table settings
table_margin = 40
table_side_color = (200, 200, 0)
table_color = (0, 100, 0)
separation_line_color = (200, 200, 200)
hole_radius = 22
middle_hole_offset = np.array([[-hole_radius * 2, hole_radius], [-hole_radius, 0],
                               [hole_radius, 0], [hole_radius * 2, hole_radius]])
side_hole_offset = np.array([
    [- 2 * math.cos(math.radians(45)) * hole_radius - hole_radius, hole_radius],
    [- math.cos(math.radians(45)) * hole_radius, -
    math.cos(math.radians(45)) * hole_radius],
    [math.cos(math.radians(45)) * hole_radius,
     math.cos(math.radians(45)) * hole_radius],
    [- hole_radius, 2 * math.cos(math.radians(45)) * hole_radius + hole_radius]
])

# cue settings
player1_cue_color = (200, 100, 0)
player2_cue_color = (0, 100, 200)
cue_hit_power = 3
cue_length = 250
cue_thickness = 4
cue_max_displacement = 100
# safe displacement is the length the cue stick can be pulled before
# causing the ball to move
cue_safe_displacement = 1
aiming_line_length = 14

# ball settings
total_ball_num = 16
ball_radius = 14
ball_mass = 14
speed_angle_threshold = 0.09
visible_angle_threshold = 0.05
ball_colors = [
    (255, 255, 255),
    (0, 200, 200),
    (0, 0, 200),
    (150, 0, 0),
    (200, 0, 200),
    (200, 0, 0),
    (50, 0, 0),
    (100, 0, 0),
    (0, 0, 0),
    (0, 200, 200),
    (0, 0, 200),
    (150, 0, 0),
    (200, 0, 200),
    (200, 0, 0),
    (50, 0, 0),
    (100, 0, 0)
]
ball_stripe_thickness = 5
ball_stripe_point_num = 25
ball_starting_place_ratio = [0.75, 0.5]


if 'resolution' in locals():
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, 0]) * [0.25, 0.5]
ball_label_text_size = 10

friction_threshold = 0.06
friction_coeff = 0.99
ball_coeff_of_restitution = 0.9
table_coeff_of_restitution = 0.9

# in-game ball target variables
player1_target_text = 'P1 balls - '
player2_target_text = 'P2 balls - '
target_ball_spacing = 3
player1_turn_label = ""
player2_turn_label = ""
penalty_indication_text = " "
game_over_label_font_size = 40
