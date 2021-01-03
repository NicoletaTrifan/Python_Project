"""
Module that has functions that assure creating the graphic interface of the game, by importing it in the main file.
Contains function that draw the board, place pieces and load screens for the situations when a player wins/lose or it
is a draw.
"""
import pygame
import numpy
WHITE = (255, 255, 255)
GRAY = (204, 204, 204)

global centers, radius, cl, board, rows_lib


def draw_board(screen_to_display, columns, rows):

    """
    Gets preferences and draws the board on the screen.
    :param screen_to_display: the screen where the board is supposed to be displayed
    :param columns: variable that represents how many columns the board should have
    :param rows: variable that represents how many rows the board should have
    """

    global centers, radius, board, rows_lib
    screen_to_display.fill((128, 170, 255))
    centers = list()
    rows_lib = rows
    for c in range(columns):
        for r in range(rows):
            pygame.draw.rect(screen_to_display, WHITE, (int(c*500/columns), int(r*500/columns+500/rows), 100, 100))
            pygame.draw.circle(screen_to_display, (128, 170, 255), (int(c*500/columns+500/(columns*2)),
                                                                    int(r*500/columns + 500/rows+500/(columns*2))),
                               int(500/(2.5*columns)))
            centers.append([(int(c*500/columns+500/(columns*2)), int(r*500/columns + 500/rows+500/(columns*2)))])
    radius = int(500/(2.5*columns))
    board = numpy.array([[0*x*y for x in range(columns)] for y in range(rows+1)])


def color(screen_to_display, position, turn, columns, r_last):

    """
    Gets parameters and colors a piece on the board (place a piece).
    :param screen_to_display: the screen where the board is supposed to be displayed
    :param position: column that was calculated, on which a piece is placed
    :param turn: variable that defines the color of the piece depending on the player's turn
    :param columns: variable that denotes the total amount of columns on board
    :param r_last: variable that denotes the actual lowest row on the board
    :return:
    """

    global cl, rows_lib
    if turn == 1:
        cl = (255, 0, 0)
    elif turn == 2:
        cl = (255, 255, 0)
    pygame.draw.circle(screen_to_display, cl, (int(position * 500 / columns + 500 / (columns * 2)),
                                               int(r_last * 500 / columns + 500 / rows_lib + 500 / (columns * 2))),
                       int(500 / (2.5 * columns)))
    pygame.display.update()


def load_final_win(screen_to_display):

    """
    Function displays the screen with winning message when playing with AI.
    :param screen_to_display: the screen where the board is supposed to be displayed
    :return:
    """

    screen_to_display.fill((128, 170, 255))
    winner = pygame.image.load('winner.png').convert_alpha()
    screen_to_display.blit(winner, (90, 100))


def load_final_lose(screen_to_display):
    """
    Function displays the screen with game over message when playing with AI.
    :param screen_to_display: the screen where the board is supposed to be displayed
    :return:
    """
    screen_to_display.fill((128, 170, 255))
    winner = pygame.image.load('game_over.png').convert_alpha()
    screen_to_display.blit(winner, (20, 100))


def winner_player_screen(screen_to_display, player):
    """
    Function displays the screen with winning message when playing with a human opponent.
    :param screen_to_display: the screen where the board is supposed to be displayed
    :param player: variable that represents which of players has won
    :return:
    """
    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    menu_title = font.render('Winner is '+player, True, GRAY, None)
    menu_title_area = menu_title.get_rect()
    menu_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(menu_title, menu_title_area)


def draw(screen_to_display):
    """
    Function used to display the message that game ended with draw.
    :param screen_to_display: the screen where the board is supposed to be displayed
    :return:
    """
    screen_to_display.fill((128, 170, 255))
    font = pygame.font.SysFont("segoescript", 36)

    title = font.render('4 in a ROW', True, WHITE, None)
    title_area = title.get_rect()
    title_area.center = (500 // 2, 500 // 8)
    screen_to_display.blit(title, title_area)

    menu_title = font.render("Game ends with draw", True, GRAY, None)
    menu_title_area = menu_title.get_rect()
    menu_title_area.center = (500 // 2, 500 // 3)
    screen_to_display.blit(menu_title, menu_title_area)
