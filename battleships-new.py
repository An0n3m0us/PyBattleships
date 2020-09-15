import sys, os, time
import curses

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

def centerString(width, string):
    return int((width // 2) - (len(string) // 2) - len(string) % 2)

# https://gist.github.com/claymcleod/b670285f334acd56ad1c
def draw_menu(stdscr):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        row1 = "-------------------------------"[:width-1]
        row2 = "Player  1"[:width-1]
        row3 = "A B C D E F G H I J"[:width-1]

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        # Rendering title

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

        # Turn on input
        curses.echo()
        s = stdscr.getstr(22, 2, 4)
        board[0][0] = "---x------"

        # Turning off attributes for title
        stdscr.attron(curses.color_pair(1))
        stdscr.attroff(curses.A_BOLD)

        # Refresh the screen
        stdscr.refresh()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
