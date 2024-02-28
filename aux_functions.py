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