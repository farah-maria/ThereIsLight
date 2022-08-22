""" Modules allow random selection, colour, time delay and scores record """
import random
import colorama
import gspread
import time
import sys
import pprint
from colorama import Fore
from time import sleep
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('HJ_Scoresheet')

scores_data = SHEET.worksheet('scores_data')
data = scores_data.get_all_values()

##############################################################
# (pre-story set up of code, & support for some functions

global game_speed
game_speed = 2


class Enemy:
    """ Enemy who reduces player's power through the game """

    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.calories_to_burn = calories_to_burn

#  Methods not being used but might come in handy in the future
  
    def get_enemy_name(self):
        return self.name

    def get_enemy_fighting_spirit(self):
        return self.fighting_spirit

    def get_enemy_calories_to_burn(self):
        return self.calories_to_burn

    def set_enemy_name(self, name):
        self.name = name

    def set_fighting_spirit(self, fighting_spirit):
        self.fighting_spirit = fighting_spirit

    def set_calories_to_burn(self, calories_to_burn):
        self.calories_to_burn = calories_to_burn

# Heroine/ main character class


class Heroine:
    """ Character for user to be through the game """

    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def set_heroine_name(self, name):
        self.name = name

    def set_fighting_spirit(self, fighting_spirit):
        self.fighting_spirit = fighting_spirit

    def set_self_esteem(self, self_esteem):
        self.self_esteem = self_esteem

    def set_calories_to_burn(self, calories_to_burn):
        self.calories_to_burn = calories_to_burn

    def get_heroine_name(self):
        return self.name

    def get_fighting_spirit(self, fighting_spirit):
        return self.fighting_spirit

    def get_self_esteem(self, self_esteem):
        return self.fighting_spirit

    def get_calories_to_burn(self, calories_to_burn):
        return self.fighting_spirit

    def print_stats(self):
        slow_read(f"\nYou have selected {self.name}.\n")
        print("")
        sleep(game_speed / 2)
        print(F"{Fore.BLUE}These are your starting stats: \n")
        print("")
        sleep(game_speed / 2)
        print(f"\nfighting spirit - {self.fighting_spirit}")
        sleep(game_speed / 2)
        print(f"\nself esteem - {self.self_esteem}")
        sleep(game_speed / 2)
        print(f"\ncalories to burn - {self.calories_to_burn}\n \n")
        print("")
        time.sleep(game_speed)
        """Heroine now taken to first part of the story"""

# re-writing mess of code from below #


def intro_text():
    # PART ONE: LOGO. INTRO to game. Goes to decision function: 
    # play or not
    print("""
    ╔╦╗╦ ╦╔═╗╦═╗╔═╗  ╦╔═╗  ╦  ╦╔═╗╦ ╦╔╦╗
     ║ ╠═╣║╣ ╠╦╝║╣   ║╚═╗  ║  ║║ ╦╠═╣ ║ 
     ╩ ╩ ╩╚═╝╩╚═╚═╝  ╩╚═╝  ╩═╝╩╚═╝╩ ╩ ╩                                                       
    """)
    """ CREDS for lettering in title: 
    Mini by Glenn Chappell 4/93
    Includes ISO Latin-1
    figlet release 2.1 -- 12 Aug 1994
    Permission is hereby given to modify this font, as long as the
    modifier's name is placed on a comment line.
    Modified by Paul Burton <solution@earthlink.net> 12/96 to include 
    new parameter
    supported by FIGlet and FIGWin.  
    May also be slightly modified for better use
    of new full-width/kern/smush alternatives, 
    but default output is NOT changed.
    from https://patorjk.com/"""

    time.sleep(game_speed)
    intro = """This is a game where winning is hard.
The situation is as follows... 
You wake up trapped in a patriarchial nightmare.
The odds are staked against you.
There will be enemies! And enemies are a drag!
But you will always have options: either y/n...
...or a number you need to select to choose a pathway.
(Remember to press 'enter' after your selection.)
Also, you can pick up points, which increases your score...
... by eating cake and winning fights :) """
    for line in intro.splitlines():
        print(line)
        sleep(game_speed)

    slow_read(F"\n{Fore.GREEN}Would you like to play?")


def slow_read(string):
    """ allows text to appear letter by letter in console """
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)


