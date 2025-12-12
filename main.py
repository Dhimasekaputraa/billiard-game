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

    # Jika user menekan tombol Exit
    if button_pressed == config.exit_button:
        was_closed = True
        continue

    # Jika user memilih salah satu mode game
    if game_mode is not None:
        # Loop untuk handle restart
        game_running = True
        while game_running:
            # Buat game baru dengan mode yang dipilih
            game = gamestate.GameState(game_mode=game_mode)
            game.start_pool()
            events = event.events()
            exit_to_menu = False
            should_restart = False
            
            while not (events["closed"] or game.is_game_over or exit_to_menu or should_restart):
                events = event.events()
                
                # Check pause button dengan ESC key
                if events["quit_to_main_menu"]:
                    pause_action = graphics.draw_pause_menu(game)
                    
                    if pause_action is None:
                        # User closed window dari pause menu
                        was_closed = True
                        game_running = False
                        exit_to_menu = True
                        break
                    elif pause_action == config.pause_exit_button:
                        # Exit to main menu
                        game_running = False
                        exit_to_menu = True
                        break
                    elif pause_action == config.pause_restart_button:
                        # Restart game - keluar dari inner loop, akan create game baru
                        should_restart = True
                        break
                    
                    # Redraw setelah keluar dari pause
                    game.redraw_all()
                
                collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
                game.redraw_all()

                if game.all_not_moving():
                    game.check_pool_rules()
                    game.cue.make_visible(game.current_player)
                    
                    while not ((events["closed"] or exit_to_menu) or game.is_game_over) and game.all_not_moving():
                        game.redraw_all()
                        events = event.events()
                        
                        # Check pause button dengan ESC key saat idle
                        if events["quit_to_main_menu"]:
                            pause_action = graphics.draw_pause_menu(game)
                            
                            if pause_action is None:
                                # User closed window
                                was_closed = True
                                game_running = False
                                exit_to_menu = True
                                break
                            elif pause_action == config.pause_exit_button:
                                # Exit to main menu
                                game_running = False
                                exit_to_menu = True
                                break
                            elif pause_action == config.pause_restart_button:
                                # Restart - break dari inner loop
                                should_restart = True
                                break
                            
                            game.redraw_all()
                        
                        if game.cue.is_clicked(events):
                            game.cue.cue_is_active(game, events)
                        elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                            game.white_ball.is_active(game, game.is_behind_line_break())
                
                # Check jika window closed
                if events["closed"]:
                    was_closed = True
                    game_running = False
                    exit_to_menu = True
                    break
            
            # Jika restart, loop akan continue dan create game baru dengan mode yang sama
            # Jika exit_to_menu atau closed, loop akan break dan kembali ke main menu
            if was_closed:
                # Window ditutup, keluar dari semua loop
                game_running = False
            elif should_restart:
                # Restart game - continue loop untuk create game baru dengan game_mode yang sama
                continue
            else:
                # Exit to menu atau game over
                game_running = False

pygame.quit()