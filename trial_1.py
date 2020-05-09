from IPython.display import clear_output
import random
def welcome():
    print("Welcome to Crude Tic tak Toe")
    print("Instruction : \n the number pad is for the position in the game board.\n That's It  ")

current_values=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def game_board(values):
    clear_output()
    print(' '+values[7]+' |'+" "+values[8]+' |'+" "+values[9]+'\n'
          ' '+values[4]+' |'+" "+values[5]+' |'+" "+values[6]+'\n'
         ' '+values[1]+' |'+" "+values[2]+' |'+" "+values[3]+'\n')

player1=""
player2=""
def player():
    global player1
    global player2
    player1 =input('PLayer1 choose X or O :   ').upper()
    if player1=='X':
         player2='O'
    else :
        player2='X'



def who_first():
    x = random.randint(0, 2)
    if x == 1:
        print("player 1 goes First")
        return player1
    else:
        print("player 2 goes first")
        return player2


def win_check(current_values,symbol):
    return((current_values[1]==current_values[2]==current_values[3]==symbol)or   #buttom row
           (current_values[4]==current_values[5]==current_values[6]==symbol)or   #middle row
           (current_values[7]==current_values[8]==current_values[9]==symbol)or   #top row
           (current_values[1]==current_values[4]==current_values[7]==symbol)or   #first colm
           (current_values[2]==current_values[5]==current_values[8]==symbol)or   #middle colm
           (current_values[3]==current_values[6]==current_values[9]==symbol)or   #last colm
           (current_values[1]==current_values[5]==current_values[9]==symbol)or   #diagonal 1
           (current_values[3]==current_values[5]==current_values[7]==symbol))  #diagonal 2


turn = symbol = who_first()


def player_switch():
    global symbol

    if turn == player1:
        print("Player2's turn")
        symbol = player2
    else:
        print("player 1's turn")
        symbol = player1
    return symbol

def player_input(current_values,symbol):
    global game_on
    num = int(input("Enter the position"))
    current_values[num]=symbol
    if win_check(current_values,symbol):
        game_on = False
        return game_on
def draw_check(values):
    pass



welcome()
game_board(current_values)
player()

game_on =True
while game_on:
    turn =player_switch()
    game_board(current_values)
    player_input(current_values,symbol)

print(" \n \ncongo %s wins \n"%turn)
game_board(current_values)

#draw ka baki hai
#doesnt print the name of player who won
#restart ka option