import pygame
import myGraphics
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

s.connect(('127.0.0.1', port))

print(s.recv(1024).decode('utf8'))

# s.close()
WHITE = (255, 255, 255)
GRAY = (204, 204, 204)
pygame.init()

screen = pygame.display.set_mode([500, 550])
pygame.display.set_caption("Four in a Row Game")


if __name__ == "__main__":
    global columns, rows, turn
    running = True
    myGraphics.main_menu_screen(screen)
    pygame.display.flip()
    screen1 = True  # menu
    screen2 = False  # human-waiting
    screen3 = False  # AI levels
    screen4 = False  # AI board size
    screen5 = False  # AI order
    screen6 = False  # board screen
    screen6_checker = False
    play_human = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and screen1 and (not screen2) and (not screen3) and (not screen4) \
                    and (not screen5) and (not screen6):
                try:
                    if myGraphics.mask_human_button.get_at((event.pos[0] - 90, event.pos[1] - 200)) and \
                            myGraphics.checker_main_menu:
                        # Call the method that change the screen
                        myGraphics.checker_main_menu = False
                        screen2 = True
                        screen1 = False
                        myGraphics.human_play_option(screen)
                        pygame.display.flip()
                        s.send(str("Player chose to play with human").encode('utf8'))
                        play_human = True
                except IndexError:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN and screen1 and (not screen2) and (not screen3) and (not screen4)\
                    and (not screen5) and (not screen6):
                try:
                    if myGraphics.mask_ai_button.get_at((event.pos[0] - 60, event.pos[1] - 300)) and \
                            myGraphics.checker_main_menu:
                        myGraphics.checker_main_menu = False
                        screen3 = True
                        screen1 = False
                        myGraphics.computer_play_option_levels(screen)
                        pygame.display.flip()
                        play_human = False
                except IndexError:
                    pass
            if not play_human:
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and screen3 and \
                        (not screen4) and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_easy_level.get_at((event.pos[0] - 90, event.pos[1] - 200)) and \
                                myGraphics.checker_levels:
                            myGraphics.checker_levels = False
                            screen4 = True
                            screen3 = False
                            myGraphics.board_options(screen)
                            pygame.display.flip()
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and screen3 and \
                        (not screen4) and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_medium_level.get_at((event.pos[0] - 70, event.pos[1] - 300)) and \
                                myGraphics.checker_levels:
                            myGraphics.checker_levels = False
                            screen4 = True
                            screen3 = False
                            myGraphics.board_options(screen)
                            pygame.display.flip()
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and screen3 and \
                        (not screen4) and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_hard_level.get_at((event.pos[0] - 80, event.pos[1] - 380)) and \
                                myGraphics.checker_levels:
                            myGraphics.checker_levels = False
                            screen4 = True
                            screen3 = False
                            myGraphics.board_options(screen)
                            pygame.display.flip()
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_5x4.get_at((event.pos[0]-70, event.pos[1]-200)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 5
                            rows = 4
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_6x5.get_at((event.pos[0]-70, event.pos[1]-270)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 6
                            rows = 5
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_7x6.get_at((event.pos[0]-70, event.pos[1]-350)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 7
                            rows = 6
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_8x7.get_at((event.pos[0]-250, event.pos[1]-200)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 8
                            rows = 7
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_9x7.get_at((event.pos[0]-250, event.pos[1]-270)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 9
                            rows = 7
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        screen4 and (not screen5) and (not screen6):
                    try:
                        if myGraphics.mask_level_10x7.get_at((event.pos[0]-250, event.pos[1]-350)) and \
                                myGraphics.board_checker:
                            screen4 = False
                            screen5 = True
                            myGraphics.choose_order(screen)
                            pygame.display.flip()
                            columns = 10
                            rows = 7
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        (not screen4) and screen5 and (not screen6):
                    try:
                        if myGraphics.mask_button_first.get_at((event.pos[0]-70, event.pos[1]-200)) and \
                                myGraphics.order_checker:
                            screen6 = True
                            myGraphics.draw_board(screen, columns, rows)
                            pygame.display.flip()
                            turn = 1
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and (not screen1) and (not screen2) and (not screen3) and \
                        (not screen4) and screen5 and (not screen6):
                    try:
                        if myGraphics.mask_button_second.get_at((event.pos[0]-250, event.pos[1]-215)) and \
                                myGraphics.order_checker:
                            screen6 = True
                            myGraphics.draw_board(screen, columns, rows)
                            pygame.display.flip()
                            turn = 2
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN and screen6 and screen6_checker:
                    # myGraphics.color(screen, event.pos, turn)
                    # print(myGraphics.centers)
                    pass
                if (not screen1) and (not screen2) and screen3 and (not screen4) and (not screen5) and (not screen6):
                    myGraphics.checker_levels = True
                if (not screen1) and (not screen2) and (not screen3) and screen4 and (not screen5) and (not screen6):
                    myGraphics.board_checker = True
                if (not screen1) and (not screen2) and (not screen3) and (not screen4) and screen5 and (not screen6):
                    myGraphics.order_checker = True
                if screen6:
                    screen6_checker = True
    pygame.quit()

s.close()
