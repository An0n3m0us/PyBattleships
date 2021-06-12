import sys, os, time
import curses

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

battleships = [["C", "B", "D", "S", "P"], ["CCCCC", "BBBB", "DDD", "SSS", "PP"]]

def draw_board(stdscr, width, xOffset):

    curses.noecho()

    row1 = "-------------------------------"[:width-1]
    row2 = "Player  1"[:width-1]
    row3 = "A B C D E F G H I J"[:width-1]

    stdscr.addstr(0, 4+xOffset, row1)
    stdscr.addstr(2, 15+xOffset, row2)

    stdscr.addstr(4, 10+xOffset, row3)
    for i in range(10):
        row4 = "0 " + " ".join(board[0][i]) + " 0"[:width-1]
        stdscr.addstr(5+i, 8+xOffset, row4.replace("0", str(i)))

    stdscr.addstr(15, 10+xOffset, row3)
    stdscr.addstr(17, 4+xOffset, row1)

    curses.echo()

def draw_battleshipContainer(stdscr, width, xOffset):
    curses.noecho()

    for i in range(len(battleships[1])):
        row1 = battleships[1][i]
        stdscr.addstr(5+i, xOffset, row1)

    curses.echo()

# https://gist.github.com/claymcleod/b670285f334acd56ad1c
def draw(stdscr):

    k = 0
    cursor = {"x": 30, "y": 5}
    cursorText = ""
    boundsX = [20, 48]
    boundsY = [5, 14]
    xOffset = 20
    type = ""

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)

    while True:
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor["y"] = cursor["y"] + 1
        elif k == curses.KEY_UP:
            cursor["y"] = cursor["y"] - 1
        elif k == curses.KEY_RIGHT:
            if cursor["x"] > 23:
                cursor["x"] = cursor["x"] + 2
            else:
                cursor["x"] = cursor["x"] + 1
        elif k == curses.KEY_LEFT:
            if cursor["x"] > 25:
                cursor["x"] = cursor["x"] - 2
            else:
                cursor["x"] = cursor["x"] - 1

        if cursorText == "":
            cursor["x"] = min(boundsX[1], cursor["x"])
            cursor["x"] = max(boundsX[0], cursor["x"])
            cursor["y"] = min(boundsY[1], cursor["y"])
            cursor["y"] = max(boundsY[0], cursor["y"])
        else:
            cursor["x"] = min(boundsX[1]-(len(cursorText)-1), cursor["x"])
            cursor["x"] = max(boundsX[0]+10, cursor["x"])
            cursor["y"] = min(boundsY[1], cursor["y"])
            cursor["y"] = max(boundsY[0], cursor["y"])

        # Turn on colors and bold
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        # Draw board
        if type == "condensed":
            xOffset = 0

        draw_board(stdscr, width, xOffset)
        draw_battleshipContainer(stdscr, width, xOffset)

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
            stdscr.addstr(0, 0, str(cursor["x"]) + "," + str(cursor["y"]))

            # Select based of a -5 offset
            selectedShip = battleships[1][cursor["y"]-5]
            if cursor["x"] >= xOffset and cursor["x"] < xOffset+len(selectedShip):
                cursorText = str(" ".join(list(selectedShip)))
                cursor["y"] = cursor["y"]
                cursor["x"] = 30

        stdscr.addstr(cursor["y"], cursor["x"], cursorText)

        """if cursorText[0] != -1:
            # Disable ship in list
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(5+cursorText[0], 20, battleships[1][cursorText[0]])
            stdscr.attroff(curses.color_pair(2))

            if k == ord('r'):
                cursorText[2] ^= 1

            if cursorText[2] == 0:
                minMaxX[0] = 30+cursorText[1]*2
                minMaxX[1] = 48-(len(battleships[1][cursorText[0]])*2-cursorText[1]*2)+2
                minMaxY[0] = 5
                minMaxY[1] = 14

                #if cursor["x"]+cursorText[0] < minMaxX[0]:
                #    cursor["x"] = 30+cursorText[1]*2
                #elif cursor["x"]+cursorText[0] > minMaxX[1]:
                #    cursor["x"] = 30+cursorText[1]*2+len(battleships[1][cursorText[0]])*2


                stdscr.addstr(cursor["y"], cursor["x"]-(cursorText[1]*2), " ".join(battleships[1][cursorText[0]]))

            elif cursorText[2] == 1:
                minMaxX[0] = 30
                minMaxX[1] = 48
                minMaxY[0] = 5+cursorText[1]
                minMaxY[1] = 18-len(battleships[1][cursorText[0]])-(len(battleships[1][cursorText[0]])-cursorText[1])+2

                if cursor["y"]+cursorText[1] > minMaxY[1]:
                    cursor["y"] = minMaxY[1]-cursorText[1]

                for i in range(len(battleships[1][cursorText[0]])):
                    stdscr.addstr(cursor["y"]+i-cursorText[1], cursor["x"], battleships[0][cursorText[0]])"""

        # Turn off bold
        stdscr.attroff(curses.A_BOLD)

        stdscr.move(cursor["y"], cursor["x"])

        # Refresh the screen
        stdscr.refresh()

        k = stdscr.getch()

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
