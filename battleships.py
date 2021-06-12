import sys, os, time
import curses

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

battleships = [["C", "B", "D", "S", "P"], ["CCCCC", "BBBB", "DDD", "SSS", "PP"]]
battleshipStatus = ["", "", "", "", ""];

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
        if battleshipStatus[i] == "S":
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(5+i, xOffset, row1)
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(5+i, xOffset, row1)
            stdscr.attroff(curses.color_pair(1))

    curses.echo()

# https://gist.github.com/claymcleod/b670285f334acd56ad1c
def draw(stdscr):

    k = 0
    cursor = {"x": 20, "y": 5}
    cursorText = {"text": "", "index": -1}
    cursorTextOffset = 0
    cursorTextRot = 0
    boundsX = [20, 48]
    boundsY = [5, 14]
    xOffset = 20

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

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

        if cursorText["text"] == "":
            cursor["x"] = min(boundsX[1], cursor["x"])
            cursor["x"] = max(boundsX[0], cursor["x"])
            cursor["y"] = min(boundsY[1], cursor["y"])
            cursor["y"] = max(boundsY[0], cursor["y"])
        else:
            if k == ord('r'):
                cursorTextRot ^= 1

            if cursorTextRot == 0:
                cursor["x"] = min(boundsX[1]-(len(cursorText["text"])-cursorTextOffset)*2+2, cursor["x"])
                cursor["x"] = max(boundsX[0], cursor["x"])
                cursor["y"] = min(boundsY[1], cursor["y"])
                cursor["y"] = max(boundsY[0], cursor["y"])
            else:
                cursor["x"] = min(boundsX[1], cursor["x"])
                cursor["x"] = max(boundsX[0], cursor["x"])
                cursor["y"] = min(boundsY[1]-(len(cursorText["text"])-cursorTextOffset)+1, cursor["y"])
                cursor["y"] = max(boundsY[0]+cursorTextOffset, cursor["y"])

        # Turn on colors and bold
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        # Draw board
        if type == "condensed":
            xOffset = 0

        draw_board(stdscr, width, xOffset)
        draw_battleshipContainer(stdscr, width, xOffset)

        # Turn off color
        stdscr.attroff(curses.color_pair(1))







        # Selection
        if k == ord(' '):
            # Select based of a -5 offset
            listIndex = cursor["y"]-5
            if len(battleships[1]) > listIndex:
                selectedShip = battleships[1][listIndex]
                if cursor["x"] >= xOffset and cursor["x"] < xOffset+len(selectedShip):
                    cursorText["text"] = battleships[1][listIndex]
                    cursorText["index"] = listIndex
                    cursorTextOffset = (cursor["x"]-xOffset)
                    cursor["y"] = cursor["y"]
                    cursor["x"] = 30+(cursorTextOffset*2)
                    battleshipStatus[listIndex] = "S"
                    draw_battleshipContainer(stdscr, width, xOffset)

        # Draw ship on board
        if cursorText["text"] != "":
            if cursor["x"] > boundsX[0]+8:

                if cursorTextRot == 0:
                    # Invalid placement
                    if cursor["x"] < boundsX[0]+10+(cursorTextOffset*2):
                        stdscr.attron(curses.color_pair(3))
                    else:
                        stdscr.attroff(curses.color_pair(3))

                    stdscr.addstr(cursor["y"], cursor["x"]-(cursorTextOffset*2), str(" ".join(list(cursorText["text"]))))
                else:
                    # Invalid placement
                    if cursor["x"] < boundsX[0]+10:
                        stdscr.attron(curses.color_pair(3))
                    else:
                        stdscr.attroff(curses.color_pair(3))

                    for i in range(len(cursorText["text"])):
                        stdscr.addstr(cursor["y"]-cursorTextOffset+i, cursor["x"], cursorText["text"][0])

            else:
                # Deselection
                cursorText["text"] = ""
                battleshipStatus[cursorText["index"]] = ""
                cursor["x"] = 20
                cursor["y"] = 5
                cursorText["index"] = -1
                cursorTextRot = 0
                draw_battleshipContainer(stdscr, width, xOffset)




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
