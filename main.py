import pygame

import collisions
import event
import gamestate
import graphics
import config

was_closed = False
while not was_closed:
    # Buat game state sementara hanya untuk menampilkan menu
    temp_game = gamestate.GameState()
    button_pressed = graphics.draw_main_menu(temp_game)

    # Tentukan mode berdasarkan tombol yang ditekan
    if button_pressed == config.play_single_button:
        game_mode = "single"
    elif button_pressed == config.play_multi_button:
        game_mode = "multiplayer"
    else:
        game_mode = None

    # Jika user memilih salah satu mode game
    if game_mode is not None:
        # Buat game baru dengan mode yang dipilih
        game = gamestate.GameState(game_mode=game_mode)
        game.start_pool()
        events = event.events()
        
        while not (events["closed"] or game.is_game_over or events["quit_to_main_menu"]):
            events = event.events()
            
            # Cek pause game
            if events["pause"]:
                pause_result = graphics.draw_pause_screen(game)
                if pause_result == "exit":
                    events["quit_to_main_menu"] = True
                    break
                else:
                    game.redraw_all()
            
            collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
            game.redraw_all()

            if game.all_not_moving():
                game.check_pool_rules()
                game.cue.make_visible(game.current_player)
                while not (
                    (events["closed"] or events["quit_to_main_menu"]) or game.is_game_over) and game.all_not_moving():
                    game.redraw_all()
                    events = event.events()
                    
                    # Cek pause game saat bola berhenti
                    if events["pause"]:
                        pause_result = graphics.draw_pause_screen(game)
                        if pause_result == "exit":
                            events["quit_to_main_menu"] = True
                            break
                        else:
                            game.redraw_all()
                            continue
                    
                    if game.cue.is_clicked(events):
                        game.cue.cue_is_active(game, events)
                    elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                        game.white_ball.is_active(game, game.is_behind_line_break())
        was_closed = events["closed"]

    # Jika user menekan tombol Exit
    if button_pressed == config.exit_button:
        was_closed = True

pygame.quit()