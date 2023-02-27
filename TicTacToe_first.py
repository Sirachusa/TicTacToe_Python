# Displaying the board:

def display_board(board):
    
    print('\n'*100)
    
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')

# Choose a mark for Player1 and Player2

def player_input():
    
    mark = ''
    
    while mark not in ['X','O']:
        
        mark = input('Please choose a mark for Player1: (X or O) ').upper()
        
        if mark == 'X':
            
            return ('X','O')
        
        else:
            
            return ('O','X')
        
        
# Place a marker to desired position:

def place_marker(board, marker, position):
    
    board[position] = marker
    
# Check if one of the marker win | ROWS, COLUMNS, DIAGONALS

def win_check(board, mark):
    
    x_win = 'XXX'
    o_win = 'OOO'
    
    if   (board[1]+board[2]+board[3] == x_win) or \
         (board[4]+board[5]+board[6] == x_win) or \
         (board[7]+board[8]+board[9] == x_win) or \
         (board[1]+board[4]+board[7] == x_win) or \
         (board[2]+board[5]+board[8] == x_win) or \
         (board[3]+board[6]+board[9] == x_win) or \
         (board[1]+board[5]+board[9] == x_win) or \
         (board[3]+board[5]+board[7] == x_win):
        
        return True
    
    elif (board[1]+board[2]+board[3] == o_win) or \
         (board[4]+board[5]+board[6] == o_win) or \
         (board[7]+board[7]+board[9] == o_win) or \
         (board[1]+board[4]+board[7] == o_win) or \
         (board[2]+board[5]+board[8] == o_win) or \
         (board[3]+board[6]+board[9] == o_win) or \
         (board[1]+board[5]+board[9] == o_win) or \
         (board[3]+board[5]+board[7] == o_win):
        
        return True
    
    else:
        return False 

    
# Randomize whos begin the game:

import random

def choose_first():
    
    first = random.randint(0,1)
    
    if first == 0:
        return 'Player1'
    else:
        return 'Player2'

    
# Check the position is avalaible:

def space_check(board, position):
    
    return board[position] == ' ' 


# Check the board is filled or not:

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False      
    
    return True    


# input for the position, if the position is not free, the while loop ask again and print the space is occupied.

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9]:
        
        position = int(input('Please give a position for your mark: (1-9) '))
        
        if space_check(board,position) == False:
            
            print('This position is taken, please give another:')
            position = 0
        
        elif space_check(board,position):
            return position

# Just a question for replay:        
        
def replay():
    
    play_again = input('Do you wanna play another match? (Y or N) ').upper()
    
    return play_again == 'Y'


# Setup the whole game: [ the hardest part for me :) ]

def play_the_game():

    print('Welcome my first TicTacToe game with Python!! :)')
    
# While loop keep running the game
    while True:
        # Play the game!
        
        ## Set everything up (board,who's first, markers)
        board = ['_',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player1_mark, player2_mark = player_input()
        
        turn = choose_first()
        print(turn + ' begin the game!')
        
        game_on = True
        
        ## Game play.
        
        while game_on:
            
            # Player 1 turn
            
            if turn == 'Player1':

                # Show the board
                display_board(board)

                # Choose a position
                position = player_choice(board)

                # Place marker
                place_marker(board,player1_mark,position)

                # Check if win
                if win_check(board, player1_mark):
                    display_board(board)
                    print('Player 1 won!')
                    game_on = False

                # Check if tie
                else:
                    if  full_board_check(board):
                        display_board(board)
                        print("It's a tie! Nice play!")
                        break
                    else:
                        turn = 'Player2'
            
            # Player2 turn
            
            elif turn == 'Player2':

                # Show the board
                display_board(board)

                # Choose a position
                position = player_choice(board)

                # Place marker
                place_marker(board,player2_mark,position)

                # Check if win
                if win_check(board, player2_mark):
                    display_board(board)
                    print('Player 2 won!')
                    game_on = False

                # Check if tie
                else:
                    if  full_board_check(board):
                        display_board(board)
                        print("It's a tie! Nice play!")
                        break
                    else:
                        turn = 'Player1'

# Break out from the loop with replay()

        if replay() == False:
            break

play_the_game()