######################################################
class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def printStats_and_start(self): 
        # STARTS THE GAME AFTER PLAYER CHOOSES 'Y' in PART 3, line 408)
        """ Calls stats on player's choice of Heroine,""" 
        """ & starts the story (with a bus fight!)"""
        global heroine
        slow_read(f"\nYou have selected {self.name}.\n") 
        print("")
        sleep(1)
        print(F"{Fore.BLUE}These are your starting stats: \n")
        print("")
        sleep(1)
        print(f"\nfighting spirit - {self.fighting_spirit}")
        sleep(1)
        print(f"\nself esteem - {self.self_esteem}")
        sleep(1)
        print(f"\ncalories to burn - {self.calories_to_burn}\n \n")
        print("")
        time.sleep(2)  
        Bus_Fight()
        """Heroine is taken to first part of the story"""

# heroine stats:


Demeter = Heroine("Demeter", 80, 80, 2800)

Persephone = Heroine("Persephone", 90, 50, 1500)

Athena = Heroine("Athena", 100, 90, 2000)

Lilith = Heroine("Lilith", 75, 40, 3500)

Roe = Heroine("Roe", 100, 95, 3000)


# opponents who appear in battles:

class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn

# enemy stats


Kavanaugh = Enemy("Kavanaugh", 40, 2500)

Schlafly = Enemy("Schlafly", 60, 3000)

Trump = Enemy("Trump", 100, 3500)

# # # 


def slow_read(string):
    """ allows text to appear letter by letter in console """
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)


def score_end():
    """calculates and returns score at the end"""
    global heroine
    total_points = heroine.calories_to_burn + heroine.fighting_spirit 
    + heroine.self_esteem
    float_points = total_points/30
    total_score = int(float_points)
    slow_read(F"\n{Fore.WHITE}Thank you for playing...\n")
    print(f"Your end of game score is {total_score}\n")
    print("""
            
╔═╗┌─┐┌┬┐┌─┐  ┌─┐┬  ┬┌─┐┬─┐
║ ╦├─┤│││├┤   │ │└┐┌┘├┤ ├┬┘
╚═╝┴ ┴┴ ┴└─┘  └─┘ └┘ └─┘┴└─
                                           
            \n""")
# https://web.archive.org/web/20120819044459/http://www.roysac.com/thedrawfonts-tdf.asp
# FIGFont created with: http://patorjk.com/figfont-editor      
    slow_read(F"{Fore.GREEN}Want to play again?\n")
    play_or_not()  
  
  
###################################################################
# STORY: start at the bottom of the page for part 1, & move up.
###################################################################

# PART EIGHT of EIGHT: FIGHT KAVANAUGH AT WORK. THE OFFICE IS UNSAFE!. THE END.


def Office():
    """ Last fight """
    global heroine
    time.sleep(2)
    print("")
    slow_read(F"{Fore.MAGENTA}\nCHAPTER FOUR: The Last Battle.\n")
    slow_read(F"\n{Fore.WHITE}You walk to work carefully... \n")
    slow_read("go through the revolving doors and into the office.\n")
    slow_read("Your colleagues look nervous as they look up.\n")
    time.sleep(1)
    print(f"Someone whispers, '{heroine.name}...'\n")
    time.sleep(2)
    print("'We've got a new boss!'\n")
    time.sleep(2)
    slow_read(F"{Fore.BLUE}'But what happened to our old one?', you ask.\n")
    time.sleep(1)
    slow_read(
        F"{Fore.WHITE}'She got voted out in a horrible takeover!'\n")
    slow_read("'It all happened last night....\n'")
    time.sleep(1)
    slow_read("Everyone looks down as a man in a suit approaches.\n")
    slow_read("He looks polite, and smiles kindly.\n")
    time.sleep(1)
    print(f"\n'Hi, {heroine.name}, my name is Kavanaugh...'")
    time.sleep(2)
    print("\n'I'm so sorry, but you don't work here anymore.'")
    slow_read(F"\n{Fore.BLUE}'But why?!' You ask.")
    slow_read("\n'I went through hell to get here!!!'")
    time.sleep(2)
    print(F"\n{Fore.WHITE}He smiles nicely.")
    print("\n'Because my people get what they want,' he says.")
    slow_read("\n.....................\n")
    slow_read(F"{Fore.GREEN}Suddenly, your workmate Conor stands up\n")
    slow_read("...and throws a stapler at Kavanaugh's head.\n")
    slow_read(
        "Others join in. Your desk-neighbour Quinn throws a book at him...\n")
    print("\n(- it's a copy of Tom Paine's 'The Rights of Man', of course)\n")
    time.sleep(2)
    slow_read(".....................")
    print(F"\n{Fore.WHITE}And this was how the revolution started.\n")
    time.sleep(2)
    print(F"{Fore.LIGHTBLUE_EX}In the words of Charles Bukowski:\n")
    time.sleep(2)
    slow_read(F"\n{Fore.WHITE}'There is a light somewhere...\n")
    slow_read("it may not be much light but\n")
    slow_read("it beats the darkness.'\n")
    score_end()

  
