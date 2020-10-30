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
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'

myPlayer = Player()

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
    print('  Choose: Play, Help, or Quit    ')
    print('      Copyright 2020 LSC        ')
    title_screen_selections()

def help_menu():
    print('#################################')
    print('####Welcome  to the Text RPG!####')
    print('#################################')
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
    print('Actions commands type: up, down, right, left, or look')
    print('"look" inspects objects')
    print('------Good luck!-------')
    print('----Share and Enjoy----')
    title_screen_selections()


#### Game functionality ####
def start_game():
    return "PLACEHOLDER"

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

zone_name = ''
description = 'description'
examination = 'examine'
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
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: 'b1',
        left: '',
        right: 'a2',
    },
    'a2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: 'b2',
        left: 'a1',
        right: 'a3',
    },
    'a3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: 'b2',
        left: 'a3',
        right: 'a4',
    },
    'a4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: 'b4',
        left: 'a3',
        right: '',
    },
    'b1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'a1',
        down: 'c1',
        left: 'b1',
        right: 'b3',
    },
    'b2': {
        zone_name: "",
        description: 'You have entered the cave.',
        examination:'It is dark but thanks to the light coming from the outside you can see that this area is...safe.',
        solved: False,
        up: 'a2',
        down: 'c2',
        left: 'b1',
        right: 'b3',
    },
    'b3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'a3',
        down: 'c3',
        left: 'b2',
        right: 'b4',
    },
    'b4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'a4',
        down: 'c4',
        left: 'b3',
        right: '',
    },
    'c1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    },
    'c2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'b2',
        down: 'd2',
        left: 'c1',
        right: 'c3',
    },
    'c3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    },
    'c4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    },
    'd1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    },
    'd2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'c2',
        down: '',
        left: 'd1',
        right: 'd3',
    },
    'd3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    },
    'd4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: '',
        down: '',
        left: '',
        right: '',
    }
}

