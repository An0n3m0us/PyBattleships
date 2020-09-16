import sys, os, time
import curses

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

battleships = [["C", "B", "D", "S", "P"], ["CCCCC", "BBBB", "DDD", "SSS", "PP"]]

def centerString(width, string):
    return int((width // 2) - (len(string) // 2) - len(string) % 2)

def draw_board(stdscr, width):
    curses.noecho()

    row1 = "-------------------------------"[:width-1]
    row2 = "Player  1"[:width-1]
    row3 = "A B C D E F G H I J"[:width-1]

    stdscr.addstr(1, centerString(width, row1), row1)
    stdscr.addstr(3, centerString(width, row2), row2)
    stdscr.addstr(5, centerString(width, row3), row3)

    for i in range(10):
        row4 = "0 " + " ".join(board[0][i]) + " 0"[:width-1]
        stdscr.addstr(6+i, centerString(width, row4), row4.replace("0", str(i)))

    stdscr.addstr(16, centerString(width, row3), row3)
    stdscr.addstr(18, centerString(width, row1), row1)

    stdscr.addstr(20, 0, "({SHIP}{COLUMN}{ROW}{DIRECTION} ( 'CB3s' for Carrier B3 south))")
    stdscr.addstr(22, 0, "> "[:width-1])

    curses.echo()

def draw_battleshipContainer(stdscr, width):
    curses.noecho()

    for i in range(len(battleships[1])):
        row1 = battleships[1][i]
        stdscr.addstr(6+i, 14, row1)

    curses.echo()

# https://gist.github.com/claymcleod/b670285f334acd56ad1c
def draw(stdscr):

    k = 0
    cursor_x = 23
    cursor_y = 6
    cursorText = [-1, -1, -1]
    minMaxX = [14, 41]
    minMaxY = [6, 15]

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            if cursor_x > 20:
                cursor_x = cursor_x + 2
            else:
                cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            if cursor_x > 20:
                cursor_x = cursor_x - 2
            else:
                cursor_x = cursor_x - 1

        cursor_x = max(minMaxX[0], cursor_x)
        cursor_x = min(minMaxX[1], cursor_x)

        cursor_y = max(minMaxY[0], cursor_y)
        cursor_y = min(minMaxY[1], cursor_y)

        # Turn on colors and bold
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        # Draw board
        draw_board(stdscr, width)
        draw_battleshipContainer(stdscr, width)

        # Input
        """query = stdscr.getstr(22, 2, 4)
        query = list(str(query)[2:-1])

        if (len(query) == 4 and query[0].upper() in battleships[0] and query[1].upper() in columns and query[2].isdigit() and query[3].lower() in ["n", "e", "s", "w"]):
            ship = [query[0].upper(), battleships[0].index(query[0].upper())] # Char, index
            ship = [ship[0], ship[1], int(battleships[1][ship[1]][-2])] # Char, index, length

            column = int(columns[query[1].upper()])
            row = int(query[2])
            direction = [query[3].lower(), ""]

            # Check directions
            if direction[0] == "n" or direction[0] == "w":
                direction[1] = -1
            elif direction[0] == "s" or direction[0] == "e":
                direction[1] = 1

            # Check if ship can be placed based on length
            if (direction[0] == "n" or direction[0] == "s") and ((row+(ship[2]*direction[1])-direction[1]) in rows):
                emptyPositions = 0

                # Check if positions are empty
                for length in range(ship[2]):
                    length = length*direction[1]
                    posRow = list(board[0][row+length])
                    if posRow[column] == "-":
                        emptyPositions += 1

                # If positions are empty, place ship
                if emptyPositions == ship[2]:
                    for length in range(ship[2]):
                        length = length*direction[1]
                        posRow = list(board[0][row+length])
                        posRow[column] = ship[0]
                        board[0][row+length] = ''.join(posRow)
                    # Remove ship
                    battleships[0].pop(ship[1])
                    battleships[1].pop(ship[1])

            if (direction[0] == "e" or direction[0] == "w") and ((column+(ship[2]*direction[1])-direction[1]) in columns.values()):
                emptyPositions = 0

                # Check if positions are empty
                posColumn = list(board[0][row])
                for length in range(ship[2]):
                    length = length*direction[1]
                    if posColumn[column+length] == "-":
                        emptyPositions += 1

                # If positions are empty, place ship
                if emptyPositions == ship[2]:
                    for length in range(ship[2]):
                        length = length*direction[1]
                        posColumn[column+length] = ship[0]
                        board[0][row] = ''.join(posColumn)
                    # Remove ship
                    battleships[0].pop(ship[1])
                    battleships[1].pop(ship[1])"""

        # Turn off color
        stdscr.attroff(curses.color_pair(1))

        # Selection
        if k == ord(' '):

            for yRow in range(5):
                if cursor_y == 6+yRow and cursor_x >= 14 and cursor_x <= 19:
                    length = len(battleships[1][yRow])
                    for i in range(length):
                        if cursor_y == 6+yRow and cursor_x == 14+i:
                            cursorText = [yRow, 0-i, 0]
                            cursor_y = 6+yRow
                            cursor_x = 23+i*2

        if cursorText[0] != -1:
            if k == ord('r'):
                cursorText[2] ^= 1

            minMaxX[0] = 23 - cursorText[1]*2
            minMaxX[1] = 33 - cursorText[1]*2+(5-len(battleships[1][cursorText[0]]))*2

        # Move cursor
        if cursorText[2] == 0:
            stdscr.addstr(cursor_y, cursor_x+(cursorText[1]*2), " ".join(battleships[1][cursorText[0]]))
        elif cursorText[2] == 1:
            for i in range(len(battleships[1][cursorText[0]])):
                stdscr.addstr(cursor_y+i+cursorText[1], cursor_x, battleships[0][cursorText[0]])

        # Turn off bold
        stdscr.attroff(curses.A_BOLD)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        k = stdscr.getch()

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
