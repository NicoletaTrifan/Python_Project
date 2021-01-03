"""
Implements the game 4 in a ROW/ Connect 4.
Generate a board based on player preferences.
Player clicks the column he wants to put his piece on, and it is placed on the lowest position of the column.

The player wins when he first makes a row of 4 pieces(horizontally, vertically, diagonally).
Graphic interface is created with myGraphics module.
"""

import sys
import pygame
import myGraphics
import random
WHITE = (255, 255, 255)
GRAY = (204, 204, 204)
global level, first_player_human
pygame.init()

screen = pygame.display.set_mode([500, 550])
pygame.display.set_caption("Four in a Row Game")


def get_complexity():

    """
    Gets the player input from the command line and updates the global variable level that is used to make difference
    between AI playing strategies.
    :return:
    """

    global level
    my_level = input()
    if my_level == "1":
        level = 1
    elif my_level == "2":
        level = 2
    elif my_level == "3":
        level = 3


def check_last_row(last_r):

    """
    Gets the current lowest row that is used to place pieces on the board and checks if it has any available positions.
    :param last_r: The current lowest row with free positions on the board
    :return rez: Counter that is used to check how many available positions remained on the actual row and returned by
    this function in order to complete further actions.
    """

    rez = columns
    for col in range(columns):
        if myGraphics.board[last_r][col] == 1:
            rez = rez - 1
        elif myGraphics.board[last_r][col] == 2:
            rez = rez - 1
        else:
            pass
    return rez


def check_winner():

    """
    This function is called after everytime a  move is made on the board in order to check if there is already a winner
    for the game.
    Depending on the direction of checking, every 4 elements will be selected and verified if they represent a row of
    the same pieces.
    :return:
        1 - player 1 wins
        2 - player 2 wins
        3 - there are no winners yet
    """

    for c in range(COLUMNS-3):  # check horizontal combinations
        for r in range(ROWS):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r][c + 1] == 1 and myGraphics.board[r][c + 2] == 1 and \
                    myGraphics.board[r][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r][c + 1] == 2 and myGraphics.board[r][c + 2] == 2 and \
                    myGraphics.board[r][c + 3] == 2:
                return 2
    for c in range(COLUMNS):   # check vertical combinations
        for r in range(ROWS - 3):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r + 1][c] == 1 and myGraphics.board[r + 2][c] == 1 and \
                    myGraphics.board[r + 3][c] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r + 1][c] == 2 and myGraphics.board[r + 2][c] == 2 and \
                    myGraphics.board[r + 3][c] == 2:
                return 2
    for c in range(COLUMNS - 3):  # check main diagonal
        for r in range(ROWS - 3):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r + 1][c + 1] == 1 and\
                    myGraphics.board[r + 2][c + 2] == 1 and myGraphics.board[r + 3][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r + 1][c + 1] == 2 and \
                    myGraphics.board[r + 2][c + 2] == 2 and myGraphics.board[r + 3][c + 3] == 2:
                return 2
    for c in range(COLUMNS - 3):  # check on secondary diagonal
        for r in range(3, ROWS):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r - 1][c + 1] == 1 and \
                    myGraphics.board[r - 2][c + 2] == 1 and myGraphics.board[r - 3][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r - 1][c + 1] == 2 and \
                    myGraphics.board[r - 2][c + 2] == 2 and myGraphics.board[r - 3][c + 3] == 2:
                return 2
    return 3


def get_best_move():

    """
    The current function has as purpose calculating the best move AI could perform at hard level.
    When human puts a piece on board it calculates the available positions on the horizontal(right, left) and vertical
    directions, then chooses random one of them in order to block the player.
    :return:
    If the position is possible to calculate, function returns the choice.
    """

    directions = list()
    for column in range(COLUMNS):
        for row in range(ROWS):
            if myGraphics.board[row][column] == 1:
                if column-1 >= 0 and myGraphics.board[row][column-1] == 0:
                    directions.append((row, column - 1))
                if column+1 < COLUMNS and myGraphics.board[row][column+1] == 0:
                    directions.append((row, column + 1))
                if row-1 >= 0 and myGraphics.board[row-1][column] == 0:
                    directions.append((row - 1, column))
    if len(directions) > 0:
        return random.choice(directions)


