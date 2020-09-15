import sys, os, time
import curses

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

battleships = [["C", "B", "D", "S", "P"], ["[C]arrier(5)", "[B]attleship(4)", "[D]estroyer(3)", "[S]ubmarine(3)", "[P]atrol Boat(2)"]]

def centerString(width, string):
    return int((width // 2) - (len(string) // 2) - len(string) % 2)

def draw_board(stdscr, width):
    curses.noecho()

    row1 = "-------------------------------"[:width-1]
    row2 = "Player  1"[:width-1]
    row3 = "A B C D E F G H I J"[:width-1]

    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)

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
        stdscr.addstr(6+i*2, 5, row1)
    
    curses.echo()

# https://gist.github.com/claymcleod/b670285f334acd56ad1c
def draw(stdscr):
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

        # Draw board
        draw_board(stdscr, width)
        draw_battleshipContainer(stdscr, width)

        # Turn on input
        s = stdscr.getstr(22, 2, 4)
        board[0][0] = "---x------"

        # Turning off attributes for title
        stdscr.attron(curses.color_pair(1))
        stdscr.attroff(curses.A_BOLD)

        # Refresh the screen
        stdscr.refresh()

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
