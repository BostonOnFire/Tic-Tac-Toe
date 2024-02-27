import os
from aux_functions import board_gen, whose_turn

coordinates = {1:'1', 2:'2', 3:'3',
               4:'4', 5:'5', 6:'6',
               7:'7', 8:'8', 9:'9'}

ongoing = True
turn = 0

while ongoing:
    os.system('cls' if os.name == 'nt' else 'clear')
    board_gen(coordinates)
    choice = input()
    if choice == 'q':
        ongoing = False
    turn += 1
    coordinates[int(choice)] = whose_turn(turn)