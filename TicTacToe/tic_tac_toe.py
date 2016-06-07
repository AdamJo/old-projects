###################################################################
#  1 player tic tac toe with an AI.                               #
#  Rules: Connect three in a row to win.                          #
#         Who ever wins the coin toss for X, goes first.          #
#         If grid is full and no combinations of three are made   #
#         the game is a draw.                                     #
###################################################################

import random
import sys 

# Outputs the tic tac toe table in a 3 x 3 grid
def output( ):

    print ''
    print table[1] + ' | ' + table[2] + ' | ' + table[3]
    print '_________'
    print table[4] + ' | ' + table[5] + ' | ' + table[6]
    print '_________'
    print table[7] + ' | ' + table[8] + ' | ' + table[9]
    print ''

#Asks for user input for next move
#If input is already taken it will ask for a new input.
#return - N/A
def player_1():
    output()
    player_wins = ('\n***Player Wins***')
    player_input = input("Enter Position: ")
    
    while True:
        end = grid(player_input, user, player_wins)
        if end == False:
            output()
            player_input = input("Enter a unused position: ")
        else:
            break

#calculates the next move for the AI.
#return - N/A
def dumb_AI():
    computer_wins = ('\n***Computer Wins***')
    corners = [1,3,7,9]
    end = False

    #First: determines if middle point is open.
    #Second: determines if corners are open.
    #Third: Defaults to a random position that is still open.
    while True:
        if table[5] == '5':
            AI_input = 5
            end = grid(AI_input, computer, computer_wins)

        elif ( table[1] == '1' or table[3] == '3' or
               table[7] == '7' or table[9] == '9'):
            random.shuffle(corners)
            AI_input = corners[0]
            end = grid(AI_input, computer, computer_wins)

        else:
            AI_input = random.randint(1,9)
            end = grid(AI_input, computer, computer_wins)

        if end == True:
            break

#Parameters: position - User/Computer input position
#            result - User/Computer X or O symbol
#            evaluate - Displays the user/computer winning banner
#                       to be used with evaluate method.
#return - False is table position is already used, True if is not.
def grid(position, result, banner):
    if (table[position] == 'X' or table[position] == 'O'):
        return False
    else:
        table[position] = result
        checker(banner)
        draw()
        return True

#Parameters - The banner is used to determine who had the
#             winning connection
#return - N/A.
def checker(banner):
    count = 0
    dictionary = { #rows
                   1: table[1] + table[2] + table[3],
                   2: table[4] + table[5] + table[6],
                   3: table[7] + table[8] + table[9],
                   #columns  
                   4: table[1] + table[4] + table[7],
                   5: table[2] + table[5] + table[8],
                   6: table[3] + table[6] + table[9],
                   #diagnols
                   7: table[1] + table[5] + table[9],
                   8: table[3] + table[5] + table[7],
                 }

    for entry in dictionary:
        solving = dictionary[entry]
        evaluate(solving, banner)

#Determines if game board is full and should end in a draw.
#returns - N/A
def draw():
    count = 0
    X_mark = ord('X')
    O_mark = ord('O')

    for i in range(1, 10):
        if  table[i] == 'X' or table[i] == 'O':
            count += 1

    if count == 9:
        print "\nGame ended in draw",
        output()
        sys.exit()

#Parameters - Solved: The row/column/diagnol that is being
#                     checked
#             Banner: Used to determine who the winner is and display a
#                     banner for the winner
#Return - N/A
def evaluate(solved, banner):
    if solved == 'XXX' or solved == 'OOO':
        print banner
        output()
        sys.exit()

#Defines the 3x3 table used for the tic tac toe board
#Tosses a coin and user choses either heads or tails.
#If user prediction is correct player is X goes first.
#
#Returns - Player and AI either assigned as X or O depending on coin toss
def new_game():
    global table
    AI, player, user_Input = ' ', ' ', -1
    table = [0,'1','2','3','4','5','6','7','8','9']
    coin_Toss = random.randint(0,1)

    while True:
        user_Input = input('Coin toss for first move ' +
                           ' \n ->choose 0 or 1 (heads or tails) : ')
        if user_Input == 0 or user_Input == 1:
            break

    if user_Input != coin_Toss:
        print coin_Toss
        print ' /--------------------------\\'
        print '| Computer won the coin toss |'
        print ' \--------------------------/'
        AI = 'X'
        player = 'O'
    else:
        print ' /-----------------------\\'
        print '| Player won the coin toss|'
        print ' \-----------------------/'
        player = 'X'
        AI = 'O'

    return player, AI

##################################################################

user, computer = new_game()

#In tic tac toe, X always goes first.
while True:
    if user == 'X':
        player_1()
        dumb_AI()
    else:
        dumb_AI()
        player_1()
