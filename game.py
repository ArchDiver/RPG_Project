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
    print('-------Good luck!------')
    print('----Share and Enjoy----')
    title_screen_selections()

def start_game():







