import pygame

WHITE = (255, 255, 255)
GRAY = (204, 204, 204)

global centers, radius, cl, board, rows_lib


def draw_board(screen_to_display, columns, rows):
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
    board = [[0*x*y for x in range(columns)] for y in range(rows+1)]
    # board = [[0]*rows]*(columns+1)


def color(screen_to_display, position, turn, columns, r_last):
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
    screen_to_display.fill((128, 170, 255))
    winner = pygame.image.load('winner.png').convert_alpha()
    screen_to_display.blit(winner, (90, 100))


def load_final_loose(screen_to_display):
    screen_to_display.fill((128, 170, 255))
    winner = pygame.image.load('game_over.png').convert_alpha()
    screen_to_display.blit(winner, (20, 100))