# PART SEVEN: IF PLAYER BEAT TRUMP, TREATS!! AND TIME TO GO TO WORK.


def treats():
    treats_list = ["coffee", "smoothie", "valium"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    slow_read(F"\n{Fore.MAGENTA}Nice! :)\n")
    Office()
    """ Time to go to work!"""


# PART SIX - FIGHT TRUMP, OR NO FREE MEDICAL TREATMENT!


def Fight_Trump():
    global heroine
    """a fight for medical care"""
    time.sleep(1)
    slow_read(F"\n{Fore.MAGENTA}CHAPTER THREE:\n")
    time.sleep(2)
    print(F"\n{Fore.WHITE}You're feeling pretty damn good about yourself...\n")
    
    accident = """and you cross the road to a tall, glass building.
These are the offices where you work.
You push at the revolving door...
And bang your face. Someone pushed it in the opposite direction...
Blood streams from your nose. It feels broken.
Holding your nose, you run to the hospital.
It's only a block away... and work would make you go anyway.
But at the main entrance to the emergency department...
stands a squarish, tanned man shaking his head."""
    
    for line in accident.splitlines():
        print(line)
        sleep(2)

    slow_read(f"\n'No free medical care for you, {heroine.name}.\n")
    slow_read(
        "\n'I've called the cops on you. Your insurance ran out years ago.'")
    time.sleep(2)
    print("\nThree black vans pull up by the hospital gate.")
    time.sleep(2)
    print("\nThe men who get out...")
    time.sleep(2)
    print("\nThey don't look like police, more like private security.")
    time.sleep(2)
    slow_read(F"\n{Fore.BLUE}You have three options...\n ")
    time.sleep(1)
    choice = input(
        F"{Fore.GREEN}1. Use injustice_zapper \n2. Run! \n3. Call cops.")
    if choice == "1":
        time.sleep(2)
        slow_read(F"\n{Fore.WHITE}You point the zapper at Trump.\n")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 3:
            time.sleep(2)
            print("But his men get to you before you zapp...\n ")
            time.sleep(2)
            print("They bundle you into the back of a van.\n")
            time.sleep(2)
            print("Oh dear... That's the end of you.\n")
            time.sleep(2)
            score_end()

        elif defeat_chance < 4:
            Trump.fighting_spirit -= 90
            time.sleep(2) 
            slow_read(
                F"{Fore.WHITE}You stun him, then turn and zapp the others.")
            time.sleep(1)
            slow_read(
                "Trump's fighting spirit has been knocked by 90 points...")
            time.sleep(2)
            slow_read(f"and is now down to just {Trump.fighting_spirit}.")
            time.sleep(2)
            print("It'll be a while before he poses a problem again...")
            print("Well done :)")
            time.sleep(2)
            slow_read("You get the medical treatment you need...")
            time.sleep(1)
            print("and are able to return to work.")
            time.sleep(2)
            slow_read(F"{Fore.GREEN}You decide to flip a coin...")
            time.sleep(2)
            print("If it's heads, you grab a coffee.")
            time.sleep(2)
            slow_read("If it's tails, you get a smoothie.")
            time.sleep(2)
            slow_read("And if the coin falls out of your hand...")
            time.sleep(2)
            slow_read("you can have some valium. (You probably need it).")
            time.sleep(2)
            print(F"{Fore.BLUE}You flip the coin and you get... \n")
            treats()
            """ treats for if you beat Trump """
 
    elif choice == 2:
        print("You run, and slip on your own blood.")
        time.sleep(2)
        print("A black van drives straight into you.")
        time.sleep(2)
        slow_read(F"{Fore.RED}Sorry. You died.")
        time.sleep(2)
        score_end()
      
    else:
        police = """The police don't arrive in time.
But some medical staff run out of the building.
A nurse gets Trump in the neck with a needle...
The security men scatter.
You get the care you need, and everyone is smiling.
You decide to flip a coin...
If it's heads, you grab a coffee.
If it's tails, you get a smoothie.
And if the coin falls out of your hand...
you can have some valium from the nurse. 
(You probably need it).
You flip the coin and you get..."""
        for line in police.splitlines():
            print(line)
            sleep(2) 
        treats()
        """Treats for if you beat Trump"""


# PART FIVE - IF PLAYER BEAT SCHLAFLY, GO TO CAFE & GET READY TO FIGHT TRUMP!


def perks_select():
    print("")
    print("")
    slow_read(F"\n{Fore.MAGENTA}CHAPTER TWO:\n \n")
    """ heroine gets a perk that raises score after defeating Schlafly """
    global heroine
    print("")
    print("")
    print(F"\n{Fore.WHITE}The bus stops near the office and you get off.\n")
    prize = """You decide to flip a coin...
If it's heads, you'll grab a coffee from the cafe opposite.
If it's tails, you get coffee AND cake."""

    for line in prize.splitlines():
        print(line)
        sleep(2) 
    
    slow_read("You flip the coin and you get...\n ")

    perk_chance = random.randint(0, 10)
    if perk_chance > 5:
        slow_read(F"{Fore.GREEN}\nTails!\n")
        time.sleep(2)
        slow_read(
            F"{Fore.BLUE}You get a large coffee AND a big slice of cake.\n")
        heroine.fighting_spirit += 100
        heroine.calories_to_burn += 300
        heroine.self_esteem += 200
        time.sleep(1)
        slow_read("Your fighting spirit increases by 100pts...\n")
        slow_read(
            f"to {heroine.fighting_spirit}.\n")
        slow_read("Your calories to use for fighting increase by 200,\n") 
        slow_read(f"to {heroine.calories_to_burn}.\n")
        slow_read("& your self-esteem has gone up by 200pts\n")
        slow_read(f"to: {heroine.self_esteem}.\n")
        sleep(2)
        Fight_Trump() 
        """ Onto the next scene to fight Trump! """
    elif perk_chance < 6:
        time.sleep(1)
        slow_read(F"\n{Fore.GREEN}Heads!\n")
        heroine.fighting_spirit += 50
        time.sleep(2)
        slow_read(
            F"\n{Fore.BLUE}You grab coffee.") 
        slow_read("Caffiene ups your fighting spirit...\n")
        time.sleep(1)
        slow_read(f"\nby 50 points, to {heroine.fighting_spirit} :)\n \n")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
                

# PART FOUR: A BUS FIGHT WITH SCHLAFLY! 1st PART OF REAL STORY.


def Bus_Fight():
    global heroine
    """ First battle of heroine Vs opponent """
    print("")
    slow_read(F"{Fore.MAGENTA}CHAPTER ONE:\n \n")
    sleep(2)
    print(F"{Fore.WHITE}You get on a bus. It is 8am.")
    sleep(2)
    bus_description = """You have 20mins to read before work.
Just as you get your book out of your bag...
a dangerous enemy sits next to you...
blocking your way out into the aisle.
'Hello', she says. 'My name's Schlafly...'
'I don't think you should be going to work,' she continues..."""

    for line in bus_description.splitlines():
        print(line)
        time.sleep(2)
    
    slow_read("she draws a tiny gun from the pocket of her cardigan.\n")

    print(F"\n{Fore.GREEN}You have two choices: \n")
    time.sleep(2)
    choice = input(
        F"{Fore.BLUE}1. Use injustice_zapper \n2. Push her and run! \n")
    if choice == "1":
        slow_read(
            F"{Fore.WHITE}\n You point the zapper at Schlafly.\n")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 7:
            time.sleep(2)
            print("")
            slow_read(
                F"\n{Fore.WHITE}Schlafly knocks the zapper outta your hands\n")
            time.sleep(2)
            slow_read("\nand shoots you. You die.")
            time.sleep(2)
            slow_read(F"{Fore.RED}\n\nYou'll never get to work, now. Sorry!\n")
            time.sleep(2)
            print("")
            score_end()

        elif defeat_chance < 8:
            Schlafly.fighting_spirit -= 40 
            slow_read(F"\n{Fore. WHITE}You manage to stun her. She falls.")
            time.sleep(1)
            slow_read("\nHer fighting spirit has been knocked by 40 points...")
            slow_read(
                f"\nand is now down to just {Schlafly.fighting_spirit}.\n")
            slow_read(
                "She'll have less energy to pester other people, now :)")
            time.sleep(2)
            print("\nWell done!")
            time.sleep(2)
            perks_select()
                        
    else:
        slow_read(F"\n{Fore. WHITE}Schlafly gets right back up...")
        slow_read("\n... and shoots you in the back as you try to run.")
        time.sleep(1.5)
        slow_read(F"\n{Fore.RED}Sorry. She won. You died.\n \n")
        time.sleep(1.5)
        score_end()


# PART THREE: If 'Y', CHOOSE A HEROINE & move to a bus fight!!


def heroine_select():
    global heroine
    """ Allows player to choose which heroine they play as.
    Go to line 32 if need to read the printStats function """
    selection = input(
        "\n1. Demeter \n2. Persephone  \n3. Athena \n4. Lilith \n5. Roe \n")
   
    if selection == "1":
        heroine = Demeter
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "2":
        heroine = Persephone
        heroine.printStats_and_start()
    elif selection == "3":
        heroine = Athena
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "4":
        heroine = Lilith
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "5":
        heroine = Roe
        heroine.printStats_and_start()
    else:
        slow_read(F"{Fore.RED}Error!")
        slow_read("Only press 1, 2, 3, 4 or 5 and press enter")
        heroine_select()  # This function is defined on line 37.


# PART TWO - WANNA PLAY OR NOT?


def play_or_not():
    """ player chooses to continue to game or quit """
    answer = input(F"\n\n{Fore.BLUE}Answer 'y' or 'n': ")
    if answer.lower().strip() == "y":
        slow_read(F"\n{Fore.WHITE}Great! ") 
        slow_read("Choose which character you want to be...")
        print("")
        heroine_select()
    elif answer.lower().strip() == "n":
        print(F"{Fore.WHITE}I don't blame you. Bye!")
        exit()
    else:
        slow_read(F"\n{Fore.RED}Incorrect input!")
        slow_read("\n\nTry again. Just one letter and press enter.")
        play_or_not()


# PART ONE: LOGO. INTRO to game. Takes goes to decision function: play or not

print("""
╔╦╗╦ ╦╔═╗╦═╗╔═╗  ╦╔═╗  ╦  ╦╔═╗╦ ╦╔╦╗
 ║ ╠═╣║╣ ╠╦╝║╣   ║╚═╗  ║  ║║ ╦╠═╣ ║ 
 ╩ ╩ ╩╚═╝╩╚═╚═╝  ╩╚═╝  ╩═╝╩╚═╝╩ ╩ ╩                                                       
""")

""" CREDS for lettering in title: 
Mini by Glenn Chappell 4/93
Includes ISO Latin-1
figlet release 2.1 -- 12 Aug 1994
Permission is hereby given to modify this font, as long as the
modifier's name is placed on a comment line.

Modified by Paul Burton <solution@earthlink.net> 12/96 to include 
new parameter
supported by FIGlet and FIGWin.  May also be slightly modified for better use
of new full-width/kern/smush alternatives, but default output is NOT changed.

from https://patorjk.com/"""

time.sleep(2)
intro = """This is a game where winning is hard.
The situation is as follows... 
You wake up trapped in a patriarchial nightmare.
The odds are staked against you.
There will be enemies! And enemies are a drag!
But you will always have options: either y/n...
...or a number you need to select to choose a pathway.
(Remember to press 'enter' after your selection.)
Also, you can pick up points, which increases your score...
... by eating cake and winning fights :) """

for line in intro.splitlines():
    print(line)
    sleep(2)

slow_read(F"\n{Fore.GREEN}Would you like to play?")

play_or_not()       
