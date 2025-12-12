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
window_caption = "Project Billiard Py"
fps_limit = 60

# table settings
table_margin = 32  #40
table_side_color = (64, 31, 19)
table_color = (0, 100, 0)
separation_line_color = (200, 200, 200)
hole_radius = 22
middle_hole_offset = np.array([[-hole_radius * 1.5, hole_radius * 0.6], [-hole_radius * 1, 0],
                               [hole_radius * 1, 0], [hole_radius * 1.5, hole_radius * 0.6]]) 
side_hole_offset = np.array([
    [- 2 * math.cos(math.radians(45)) * hole_radius - hole_radius * 0.6, hole_radius * 0.6],
    [- 1 * math.cos(math.radians(45)) * hole_radius, -
    1 * math.cos(math.radians(45)) * hole_radius],
    [1 * math.cos(math.radians(45)) * hole_radius,
     1 * math.cos(math.radians(45)) * hole_radius],
    [- hole_radius * 0.6, 2 * math.cos(math.radians(45)) * hole_radius + hole_radius * 0.6]
])

# cue settings
player1_cue_color = (130, 65, 0)
player2_cue_color = (200, 100, 0)
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
    (220, 220, 0),
    (0, 0, 150),
    (220, 0, 0),
    (125, 35, 200),
    (255, 150, 0),
    (0, 150, 0),
    (100, 0, 0),
    (0, 0, 0),
    (220, 220, 0),
    (0, 0, 150),
    (220, 0, 0),
    (125, 35, 200),
    (225, 150, 0),
    (0, 150, 0),
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
player1_turn_label = "Player 1 turn"
player2_turn_label = "Player 2 turn"
penalty_indication_text = " (Click on the ball to move it)"
game_over_label_font_size = 40

#menu config
menu_title_text = "BILLIARD GAME"
menu_title_font_size = 60
menu_option_font_size = 40
menu_text_color = (255, 255, 255)
menu_text_selected_color = (100, 200, 100)
menu_margin = 32
menu_spacing = np.array([10, 10])

#menu buttons
menu_buttons = ["Play Single Player", "Play Multiplayer", "Exit"]
play_single_button = 1
play_multi_button = 2
exit_button = 3