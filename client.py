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
    global level
    my_level = input()
    if my_level == "1":
        level = 1
    elif my_level == "2":
        level = 2
    elif my_level == "3":
        level = 3


def check_last_row(last_r):
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
    # check horizontal combinations
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r][c + 1] == 1 and myGraphics.board[r][c + 2] == 1 and \
                    myGraphics.board[r][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r][c + 1] == 2 and myGraphics.board[r][c + 2] == 2 and \
                    myGraphics.board[r][c + 3] == 2:
                return 2
    # check vertical combinations
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r + 1][c] == 1 and myGraphics.board[r + 2][c] == 1 and \
                    myGraphics.board[r + 3][c] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r + 1][c] == 2 and myGraphics.board[r + 2][c] == 2 and \
                    myGraphics.board[r + 3][c] == 2:
                return 2
    # check main diagonal
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r + 1][c + 1] == 1 and\
                    myGraphics.board[r + 2][c + 2] == 1 and myGraphics.board[r + 3][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r + 1][c + 1] == 2 and \
                    myGraphics.board[r + 2][c + 2] == 2 and myGraphics.board[r + 3][c + 3] == 2:
                return 2
    # check on secondary diagonal
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if myGraphics.board[r][c] == 1 and myGraphics.board[r - 1][c + 1] == 1 and \
                    myGraphics.board[r - 2][c + 2] == 1 and myGraphics.board[r - 3][c + 3] == 1:
                return 1
            if myGraphics.board[r][c] == 2 and myGraphics.board[r - 1][c + 1] == 2 and \
                    myGraphics.board[r - 2][c + 2] == 2 and myGraphics.board[r - 3][c + 3] == 2:
                return 2
    return 3


def get_best_move():
    directions = list()
    for column in range(COLUMNS):
        for row in range(ROWS):
            if myGraphics.board[row][column] == 1:
                if column-1 >= 0 and myGraphics.board[row][column-1] == 0:
                    # print("possible position", (row, column - 1))
                    directions.append((row, column - 1))
                if column+1 < COLUMNS and myGraphics.board[row][column+1] == 0:
                    # print("possible position", (row, column + 1))
                    directions.append((row, column + 1))
                if row-1 >= 0 and myGraphics.board[row-1][column] == 0:
                    # print("possible position", (row - 1, column))
                    directions.append((row - 1, column))
    if len(directions) > 0:
        return random.choice(directions)


if __name__ == "__main__":
    global columns, rows, turn, level, first_player_human
    running = True
    screen1 = True  # board screen
    play_human = False
    medium_flag = True
    draw_score = 0
    if len(sys.argv) == 5:
        if sys.argv[1] == "computer":
            # print(sys.argv[1])
            play_human = False
        elif sys.argv[1] == "human":
            play_human = True
        else:
            print("Invalid arguments")
            sys.exit()
        if int(sys.argv[2]) > 3 and 3 < int(sys.argv[3]) < int(sys.argv[2]):
            # print(sys.argv[2], sys.argv[3])
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
            for c in range(COLUMNS):
                for r in range(ROWS):
                    if myGraphics.board[r][c] != 0:
                        draw_score = draw_score + 0
                    else:
                        draw_score = draw_score + 1
            if draw_score == 0:
                myGraphics.draw(screen)
                pygame.display.update()
            if screen1 and not play_human:
                # easy level algorithm
                if level == 1:
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                    # pass
                                # for r in range(rows):
                                #     print(myGraphics.board[r])
                                # print()
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass

                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            position_ai = random.choice(myGraphics.centers)
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
                                    myGraphics.load_final_loose(screen)
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
                                    myGraphics.load_final_loose(screen)
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                    # pass
                                # for r in range(rows):
                                #     print(myGraphics.board[r])
                                # print()
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            if medium_flag:
                                position_ai = get_best_move()
                                print(position_ai)
                                color_col = position_ai[1]
                                medium_flag = False
                            else:
                                position_ai = random.choice(myGraphics.centers)
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
                                    myGraphics.load_final_loose(screen)
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
                                    myGraphics.load_final_loose(screen)
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
                                    myGraphics.load_final_loose(screen)
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass

                            else:
                                turn = 1
                    else:
                        if turn == 2:
                            position_ai = get_best_move()
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
                                    myGraphics.load_final_loose(screen)
                                    screen1 = False
                                    pygame.display.update()
                                else:
                                    pass
                                if check_last_row(last_row) == 0:
                                    rows = rows - 1
                                turn = 1
                            else:
                                turn = 2
            elif screen1 and play_human:
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
