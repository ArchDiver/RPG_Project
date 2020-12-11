# Python text RPG
# following https://www.youtube.com/watch?v=xHPmXArK6Tg
# This version made by Leland S. Crawford (ArchDiver)

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player Setup ###
class Player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.feeling = ''
        self.asrtology = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
        self.won = False
        self.solves = 0

myPlayer = Player()

#### Map ####
"""
-Player starts at b2-
a1 a2 ...
---------
| | | | | a4
---------
| | | | | b4 ...
---------
| | | | |
---------
| | | | |
---------
"""

ZONENAME = ''
DESCRIPTION = 'description'
examination = 'examine'
info = 'info'
puzzle = = 'puzzle'
solved = False
up = 'up', 'north'
down = 'down', 'south'
left = 'left', 'west'
right = 'right', 'east'

solved_placed = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle = = 'puzzle'
        solved: False,
        up: '',
        down: 'b1',
        left: '',
        right: 'a2',
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: '',
        down: 'b2',
        left: 'a1',
        right: 'a3',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: '',
        down: 'b2',
        left: 'a3',
        right: 'a4',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: '',
        down: 'b4',
        left: 'a3',
        right: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'a1',
        down: 'c1',
        left: 'b1',
        right: 'b3',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'You have entered the cave.',
        examination:'It is dark but thanks to the light coming from the outside you can see that this area is...safe.',
        solved: False,
        up: 'a2',
        down: 'c2',
        left: 'b1',
        right: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'a3',
        down: 'c3',
        left: 'b2',
        right: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'a4',
        down: 'c4',
        left: 'b3',
        right: '',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'b1',
        down: 'd1',
        left: 'c2',
        right: '',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'b2',
        down: 'd2',
        left: 'c1',
        right: 'c3',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'b3',
        down: 'd3',
        left: 'c2',
        right: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'b4',
        down: 'd4',
        left: 'c3',
        right: '',
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'c1',
        down: '',
        left: '',
        right: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'c2',
        down: '',
        left: 'd1',
        right: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'c3',
        down: '',
        left: 'd2',
        right: 'd4',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        examination:'examine',
        puzzle: 'puzzle',
        solved: False,
        up: 'c4',
        down: '',
        left: 'd3',
        right: '',
    }
}

#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower == ("play"):
        start_game() # placeholder until written
    elif option.lower == ("help"):
        help_menu()
    elif option.lower == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        option = input("> ")
        if option.lower == ("play"):
            start_game() # placeholder until written
        elif option.lower == ("help"):
            help_menu()
        elif option.lower == ("quit"):
            sys.exit()
        else:
            print("Please enter a valid command.")
def title_screen():
    os.system('clear')
    print('#################################')
    print('####Welcome  to the Text RPG!####')
    print('#################################')
    print('      Copyright 2020 LSC        ')
    print("""                                                                                                  
                                                                                                    
                                          `/oyhy+:`                                                 
                                        .-:`` `./osy+.                                              
                                     `--`          .so///::--`                                      
                                  .::-               :+``````.::---.`                               
                             `:/++:`                  +o`        `/+..----.                         
                           .++-`         -`       `  o/`+`         :/`  ``-/+/:`                    
                        -/o/`       .` //` `````..` o:  `+`         `-.      `-+o+-                 
                   `-:/ods`       ` ss/:---.``     +:    `+           `..`      `.:y+`              
               .-.-.``.s:      `.:+dMo            `/      `/             `.`       d+y.             
             -+-`    ./`    `::-+dMMM+            /.       .:              ``     /+ .s`            
            /:`     --     `s:smMMMMMN.           -.        `-                   `h   -o`           
           ..     `:.      +-yMMMMMMMMs           .          `-                  //    .+:`         
                 --       --yMMMMMMMMMN.                      `-                 y`      .o-`       
                :.      `-/mMMMMMMMMMMM+                       .-                y        :`-`      
              `+.      -:oNMMMMMMMMMMMMh                        :`               s        `         
             .+.     `+:sMMMMMMMMMMMMMMm                         +              .-                  
            :+`  `  -o:hMMMMMMMMMMMMMMMd                         :-             :                   
          `+/  `./.:o:dMMMMMMMMMMMMMMMMh                          s            ``                   
         -+.    ``.s`mMMMMMMMMMMMMMMMMMh                          o.                                
       `::         o NMMMMMMMMMMMMMMMMMy                          :+                                
      `.`  .////.  s dMMMMMMMMMMMMMMMMMs                          `y                                
          `/`  .+/:y/oMMMMMMMMMMMMMMMMM/ .+/::-`                   h                                
          `-.``` `-+m:++oyhmNMMMMMMMMMM.-o`   `.--.` `.:o//`       y                                
            .-::////:      `-+ydmNNNNMN /         `..-::` .o:      s-``                             
                                 ``.-:h-.`      `..``       +      //--/+-.                         
                                      -+:-://:-:::-.``      -       :  /.                           
                                        ::   `.```.://:-.```        .- `                            
                                         `                           -.                           
    """)  
    print('  Choose: Play, Help, or Quit    ')
    title_screen_selections()

def help_menu():
    print('#################################')
    print('####Welcome  to the Text RPG!####')
    print('#################################')
  
    print('Actions commands type: up, down, right, left, or look')
    print('"look" inspects objects')
    print('------Good luck!-------')
    print('----Share and Enjoy----')
    print('----By Leland Crawford----')
    title_screen_selections()






##### Game Interactivity ######
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    if myPlayer.solves == 5:
        print("Something in the world seems to have changed. Hmm...")
    print('\n' + "============================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        print("Choose from 'move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look'.")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'look']:
        playwer_examine(action.lower())

def move(myAction):
    ask = input("Where would you like to move to?\n")
    destination = input(ask)
    	if destination == 'up':
		move_dest = cube[player1.position][SIDE_UP] #if you are on ground, should say north
		move_player(move_dest)
	elif destination == 'left':
		move_dest = cube[player1.position][SIDE_LEFT]
		move_player(move_dest)
	elif destination == 'right':
		move_dest = cube[player1.position][SIDE_RIGHT]
		move_player(move_dest)
	elif destination == 'down':
		move_dest = cube[player1.position][SIDE_DOWN]
		move_player(move_dest)
	else:
		print("Invalid direction command, try using forward, back, left, or right.\n")
		move(myAction)

def move_player(move_dest):
    print("\nYou have moved to the " + move_dest + ".")
	player1.position = move_dest
	print_location()

def examine():
	if room_solved[player1.position] == False:
		print('\n' + (cube[player1.position][INFO]))
		print((cube[player1.position][PUZZLE]))
		puzzle_answer = input("> ")
		checkpuzzle(puzzle_answer)
	else:
		print("There is nothing new for you to see here.")

def checkpuzzle(puzzle_answer):
	if player1.position == 'ground':



#### Game functionality ####
def start_game():
    return "PLACEHOLDER"