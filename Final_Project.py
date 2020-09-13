"""
CS1311
Thomas Oswald
Zack Lignore
FINAL PROJECT
"""
# REFERENCES
# https://docs.python.org/2/library/tkinter.html
# http://effbot.org/tkinterbook/button.htm
# http://effbot.org/tkinterbook/variable.htm
# https://effbot.org/tkinterbook/widget.htm
# https://www.programiz.com/python-programming/global-local-nonlocal-variables
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
# https://pythonspot.com/tk-message-box/

import random
from tkinter import *
from tkinter import messagebox



# Input player names
player_1 = str(input('Please enter your name player 1: '))
player_2 = str(input('Please enter your name player 2: '))

game_num = [0]
winner = []
p1_score = 0
p2_score = 0

#Determines who will go first
def order():
    global p1_str
    global p2_str
    p1_num = 0
    p2_num = 0
    
    while p1_num == p2_num:
        p1_num = random.randint(0, 10)
        p2_num = random.randint(0, 10)
        
    if p1_num > p2_num:
        print()
        print(player_1,'will will go first')
        print(player_1,'will have the "X" marker')
        print()
        print(player_2,'will go second')
        print(player_2,'will have the "O" marker')
        print()
        p1_str = 'x'
        p2_str = 'o'
    else:
        print()
        print(player_2,'will will go first')
        print(player_2,'will have the "X" marker')
        print()
        print(player_1,'will go second')
        print(player_1,'will have the "O" marker')
        print()
        p1_str = 'o'
        p2_str = 'x'

print()        
print('Game', len(game_num))
order()
# Creating the title and grid for tic-tac-toe board
    
board = Tk()
board.title('Tic-Tac-Toe!')
board.geometry('300x325')
board.config(bg = 'black')


## Buttons on tic-tac-toe board
b1 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b1))
b1.place(x = 0, y = 0)
b2 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b2))
b2.place(x = 100, y = 0)
b3 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b3))
b3.place(x = 200, y = 0)
b4 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b4))
b4.place(x = 0, y = 100)
b5 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b5))
b5.place(x = 100, y = 100)
b6 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b6))
b6.place(x = 200, y = 100)
b7 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b7))
b7.place(x = 0, y = 200)
b8 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b8))
b8.place(x = 100, y = 200)
b9 = Button(board, text = 'select here', height = 6, width = 13, command = lambda:click(b9))
b9.place(x = 200, y = 200)
replay = Button(board, text = 'Restart', height = 1, width = 20, command = lambda:restart(replay))
replay.place(x = 0, y = 300)
replay.config(bg = 'light green')
stop = Button(board, text = 'Quit', height = 1, width = 20, command = lambda:end_game(stop))
stop.place(x = 150, y = 300)
stop.config(bg = 'salmon')
buttons = StringVar()


#Allows buttons to be used and stores data to determine winner
marker = 1
def click(buttons):
    global marker
    global winner
    global p1_score
    global p2_score
     
    for i in range(1, 9):
        if buttons['text'] == 'select here' and marker == 1:
            buttons['text'] = 'X'
            buttons.config(relief = SUNKEN)
            marker = 2
            
            winner.append(b1.cget('text'))
            winner.append(b2.cget('text'))
            winner.append(b3.cget('text'))
            winner.append(b4.cget('text'))
            winner.append(b5.cget('text'))
            winner.append(b6.cget('text'))
            winner.append(b7.cget('text'))
            winner.append(b8.cget('text'))
            winner.append(b9.cget('text'))
            

        elif buttons['text'] == 'select here' and marker == 2:
            buttons['text'] = 'O'
            buttons.config(relief = SUNKEN)
            marker = 1
            
            winner.append(b1.cget('text'))
            winner.append(b2.cget('text'))
            winner.append(b3.cget('text'))
            winner.append(b4.cget('text'))
            winner.append(b5.cget('text'))
            winner.append(b6.cget('text'))
            winner.append(b7.cget('text'))
            winner.append(b8.cget('text'))
            winner.append(b9.cget('text'))
            

    if (winner[-9] == 'X') and (winner[-8] == 'X') and (winner[-7] == 'X') or \
        (winner[-6] == 'X') and (winner[-5] == 'X') and (winner[-4] == 'X') or \
        (winner[-3] == 'X') and (winner[-2] == 'X') and (winner[-1] == 'X') or \
        (winner[-9] == 'X') and (winner[-6] == 'X') and (winner[-3] == 'X') or \
        (winner[-8] == 'X') and (winner[-5] == 'X') and (winner[-2] == 'X') or \
        (winner[-7] == 'X') and (winner[-4] == 'X') and (winner[-1] == 'X') or \
        (winner[-9] == 'X') and (winner[-5] == 'X') and (winner[-1] == 'X') or \
        (winner[-7] == 'X') and (winner[-5] == 'X') and (winner[-3] == 'X'):
        if p1_str == 'x':
            p1_score += 1
            messagebox.showinfo('Game over', 'Player 1 wins!')
            
        else:
            p2_score += 1
            messagebox.showinfo('Game Over', 'Player 2 wins!')
        
    elif (winner[-9] == 'O') and (winner[-8] == 'O') and (winner[-7] == 'O') or \
        (winner[-6] == 'O') and (winner[-5] == 'O') and (winner[-4] == 'O') or \
        (winner[-3] == 'O') and (winner[-2] == 'O') and (winner[-1] == 'O') or \
        (winner[-9] == 'O') and (winner[-6] == 'O') and (winner[-3] == 'O') or \
        (winner[-8] == 'O') and (winner[-5] == 'O') and (winner[-2] == 'O') or \
        (winner[-7] == 'O') and (winner[-4] == 'O') and (winner[-1] == 'O') or \
        (winner[-9] == 'O') and (winner[-5] == 'O') and (winner[-1] == 'O') or \
        (winner[-7] == 'O') and (winner[-5] == 'O') and (winner[-3] == 'O'):
        if p1_str == 'o':
            p1_score += 1
            messagebox.showinfo('Game over', 'Player 1 wins!')
            
        else:
            p2_score += 1
            messagebox.showinfo('Game over', 'Player 2 wins!')
        
    elif (winner[-9] != 'select here') and (winner[-8] != 'select here') and \
         (winner[-7] != 'select here') and (winner[-6] != 'select here') and \
         (winner[-5] != 'select here') and (winner[-4] != 'select here') and \
         (winner[-3] != 'select here') and (winner[-2] != 'select here') and \
         (winner[-1] != 'select here'):
        messagebox.showinfo('Game Over', 'Try Again')
     
#Allows restart of the game
def restart(replay):
    print()
    print('Game', len(game_num) + 1)
    order()
    global marker
    marker = 1
    b1.config(text='select here',relief = RAISED)
    b2.config(text='select here',relief = RAISED)
    b3.config(text='select here',relief = RAISED)
    b4.config(text='select here',relief = RAISED)
    b5.config(text='select here',relief = RAISED)
    b6.config(text='select here',relief = RAISED)
    b7.config(text='select here',relief = RAISED)
    b8.config(text='select here',relief = RAISED)
    b9.config(text='select here',relief = RAISED)
    game_num.append(1)

    
 #Ends the game   
def end_game(stop):
    print()
    print(player_1,'won',p1_score,'games')
    print(player_2,'won',p2_score,'games')
    if (p1_score + p2_score) < len(game_num):
        print((len(game_num)- 1) - (p1_score + p2_score),'Tie games')
    board.destroy()

mainloop()