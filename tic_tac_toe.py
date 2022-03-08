#from IPython.display import clear_output

def display_board(board):
    #clear_output()
    #print('_ '+'_ '+'_ ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    #print('_ '+'_ '+'_ ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    #print('_ '+'_ '+'_ ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    #print('_ '+'_ '+'_ ')

#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#display_board(test_board)

def player_input():

    answer = ''
    correct_answer = ['X', 'O']

    #keep asking player 1 to choose X or O
    while answer not in correct_answer:
        answer = input("Player 1, please choose X or O: ").upper()

    #assign player 2, the opposite answer
    player1 = answer

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

#player1, player2 = player_input()
#print(player_input())

#function that takes in the board list object, ('X' or 'O'), and a desired position (1-9) and assins it to the board
def place_marker(board, marker, position):
    
    board[position] = marker

#place_marker(test_board, '$', 8)
#display_board(test_board)

#function that takes in a board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or 
           (board[3] == board[5] == board[7] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[1] == board[4] == board[6] == mark) or
           (board[2] == board[5] == board[7] == mark) or
           (board[3] == board[6] == board[9] == mark))

#print(win_check(test_board, 'X'))

#function that uses the random module to randomly decide which player goes first
#you may want to lookup random.randint() Return a string of which player went first
import random
from turtle import pos, position
def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):

    return board[position] == ' '

#function that checks if the board is full and returns a boolean value
#true if full, false otherwise
def full_board_check(board):

    for b in range(1,10):
        if space_check(board,b):
            return False

    return True

#function that asks for a player's next postion (1-9) and then uses the function space_check to check if it's a free position
#if it is, then return the position for later use
def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please choose your next position: (1-9) "))
    
    return position

#function that asks the player if they want to play again and returns a boolean
#true if they do want to play again
def replay():

    answer = input("Please enter Y if you want to play again or N if you do not: ")
    if answer == 'Y':
        return True
    else:
        return False

#use while loops and the functions you've made to run the game!

print('Welcome to Tic Tac Toe!')

#while True:
    #Set the game up here
    #pass

    #while game_on:
        #Player 1 turn

        #Player 2 turn

            #pass
    
    #if not replay()
        #break

#while  loop to keep running the game
while True:
    
    #play the game

    #set everything up (board, whos first, choose markers X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first ")

    play_game = input('Ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #game play

    while game_on:

        if turn == 'Player 1':
        #player one turn

            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player1_marker, position)
            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                game_on = False
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
            #no tie and no win? then next player's turn
                else:
                    turn = 'Player 2'

        #player two turn
        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player2_marker, position)
            #check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 WON!")
                game_on = False
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    print("TIE GAME!")
                    break
            #no tie and no win? then next player's turn
                else:
                    turn = 'Player 1'

    if not replay():
        break
#break out of the while loop on replay()


    