import os
from aux_functions import board_gen, whose_turn

coordinates = {1:'1', 2:'2', 3:'3', #Dictionary for navigating board coortinates with 1-9 input
               4:'4', 5:'5', 6:'6',
               7:'7', 8:'8', 9:'9'}

ongoing = True #Variable to track if the game still continues
turn = 0 #Variable to determine whether it's even (X) or odd (O) turn
turn_rep = -1 #Variable for error handling (turn to repeat)

while ongoing:
    os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
    board_gen(coordinates) #Generates playing board
    if turn_rep == turn: #Condition to handle an invalid input error
        print("Podałeś niewłaściwe pole, spróbój ponownie")
    turn_rep = turn
    print("Tura gracza " + str((turn % 2) + 1) + ". Wybierz pole (1-9) albo wpisz 'w' żeby wyjść") #UI message with player's turn indicator
    choice = input()
    if choice == 'w': #Quits game if the input is 'w'
        ongoing = False
    elif str.isdigit(choice) and int(choice) in coordinates: #Checks if input is a valid coordinate
        if not coordinates[int(choice)] in {'X', 'O'}: #Checks if selected field has already been taken by X or O
            turn += 1
            coordinates[int(choice)] = whose_turn(turn) #Fills selected field with current player's symbol (X or O)