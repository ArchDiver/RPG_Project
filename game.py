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
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'a2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'a3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'a4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'b1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'b2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'b3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'b4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'c1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'c2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'c3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'c4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'd1': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'd2': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'd3': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    },
    'd4': {
        zone_name: "",
        description: 'description',
        examination:'examine',
        solved: False,
        up: 'ROOM PLACEHOLDER',
        down: 'ROOM PLACEHOLDER',
        left: 'ROOM PLACEHOLDER',
        right: 'ROOM PLACEHOLDER',
    }
}

