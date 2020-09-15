import time

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
directions = {"n": 0, "e": 1, "s": 2, "w": 3}

battleships = ["[C]arrier(5)", "[B]attleship(4)", "[D]estroyer(3)", "[S]ubmarine(3)", "[P]atrol Boat(2)"]
battleshipChars = ["C", "B", "D", "S", "P"]

def boardDisplay(playerIndex):
    return """
-------------------------------

           Player  """ + str(playerIndex+1) + """

      A B C D E F G H I J
    0 """ + " ".join(board[playerIndex][0]) + """ 0
    1 """ + " ".join(board[playerIndex][1]) + """ 1
    2 """ + " ".join(board[playerIndex][2]) + """ 2
    3 """ + " ".join(board[playerIndex][3]) + """ 3
    4 """ + " ".join(board[playerIndex][4]) + """ 4
    5 """ + " ".join(board[playerIndex][5]) + """ 5
    6 """ + " ".join(board[playerIndex][6]) + """ 6
    7 """ + " ".join(board[playerIndex][7]) + """ 7
    8 """ + " ".join(board[playerIndex][8]) + """ 8
    9 """ + " ".join(board[playerIndex][9]) + """ 9
      A B C D E F G H I J

-------------------------------
    """

print(boardDisplay(0))

print("Battleships: " + ", ".join(battleships))
print("Place a battleship (Use nesw to pick direction (e.g: C0An))")

query = list(input("Place destroyer: "))

# Loop until correct format given
while not (len(query) == 4 and query[0].upper() in battleshipChars and query[1].isdigit() and query[2].upper() in columns and query[3].lower() in directions):
    query = list(input("Place destroyer: "))
else:
    # Set variables
    battleship = battleshipChars.index(query[0].upper()) # Get index
    battleship = [battleship, int(battleships[battleship][-2])] # Index, length
    row = int(query[1])
    column = columns[query[2].upper()]
    direction = directions[query[3].lower()]

    posRow = list(board[0][row])
    posRow[column] = "O"
    board[0][row] = ''.join(posRow)

    del battleships[battleship[0]]
    del battleshipChars[battleship[0]]

    print(boardDisplay(0))
    print(battleships)
    print(battleshipChars)
