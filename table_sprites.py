import numpy as np
import pygame
import config
import gamestate


class Hole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (2 * config.hole_radius, 2 * config.hole_radius))
        # color which will be ignored
        self.image.fill((200, 200, 200))
        self.image.set_colorkey((200, 200, 200))

        pygame.draw.circle(self.image, (0, 0, 0),
                           (config.hole_radius, config.hole_radius), config.hole_radius, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = np.array([x, y])


# this class holds properties of a table side line, but doesn't actually
# draw it
class TableSide():
    def __init__(self, line):
        self.line = np.array(line)
        self.middle = (self.line[0] + self.line[1]) / 2
        self.size = np.round(np.abs(self.line[0] - self.line[1]))
        self.length = np.hypot(*self.size)
        if np.count_nonzero(self.size) != 2:
            # line is perpendicular to y or x axis
            if self.size[0] == 0:
                self.size[0] += 1
            else:
                self.size[1] += 1


# draws the border part of the table
class TableColoring(pygame.sprite.Sprite):
    def __init__(self, table_size, color, table_points):
        pygame.sprite.Sprite.__init__(self)
        self.points = table_points
        self.image = pygame.Surface(table_size)
        self.image.fill(color)
        color_key = (200, 200, 200)
        self.image.set_colorkey(color_key)
        pygame.draw.polygon(self.image, color_key, table_points)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.font = config.get_default_font(config.ball_radius)
        # generates text at the bottom of the table
        self.target_ball_text = [self.font.render(config.player1_target_text, False, config.player1_cue_color),
                                 self.font.render(config.player2_target_text, False, config.player2_cue_color)]

    def redraw(self):
        self.image.fill(config.table_side_color)
        color_key = (200, 200, 200)
        self.image.set_colorkey(color_key)
        pygame.draw.polygon(self.image, color_key, self.points)

    def update(self, game_state):
        self.redraw()
        self.generate_top_left_label(game_state)
        self.generate_top_right_label(game_state)
        self.generate_power_bar(game_state)
        self.generate_target_balls(game_state)

    def generate_target_balls(self, game_state):
        # draws the target balls for each players
        if game_state.ball_assignment is not None:
            start_x = np.array([config.table_margin + config.hole_radius * 3,
                                config.resolution[0] / 2 + config.hole_radius * 3])
            start_y = config.resolution[1] - config.table_margin - self.font.size(config.player1_target_text)[1] / 2
            # the text needs to be moved a bit lower to keep it aligned
            self.image.blit(self.target_ball_text[0], [start_x[0], start_y + config.ball_radius / 2])
            self.image.blit(self.target_ball_text[1], [start_x[1], start_y + config.ball_radius / 2])
            start_x += self.font.size(config.player2_target_text)[0]
            for ball in game_state.balls:
                do_draw = ball.number != 0 and ball.number != 8

                # draw to player holds the players which the balls will be added to
                draw_to_player = []

                # sorts the balls into their places
                if do_draw:
                    if game_state.ball_assignment[gamestate.Player.Player1] == ball.ball_type:
                        draw_to_player.append(1)
                    else:
                        draw_to_player.append(2)

                if ball.number == 8:
                    if game_state.potting_8ball[gamestate.Player.Player1]:
                        draw_to_player.append(1)
                    if game_state.potting_8ball[gamestate.Player.Player2]:
                        draw_to_player.append(2)

                # draws the balls
                for player in draw_to_player:
                    # player-1 because lists start with 0
                    ball.create_image(self.image, (start_x[player - 1], start_y))
                    start_x[player - 1] += config.ball_radius * 2 + config.target_ball_spacing

    def generate_top_left_label(self, game_state):
        # generates the top left label (which players turn is it and if he can move the ball)
        top_left_text = ""
        if game_state.can_move_white_ball:
            top_left_text += config.penalty_indication_text
        if game_state.current_player.value == 1:
            top_left_rendered_text = self.font.render(config.player1_turn_label + top_left_text,
                                                      False, config.player1_cue_color)
        else:
            top_left_rendered_text = self.font.render(config.player2_turn_label + top_left_text,
                                                      False, config.player2_cue_color)
        text_pos = [config.table_margin + config.hole_radius * 3,
                    config.table_margin - self.font.size(top_left_text)[1] / 2]
        self.image.blit(top_left_rendered_text, text_pos)

    def generate_top_right_label(self, game_state):
        # generates the top right label (mode game: practice atau versus)
        if game_state.game_mode == "single":
            mode_text = "PRACTICE MODE"
            text_color = (255, 200, 0)  
        elif game_state.game_mode == "multiplayer":
            mode_text = "VERSUS MODE"
            text_color = (255, 200, 0) 
        else:
            return
        
        mode_rendered_text = self.font.render(mode_text, False, text_color)
        text_size = self.font.size(mode_text)
        # Posisi di sudut kanan atas dengan margin
        text_pos = [config.resolution[0] - config.table_margin - config.hole_radius * 3 - text_size[0],
                    config.table_margin - text_size[1] / 2]
        self.image.blit(mode_rendered_text, text_pos)

    def generate_power_bar(self, game_state):
        # Tampilkan power bar hanya jika cue stick terlihat dan sedang ditarik
        if not game_state.cue.visible:
            return
        
        # Hanya tampilkan power bar ketika displacement lebih besar dari ball_radius
        if game_state.cue.displacement <= config.ball_radius:
            return
        
        # Kalkulasi persentase kekuatan
        # displacement range: ball_radius sampai cue_max_displacement
        # actual power range: 0 sampai (cue_max_displacement - ball_radius - cue_safe_displacement)
        current_displacement = game_state.cue.displacement
        min_displacement = config.ball_radius
        max_displacement = config.cue_max_displacement
        
        # Effective displacement untuk power (dikurangi safe displacement)
        effective_current = max(0, current_displacement - min_displacement - config.cue_safe_displacement)
        effective_max = max_displacement - min_displacement - config.cue_safe_displacement
        
        power_percentage = min(100, max(0, (effective_current / effective_max * 100))) if effective_max > 0 else 0
        
        # Dimensi power bar
        bar_width = 30
        bar_height = 200
        bar_margin = 20
        
        # Posisi power bar di sebelah kanan tengah
        bar_x = config.resolution[0] - config.table_margin - bar_width - bar_margin
        bar_y = (config.resolution[1] - bar_height) / 2
        
        # Gambar latar belakang power bar (kotak kosong)
        pygame.draw.rect(self.image, (100, 100, 100), 
                        (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Gambar fill power bar berdasarkan persentase (merah)
        fill_height = int(bar_height * power_percentage / 100)
        fill_y = bar_y + (bar_height - fill_height)
        pygame.draw.rect(self.image, (255, 0, 0), 
                        (bar_x, fill_y, bar_width, fill_height))
        
        # Gambar label persentase
        percentage_font = config.get_default_font(12)
        percentage_text = f"{int(power_percentage)}%"
        percentage_rendered = percentage_font.render(percentage_text, False, (255, 255, 255))
        text_pos = [bar_x - 25, bar_y + bar_height + 10]
        self.image.blit(percentage_rendered, text_pos)