import pygame

WHITE = (255, 255, 255)
GRAY = (204, 204, 204)

global mask_human_button, mask_ai_button, checker_main_menu, mask_easy_level, mask_medium_level, mask_hard_level, \
    checker_levels, board_checker, mask_level_5x4, mask_level_6x5, mask_level_7x6, mask_level_8x7, mask_level_9x7,\
    mask_level_10x7, order_checker, mask_button_first, mask_button_second, centers, radius, cl


def main_menu_screen(screen_to_display):
    global mask_human_button, mask_ai_button, checker_main_menu  # cheks if we are in the main screen/ availability of \
    # the masks
    checker_main_menu = True
    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    menu_title = font.render('Main Menu', True, GRAY, None)
    menu_title_area = menu_title.get_rect()
    menu_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(menu_title, menu_title_area)

    # play_human_button = pygame.draw.rect(screen, WHITE, (150,230,200,50))
    play_human_button = pygame.image.load('play_human.png').convert_alpha()
    screen_to_display.blit(play_human_button, (90, 200))
    mask_human_button = pygame.mask.from_surface(play_human_button)

    play_computer_button = pygame.image.load('play_AI.png').convert_alpha()
    screen_to_display.blit(play_computer_button, (60, 300))
    mask_ai_button = pygame.mask.from_surface(play_computer_button)


def human_play_option(screen_to_display):
    screen_to_display.fill((0, 0, 0))
    pygame.display.update()

    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    menu_title = font.render('Waiting for another', True, GRAY, None)
    menu_title2 = font.render('player to connect...', True, GRAY, None)
    menu_title_area = menu_title.get_rect()
    menu_title_area.center = (500 // 2, 500 // 3)
    menu_title_area2 = menu_title2.get_rect()
    menu_title_area2.center = (500 // 2, 500 // 2)
    screen_to_display.blit(menu_title, menu_title_area)
    screen_to_display.blit(menu_title2, menu_title_area2)


def computer_play_option_levels(screen_to_display):
    global mask_easy_level, mask_medium_level, mask_hard_level, checker_levels

    checker_levels = False
    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    levels_title = font.render('Choose level', True, GRAY, None)
    levels_title_area = levels_title.get_rect()
    levels_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(levels_title, levels_title_area)

    easy_level_button = pygame.image.load('easy.png').convert_alpha()
    screen_to_display.blit(easy_level_button, (90, 200))
    mask_easy_level = pygame.mask.from_surface(easy_level_button)

    medium_level_button = pygame.image.load('medium.png').convert_alpha()
    screen_to_display.blit(medium_level_button, (70, 300))
    mask_medium_level = pygame.mask.from_surface(medium_level_button)

    hard_level_button = pygame.image.load('hard.png').convert_alpha()
    screen_to_display.blit(hard_level_button, (80, 380))
    mask_hard_level = pygame.mask.from_surface(hard_level_button)


def board_options(screen_to_display):
    global board_checker,  mask_level_5x4,  mask_level_6x5,  mask_level_7x6,  mask_level_8x7,  mask_level_9x7, \
        mask_level_10x7
    board_checker = False
    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    levels_title = font.render('Choose the board size', True, GRAY, None)
    levels_title_area = levels_title.get_rect()
    levels_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(levels_title, levels_title_area)

    board_size_5x4 = pygame.image.load('5x4.png').convert_alpha()
    screen_to_display.blit(board_size_5x4, (70, 200))
    mask_level_5x4 = pygame.mask.from_surface(board_size_5x4)

    board_size_6x5 = pygame.image.load('6x5.png').convert_alpha()
    screen_to_display.blit(board_size_6x5, (70, 270))
    mask_level_6x5 = pygame.mask.from_surface(board_size_6x5)

    board_size_7x6 = pygame.image.load('7x6.png').convert_alpha()
    screen_to_display.blit(board_size_7x6, (70, 350))
    mask_level_7x6 = pygame.mask.from_surface(board_size_7x6)

    board_size_8x7 = pygame.image.load('8x7.png').convert_alpha()
    screen_to_display.blit(board_size_8x7, (250, 200))
    mask_level_8x7 = pygame.mask.from_surface(board_size_8x7)

    board_size_9x7 = pygame.image.load('9x7.png').convert_alpha()
    screen_to_display.blit(board_size_9x7, (250, 270))
    mask_level_9x7 = pygame.mask.from_surface(board_size_9x7)

    board_size_10x7 = pygame.image.load('10x7.png').convert_alpha()
    screen_to_display.blit(board_size_10x7, (250, 350))
    mask_level_10x7 = pygame.mask.from_surface(board_size_10x7)


def choose_order(screen_to_display):
    global order_checker, mask_button_first, mask_button_second
    order_checker = False

    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    levels_title = font.render('Choose the order to move', True, GRAY, None)
    levels_title_area = levels_title.get_rect()
    levels_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(levels_title, levels_title_area)

    first = pygame.image.load('first.png').convert_alpha()
    screen_to_display.blit(first, (70, 200))
    mask_button_first = pygame.mask.from_surface(first)

    second = pygame.image.load('second.png').convert_alpha()
    screen_to_display.blit(second, (250, 215))
    mask_button_second = pygame.mask.from_surface(second)


def draw_board(screen_to_display, columns, rows):
    global centers, radius
    screen_to_display.fill((128, 170, 255))
    centers = list()
    for c in range(columns):
        for r in range(rows):
            pygame.draw.rect(screen_to_display, WHITE, (int(c*500/columns), int(r*500/columns+500/rows), 100, 100))
            pygame.draw.circle(screen_to_display, (128, 170, 255), (int(c*500/columns+500/(columns*2)),
                                                                    int(r*500/columns + 500/rows+500/(columns*2))),
                               int(500/(2.5*columns)))
            centers.append([(int(c*500/columns+500/(columns*2)), int(r*500/columns + 500/rows+500/(columns*2)))])
    radius = int(500/(2.5*columns))


def color(screen_to_display, position, turn):
    global cl
    if turn == 1:
        cl = (255, 0, 0)
    elif turn == 2:
        cl = (255, 255, 0)
    for center in centers:
        if pow((position[0] - center[0][0]), 2) + pow((position[1] - center[0][1]), 2) <= pow(radius, 2):
            pygame.draw.circle(screen_to_display, cl, (center[0][0], center[0][1]), radius)
        else:
            pass
    pygame.display.update()