if __name__ == "__main__":
    global columns, rows, turn, level, first_player_human
    running = True
    screen1 = True  # board screen
    play_human = False  # check variable for player choice if he wants to play with a human or not
    medium_flag = True  # flag used at the medium level strategy to assure alternate AI moves(random/calculated)
    draw_score = 0  # variable that is used at every algorithm iteration to check if the game ends with draw
    if len(sys.argv) == 5:
        if sys.argv[1] == "computer":
            play_human = False
        elif sys.argv[1] == "human":
            play_human = True
        else:
            print("Invalid arguments")
            sys.exit()
        if int(sys.argv[2]) > 3 and 3 < int(sys.argv[3]) < int(sys.argv[2]):
            rows = int(sys.argv[3])
            columns = int(sys.argv[2])
            COLUMNS = int(sys.argv[2])
            ROWS = int(sys.argv[3])
        else:
            print("Invalid arguments")
            sys.exit()
        if sys.argv[4] == "computer":
            first_player_human = False
            turn = 2
        elif sys.argv[4] == "human":
            first_player_human = True
            turn = 1
        else:
            print("Invalid arguments")
            sys.exit()
    else:
        print("Invalid arguments")
        sys.exit()
    if not play_human:
        get_complexity()
    myGraphics.draw_board(screen, columns, rows)
    pygame.display.flip()
    while running:
        draw_score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            """
            The following lines checks if there are any positions available on the board.
            If no, and the function check_winner didn't give a result then it is a draw and the suitable screen is 
            showed.
            """

            for c in range(COLUMNS):
                for r in range(ROWS):
                    if myGraphics.board[r][c] != 0:
                        draw_score = draw_score + 0
                    else:
                        draw_score = draw_score + 1
            if draw_score == 0:
                myGraphics.draw(screen)
                pygame.display.update()
            if screen1 and not play_human:  # Player chose to play with AI
                if level == 1:  # easy level algorithm
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if turn == 1:

                            """
                            The formula for the color_col has as purpose to identify in which column fits the current 
                            pixel where the event was identified.
                            """

                            color_col = int(event.pos[0]/(500/columns))
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 1  # every time a piece is placed on board the
                                # matrix behind is updated in order to calculate easy when someone wins/lose/draw etc.
                                myGraphics.color(screen, color_col, 1, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 2
                            elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] ==\
                                    2:  # case when there is a available position vertically higher than current row
                                for i in range(last_row+1):
                                    if myGraphics.board[last_row-i][color_col] == 0 and \
                                            (myGraphics.board[last_row][color_col] == 1 or
                                             myGraphics.board[last_row][color_col] == 2):
                                        myGraphics.board[last_row-i][color_col] = 1
                                        myGraphics.color(screen, color_col, 1, columns, last_row - i)
                                        turn = 2
                                        break
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass

                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            position_ai = random.choice(myGraphics.centers)  # at easy level AI puts piece on random
                            # position
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            color_col = int(position_ai[0][0]/(500/columns))
                            # print(color_col)
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 2
                                myGraphics.color(screen, color_col, 2, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 1
                            elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] ==\
                                    2:
                                for i in range(last_row+1):
                                    if myGraphics.board[last_row-i][color_col] == 0 and \
                                            (myGraphics.board[last_row][color_col] == 1 or
                                             myGraphics.board[last_row][color_col] == 2):
                                        myGraphics.board[last_row-i][color_col] = 2
                                        myGraphics.color(screen, color_col, 2, columns, last_row - i)
                                        turn = 1
                                        break
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                            else:
                                turn = 2
                # medium level strategy
                elif level == 2:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if turn == 1:
                            color_col = int(event.pos[0]/(500/columns))
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 1
                                myGraphics.color(screen, color_col, 1, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()

                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 2
                            elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] ==\
                                    2:
                                for i in range(last_row+1):
                                    if myGraphics.board[last_row-i][color_col] == 0 and \
                                            (myGraphics.board[last_row][color_col] == 1 or
                                             myGraphics.board[last_row][color_col] == 2):
                                        myGraphics.board[last_row-i][color_col] = 1
                                        myGraphics.color(screen, color_col, 1, columns, last_row - i)
                                        turn = 2
                                        break
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            if medium_flag:
                                position_ai = get_best_move()  # at a time position is calculated by the algorithm
                                print(position_ai)
                                color_col = position_ai[1]
                                medium_flag = False
                            else:
                                position_ai = random.choice(myGraphics.centers)  # another time it moves random
                                color_col = int(position_ai[0][0] / (500 / columns))
                                medium_flag = True
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 2
                                myGraphics.color(screen, color_col, 2, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 1
                            elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] ==\
                                    2:
                                for i in range(last_row + 1):
                                    if myGraphics.board[last_row - i][color_col] == 0 and \
                                            (myGraphics.board[last_row][color_col] == 1 or
                                             myGraphics.board[last_row][color_col] == 2):
                                        myGraphics.board[last_row - i][color_col] = 2
                                        myGraphics.color(screen, color_col, 2, columns, last_row - i)
                                        turn = 1
                                        break
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                            else:
                                turn = 2
                # hard level strategy
                elif level == 3:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if turn == 1:
                            color_col = int(event.pos[0]/(500/columns))
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 1
                                myGraphics.color(screen, color_col, 1, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()

                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 2
                            elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] ==\
                                    2:
                                for i in range(last_row+1):
                                    if myGraphics.board[last_row-i][color_col] == 0 and \
                                            (myGraphics.board[last_row][color_col] == 1 or
                                             myGraphics.board[last_row][color_col] == 2):
                                        myGraphics.board[last_row-i][color_col] = 1
                                        myGraphics.color(screen, color_col, 1, columns, last_row - i)
                                        turn = 2
                                        break
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass

                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            position_ai = get_best_move()  # AI everytime calculates a good position where to move
                            print(position_ai)
                            color_col = position_ai[1]
                            last_row = rows - 1
                            if last_row == -1:
                                break
                            if myGraphics.board[last_row][color_col] == 0:
                                myGraphics.board[last_row][color_col] = 2
                                myGraphics.color(screen, color_col, 2, columns, last_row)
                                if check_winner() == 1:
                                    myGraphics.load_final_win(screen)
                                    screen1 = False
                                    pygame.display.update()
                                elif check_winner() == 2:
                                    myGraphics.load_final_lose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 1
                            else:
                                turn = 2
            elif screen1 and play_human:  # player chose to play with a human opponent
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 1:
                        piece = 1
                    else:
                        piece = 2
                    color_col = int(event.pos[0]/(500/columns))
                    last_row = rows - 1
                    if last_row == -1:
                        break
                    if myGraphics.board[last_row][color_col] == 0:
                        myGraphics.board[last_row][color_col] = piece
                        myGraphics.color(screen, color_col, piece, columns, last_row)
                        if check_winner() == 1:
                            myGraphics.winner_player_screen(screen, "player 1")
                            screen1 = False
                            pygame.display.update()
                        elif check_winner() == 2:
                            myGraphics.winner_player_screen(screen, "player 2")
                            screen1 = False
                            pygame.display.update()
                        else:
                            pass
                        if check_last_row(last_row) == 0:
                            rows = rows - 1
                        if turn == 1:
                            turn = 2
                        else:
                            turn = 1
                    elif myGraphics.board[last_row][color_col] == 1 or myGraphics.board[last_row][color_col] == \
                            2:
                        for i in range(last_row + 1):
                            if myGraphics.board[last_row - i][color_col] == 0 and \
                                    (myGraphics.board[last_row][color_col] == 1 or
                                     myGraphics.board[last_row][color_col] == 2):
                                myGraphics.board[last_row - i][color_col] = piece
                                myGraphics.color(screen, color_col, piece, columns, last_row - i)
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                                break
                        if check_winner() == 1:
                            myGraphics.winner_player_screen(screen, "player 1")
                            screen1 = False
                            pygame.display.update()
                        elif check_winner() == 2:
                            myGraphics.winner_player_screen(screen, "player 2")
                            screen1 = False
                            pygame.display.update()
                        else:
                            pass
    pygame.quit()
