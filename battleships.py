import time

board = [["----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------", "----------"]]

rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

battleships = [["C", "B", "D", "S", "P"], ["[C]arrier(5)", "[B]attleship(4)", "[D]estroyer(3)", "[S]ubmarine(3)", "[P]atrol Boat(2)"]]

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

def inputCoordinates():
    print("Battleships: " + ", ".join(battleships[1]))
    return list(input("Coordinates: "))

# MAIN CODE

print("\n\nINSTRUCTIONS: Use n, s, e, w to pick direction (e.g: CB3s for Carrier B3 south)\n\n")
#input("") # ENABLE THIS LATER
print(boardDisplay(0))

# Loop until correct format given
while len(battleships[0]) != 0:

    query = inputCoordinates()

    if (len(query) == 4 and query[0].upper() in battleships[0] and query[1].upper() in columns and query[2].isdigit() and query[3].lower() in ["n", "e", "s", "w"]):
        ship = [query[0].upper(), battleships[0].index(query[0].upper())] # Char, index
        ship = [ship[0], ship[1], int(battleships[1][ship[1]][-2])] # Char, index, length

        column = int(columns[query[1].upper()])
        row = int(query[2])
        direction = [query[3].lower(), ""]

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
                battleships[1].pop(ship[1])

        print(boardDisplay(0))
    
