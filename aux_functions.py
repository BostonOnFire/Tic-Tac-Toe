#Function for board generation
def board_gen(coordinates):
    board = (f"|{coordinates[1]}|{coordinates[2]}|{coordinates[3]}|\n"
             f"|{coordinates[4]}|{coordinates[5]}|{coordinates[6]}|\n"
             f"|{coordinates[7]}|{coordinates[8]}|{coordinates[9]}|")
    print(board)

#Function for turn switching between X and O
def whose_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else: return 'X'

#Function to check if somebody's won
def win_condition(coordinates):
    #Horizontal check
    if (coordinates[1] == coordinates[2] == coordinates [3])\
    or (coordinates[4] == coordinates[5] == coordinates [6])\
    or (coordinates[7] == coordinates[8] == coordinates [9]):
        return True
    #Vertical check
    elif (coordinates[1] == coordinates[4] == coordinates [7])\
    or (coordinates[2] == coordinates[5] == coordinates [8])\
    or (coordinates[3] == coordinates[6] == coordinates [9]):
        return True
    #Diagonal check
    elif (coordinates[1] == coordinates[5] == coordinates [9])\
    or (coordinates[3] == coordinates[5] == coordinates [7]):
        return True
    else:
        return False