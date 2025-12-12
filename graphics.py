import numpy as np
import pygame
import config
import event


class Canvas:
    def __init__(self):
        if config.fullscreen:
            config.set_max_resolution()
            self.surface = pygame.display.set_mode(config.resolution, pygame.FULLSCREEN)
        else:
            self.surface = pygame.display.set_mode(config.resolution)
        self.background = pygame.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(config.table_color)
        self.surface.blit(self.background, (0, 0))


def add_separation_line(canvas):
    # white ball separation line
    pygame.draw.line(canvas.background, config.separation_line_color, (config.white_ball_initial_pos[0], 0),
                     (config.white_ball_initial_pos[0], config.resolution[1]))

def draw_main_menu(game_state):
    # Draw title
    title_font = config.get_default_font(config.menu_title_font_size)
    title_text = title_font.render(config.menu_title_text, True, config.menu_text_color)
    title_rect = title_text.get_rect(center=(config.resolution[0]//2, 80))
    game_state.canvas.surface.blit(title_text, title_rect)
    
    # Draw buttons (sama style dengan pause menu)
    button_width = 350
    button_height = 60
    button_spacing = 20
    start_y = config.resolution[1]//2 - 40
    
    button_rects = []
    for i, button_text in enumerate(config.menu_buttons):
        button_y = start_y + i * (button_height + button_spacing)
        button_rect = pygame.Rect(
            config.resolution[0]//2 - button_width//2,
            button_y,
            button_width,
            button_height
        )
        button_rects.append((button_text, button_rect))
    
    pygame.display.flip()
    
    # Wait for button click
    button_clicked = 0
    was_clicked_prev = False
    
    while button_clicked == 0:
        mouse_pos = pygame.mouse.get_pos()
        user_events = event.events()
        is_clicked_now = user_events["clicked"]
        
        # Detect NEW click
        new_click_detected = is_clicked_now and not was_clicked_prev
        
        # Draw title
        game_state.canvas.surface.blit(title_text, title_rect)
        
        # Draw buttons dengan hover effect
        button_font = config.get_default_font(config.menu_option_font_size)
        for i, (button_text, button_rect) in enumerate(button_rects):
            is_hover = button_rect.collidepoint(mouse_pos)
            button_color = config.menu_text_selected_color if is_hover else config.menu_button_color
            
            pygame.draw.rect(game_state.canvas.surface, button_color, button_rect, border_radius=10)
            pygame.draw.rect(game_state.canvas.surface, (255, 255, 255), button_rect, 3, border_radius=10)
            
            text_surface = button_font.render(button_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button_rect.center)
            game_state.canvas.surface.blit(text_surface, text_rect)
            
            # Check click
            if new_click_detected and button_rect.collidepoint(mouse_pos):
                button_clicked = i + 1
        
        pygame.display.flip()
        
        # Event handling
        if user_events["closed"] or user_events["quit_to_main_menu"]:
            button_clicked = len(button_rects)
        
        was_clicked_prev = is_clicked_now
    
    return button_clicked


def draw_pause_menu(game_state):
    """Menampilkan pause menu tanpa background overlay"""
    
    # Title
    title_font = config.get_default_font(60)
    title_text = title_font.render(config.pause_menu_title, True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(config.resolution[0]//2, 120))
    game_state.canvas.surface.blit(title_text, title_rect)
    
    # Buttons
    button_width = 300
    button_height = 60
    button_spacing = 20
    start_y = config.resolution[1]//2 - 60
    
    button_rects = []
    for i, button_text in enumerate(config.pause_menu_buttons):
        button_y = start_y + i * (button_height + button_spacing)
        button_rect = pygame.Rect(
            config.resolution[0]//2 - button_width//2,
            button_y,
            button_width,
            button_height
        )
        button_rects.append(button_rect)
    
    pygame.display.flip()
    
    # Wait for button click
    button_clicked = 0
    was_clicked_prev = False
    
    while button_clicked == 0:
        mouse_pos = pygame.mouse.get_pos()
        user_events = event.events()
        is_clicked_now = user_events["clicked"]
        
        # Detect NEW click (transition from not clicked to clicked)
        new_click_detected = is_clicked_now and not was_clicked_prev
        
        # Redraw title (tanpa overlay)
        game_state.canvas.surface.blit(title_text, title_rect)
        
        # Draw buttons with hover effect
        button_font = config.get_default_font(35)
        for i, (button_text, button_rect) in enumerate(zip(config.pause_menu_buttons, button_rects)):
            is_hover = button_rect.collidepoint(mouse_pos)
            button_color = config.pause_menu_button_hover_color if is_hover else config.pause_menu_button_color
            
            pygame.draw.rect(game_state.canvas.surface, button_color, button_rect, border_radius=10)
            pygame.draw.rect(game_state.canvas.surface, (255, 255, 255), button_rect, 3, border_radius=10)
            
            text_surface = button_font.render(button_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button_rect.center)
            game_state.canvas.surface.blit(text_surface, text_rect)
            
            # Check click
            if new_click_detected and button_rect.collidepoint(mouse_pos):
                button_clicked = i + 1
        
        pygame.display.flip()
        
        # Event handling
        if user_events["closed"]:
            return None
        
        was_clicked_prev = is_clicked_now
    
    return button_clicked

