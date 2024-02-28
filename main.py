import os
from aux_functions import board_gen, whose_turn, win_condition

coordinates = {1:'1', 2:'2', 3:'3', #Dictionary for navigating board coortinates with 1-9 input
               4:'4', 5:'5', 6:'6',
               7:'7', 8:'8', 9:'9'}

#Function containing core gameplay
def gameplay():
    ongoing = True #Variable to track if the game still continues
    finished = False
    turn = 0 #Variable to determine whether it's even (X) or odd (O) turn
    turn_rep = -1 #Variable for error handling (turn to repeat)
    coordinates.update({1:'1', 2:'2', 3:'3', #Board reset before game start
                        4:'4', 5:'5', 6:'6',
                        7:'7', 8:'8', 9:'9'})
    while ongoing:
        os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
        print("Witaj w grze Kółko i Krzyżyk!")
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
        if win_condition(coordinates):
            ongoing, finished = False, True
        if turn > 8:
            ongoing = False
    os.system('cls' if os.name == 'nt' else 'clear') #Clears screen one last time
    board_gen(coordinates) #Generates end board state
    #Statement shows the winner or a draw if there's none and writes the result into txt file
    if finished:
        if whose_turn(turn) == 'X':
            print("Gracz 1 wygrywa! Gratulacje!")
            wynik = open("wyniki.txt", "a")
            wynik.write("Gracz 1 wygrywa!")
            wynik.close()
        else:
            print("Gracz 2 wygrywa! Gratulacje!")
            wynik = open("wyniki.txt", "a")
            wynik.write("Gracz 2 wygrywa!")
            wynik.close()
    else:
        print("Remis")
        wynik = open("wyniki.txt", "a")
        wynik.write("Remis")
        wynik.close()

#Main menu function
def main():
    while True:
        gameplay()
        replay = input("Chcesz zegrać jeszcze raz? y/n?") == 'y'
        if not replay:
            return
        
main()