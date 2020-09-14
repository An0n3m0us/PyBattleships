import time

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]


def boardDisplay(playerIndex):
    return """
            Player """ + str(playerIndex+1) + """

           ABCDEFGHIJ
         0 """ + board[playerIndex][0] + """ 0
         1 """ + board[playerIndex][1] + """ 1
         2 """ + board[playerIndex][2] + """ 2
         3 """ + board[playerIndex][3] + """ 3
         4 """ + board[playerIndex][4] + """ 4
         5 """ + board[playerIndex][5] + """ 5
         6 """ + board[playerIndex][6] + """ 6
         7 """ + board[playerIndex][7] + """ 7
         8 """ + board[playerIndex][8] + """ 8
         9 """ + board[playerIndex][9] + """ 9
           ABCDEFGHIJ
    """

print(boardDisplay(0))
print("Place your destroyer (input r to rotate or (example) A0 to place)")
input("Place destroyer: ")
