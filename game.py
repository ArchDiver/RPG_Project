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
        player_examine(action.lower())

def move(myAction):
    ask = input("Where would you like to move to?\n")
    destination = input(ask)
    	if destination == 'up':
		move_dest = cube[myPlayer.position][SIDE_UP] #if you are on ground, should say north
		move_player(move_dest)
	elif destination == 'left':
		move_dest = cube[myPlayer.position][SIDE_LEFT]
		move_player(move_dest)
	elif destination == 'right':
		move_dest = cube[myPlayer.position][SIDE_RIGHT]
		move_player(move_dest)
	elif destination == 'down':
		move_dest = cube[myPlayer.position][SIDE_DOWN]
		move_player(move_dest)
	else:
		print("Invalid direction command, try using forward, back, left, or right.\n")
		move(myAction)

def move_player(move_dest):
    print("\nYou have moved to the " + move_dest + ".")
	myPlayer.position = move_dest
	print_location()

def examine():
	if room_solved[myPlayer.position] == False:
		print('\n' + (cube[myPlayer.position][INFO]))
		print((cube[myPlayer.position][PUZZLE]))
		puzzle_answer = input("> ")
		checkpuzzle(puzzle_answer)
	else:
		print("There is nothing new for you to see here.")

def checkpuzzle(puzzle_answer):
	if myPlayer.position == 'ground':
        if myPlayer.solves >= 5:
			endspeech = ("Without you having done anything, the key begins to rotate.\nIt begins to rain.\nAll of the sides of the box begin to crumble inwards.\nLight begins to shine through the cracks in the walls.\nA blinding flash of light hits you.\nYou have escaped!")
			for character in endspeech:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			print("\nCONGRATULATIONS!")
			sys.exit()
        else:
			print("Nothing seems to happen still...")
    elif myPlayer.position == 'south':
		if puzzle_answer == (myPlayer.astrological):
			room_solved[myPlayer.position] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print("\nPuzzles solved: " + str(myPlayer.solves))
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examine()
    else:
		if puzzle_answer == (cube[myPlayer.position][SOLVED]):
			room_solved[myPlayer.position] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print("\nPuzzles solved: " + str(myPlayer.solves))
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examine()

def main_game_loop():
	total_puzzles = 6
	while myPlayer.won is False:
		#print_location()
		prompt()



#### Game functionality ####
def start_game():
    return "PLACEHOLDER"

################
# Execute Game #
################
def setup_game():
	#Clears the terminal for the game to start.
	os.system('clear')

	#QUESTION NAME: Obtains the player's name.
	question1 = "Hello there, what is your name?\n"
	for character in question1:
		#This will occur throughout the intro code.  It allows the string to be typed gradually - like a typerwriter effect.
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

    #QUESTION FEELING: Obtains the player's feeling.
	question2 = "My dear friend " + myPlayer.name + ", how are you feeling?\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	feeling = input("> ")
	myPlayer.feeling = feeling.lower()

    #Creates the adjective vocabulary for the player's feeling.
	good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving']
	hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult']
	bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']

    #Identifies what type of feeling the player is having and gives a related-sounding string.
	if player1.feeling in good_adj:
		feeling_string = "I am glad you feel"
	elif player1.feeling in hmm_adj:
		feeling_string = "that is interesting you feel"
	elif player1.feeling in bad_adj:
		feeling_string = "I am sorry to hear you feel"
	else:
		feeling_string = "I do not know what it is like to feel"
    
    #Combines all the above parts.
	question3 = "Well then, " + player1.name + ", " + feeling_string + " " + player1.feeling + ".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
    #QUESTION SIGN: Obtains the player's astrological sign for a later puzzle.
	question4 = "Now tell me, what is your astrological sign?\n"

	for character in question4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

    #Prints the astrological sign guide for the player.  Also converts text to be case-insensitive, as with most inputs.
    print("#####################################################")
	print("# Please print the proper name to indicate your sign.")
    print("# ♈ Aries (The Ram)")
	print("# ♉ Taurus (The Bull)")
    print("# ♊ Gemini (The Twins)")
	print("# ♋ Cancer (The Crab)")
    print("# ♌ Leo (The Lion)")
	print("# ♍ Virgo (The Virgin)")
    print("# ♎ Libra (The Scales)")
	print("# ♏ Scorpio (The Scorpion)")
    print("# ♐ Sagittarius (Centaur)")
	print("# ♑ Capricorn (The Goat)")
    print("# ♒ Aquarius (The Water Bearer)")
	print("# ♓ Pisces (The Fish)")
    print("#####################################################")
	astrological = input("> ")
	acceptable_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
	#Forces the player to write an acceptable sign, as this is essential to solving a puzzle later.  Also stores it in class.
    
    while astrological.lower() not in acceptable_signs:
		print("That is not an acceptable sign, please try again.")
		astrological = input("> ")
	player1.astrological = astrological.lower()

    #Leads the player into the cube puzzle now!
	speech1 = "Ah, " + player1.astrological + ", how interesting.  Well then.\n"
	speech2 = "It seems this is where we must part, " + player1.name + ".\n"
    speech3 = "How unfortunate.\n"  
	speech4 = "Oh, you don't know where you are?  Well...\n"
