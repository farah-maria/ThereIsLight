""" Modules allow random selection, colour, time delay and scores record """
import random
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
SHEET = GSPREAD_CLIENT.open('scoresheet')

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
# calls stats of heroine after player chooses which to be

    def print_stats(self):
        slow_read(f"\nYou have selected {self.name}.\n")
        print("")
        sleep(game_speed / 2)
        print(F"{Fore.CYAN}These are your starting stats: \n")
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
    intro = F"""{Fore.WHITE}This is a game where winning is hard.
The situation is as follows... 
You wake up trapped in a patriarchial nightmare.
The odds are staked against you.
There will be enemies! And enemies are a drag!
But you will always have options: either y/n...
...or a number you need to select to choose a pathway.
(Remember to press 'enter' after your selection.)
You can pick up points, which increases your score...
... by eating cake and winning fights :) """
    for line in intro.splitlines():
        print(line)
        sleep(game_speed)


def slow_read(string):
    """ allows text to appear letter by letter in console """
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.15)


def play_or_not():
    """ player chooses to continue to game or quit """
    slow_read(F"\n{Fore.GREEN}Would you like to play?")
    answer = input(F"\n\n{Fore.CYAN}Answer 'y' or 'n':\n")
    if answer.lower().strip() == "y":
        slow_read(F"\n{Fore.WHITE}Great!\n")
        slow_read("Choose which character you want to be...\n")
        print("")
        return True
    elif answer.lower().strip() == "n":
        print(F"\n{Fore.WHITE}I don't blame you. Bye!\n")
        exit()
    else:
        slow_read(F"\n{Fore.RED}Incorrect input!\n \n")
        slow_read("Try again. Just one letter and press enter.\n")
        play_or_not()


def play_again(): 
    slow_read(F"\n{Fore.WHITE}Want to play again?\n")
    answer = input(F"\n\n{Fore.CYAN}Answer 'y' or 'n':\n")
    if answer.lower().strip() == "y":
        intro_text()
    elif answer.lower().strip() == "n":
        print(F"\n{Fore.WHITE}I don't blame you. Bye!\n")
        exit()
    else:
        slow_read(F"\n{Fore.RED}Incorrect input!\n \n")
        slow_read("Try again. Just one letter and press enter.\n")
        play_again()


def heroine_select():
    """
    Allows player to choose which heroine they play as. 
    Selection takes them to start of the main story.
    """
    selection = input(
        "\n1. Demeter \n2. Persephone \n3. Athena \n4. Lilith \n5. Roe \
            \n")

    match selection:
        case "1":
            return Heroine("Demeter", 80, 80, 2800)
        case "2":
            return Heroine("Persephone", 90, 50, 1500)
        case "3":
            return Heroine("Athena", 100, 90, 2000)
        case "4":
            return Heroine("Lilith", 75, 40, 3500)
        case "5":
            return Heroine("Roe", 100, 95, 3000)
        case _:
            slow_read(F"{Fore.RED}Error!")
            slow_read("Only press 1, 2, 3, 4 or 5 and press enter")
            heroine_select() 


def score_end(heroine):
    """calculates and returns score at the end"""
    #player_name = input("What is your first name/ nickname?:\n").capitalize
    #return player_name
    total_points = heroine.calories_to_burn + heroine.fighting_spirit
    + heroine.self_esteem
    float_points = total_points / 40
    total_score = int(float_points)
    slow_read(F"\n{Fore.WHITE}Thank you for playing.\n")
    slow_read(f"Your end of game score is {total_score}\n")
    time.sleep(2)
    print("(Yes, you do get points just for playing.)")
    print("""\n
╔═╗┌─┐┌┬┐┌─┐  ┌─┐┬  ┬┌─┐┬─┐
║ ╦├─┤│││├┤   │ │└┐┌┘├┤ ├┬┘
╚═╝┴ ┴┴ ┴└─┘  └─┘ └┘ └─┘┴└─
            \n""")
# https://web.archive.org/web/20120819044459/
# http://www.roysac.com/thedrawfonts-tdf.asp
# FIGFont created with: http://patorjk.com/figfont-editor
    play_again()


###################################################################
# STORY
###################################################################


def Bus_Fight(enemy):
    """ First battle of heroine Vs opponent """
    print("")
    slow_read(F"{Fore.YELLOW}CHAPTER ONE:\n \n")
    sleep(game_speed)
    print(F"{Fore.WHITE}You get on a bus. It is 8am.\n")
    sleep(game_speed)
    bus_description = F"""You have 20mins to read before work.
Just as you get your book out of your bag...
a dangerous enemy sits next to you...
blocking your way out into the aisle.
'Hello', she says. 'My name's {enemy.get_enemy_name()} '
'I don't think you should be going to work,' she continues."""

    for line in bus_description.splitlines():
        print(line)
        time.sleep(game_speed)

    slow_read("\nShe draws a tiny gun from the pocket of her cardigan.\n")

    print(F"\n{Fore.GREEN}You have two choices: \n")

    you_are_still_alive = True
    choice = input(
        F"{Fore.CYAN}1. Use injustice_zapper \n2. Push her and run!\n")
    if choice == "1":
        slow_read(
            F"{Fore.WHITE}\nYou point the zapper at \
 {enemy.get_enemy_name()}.\n")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 7:
            time.sleep(game_speed)
            print("")
            slow_read(
                F"\n{Fore.WHITE}{enemy.get_enemy_name()} \
knocks the zapper outta your hands\n")
            time.sleep(game_speed)
            slow_read("\nand shoots you. You die.\n")
            time.sleep(game_speed)
            slow_read(F"{Fore.RED}\n\nYou'll never get to work, now. Sorry!\n")
            time.sleep(game_speed)
            print("")
            score_end(heroine)
            you_are_still_alive = False
            return you_are_still_alive
        elif defeat_chance < 8:
            enemy.fighting_spirit -= 40
            slow_read(F"\n{Fore.WHITE}You manage to stun her. She falls.\n")
            time.sleep(game_speed / 2)
            slow_read("\nHer fighting spirit is down 40 points...\n")
            slow_read(
                f"\nand is now down to just {enemy.fighting_spirit}.\n")
            slow_read(
                "She'll have less energy to pester other people, now :)\n")
            time.sleep(game_speed)
            print("\nWell done!\n")
            time.sleep(game_speed)
            you_are_still_alive = True
            return you_are_still_alive            
    else:
        slow_read(
            F"\n{Fore.WHITE}{enemy.get_enemy_name()} gets right back up...")
        slow_read("\n... and shoots you in the back as you try to run.")
        time.sleep(1.5)
        slow_read(F"\n{Fore.RED}Sorry. She won. You died.\n \n")
        time.sleep(2)
        score_end(heroine)
        time.sleep(1.5)
        you_are_still_alive = False
        return you_are_still_alive


def perks_select(heroine):
    """class attributes and method accessed by passing 
    heroine to this function """
    print("")
    print("")
    slow_read(F"\n{Fore.YELLOW}CHAPTER TWO:\n \n")
    """ heroine gets a perk that raises score after defeating Schlafly """
    print("")
    print("")
    print(F"\n{Fore.WHITE}The bus stops near the office and you get off.\n")
    prize = """You decide to flip a coin...
If it's heads, you'll grab a coffee from the cafe opposite.
If it's tails, you get coffee AND cake."""
  
    for line in prize.splitlines():
        print(line)
        sleep(game_speed)
  
    slow_read("\nYou flip the coin and you get...\n ")
  
    perk_chance = random.randint(0, 10)
    if perk_chance > 5:
        slow_read(F"\n{Fore.GREEN}Tails!\n")
        time.sleep(game_speed)
        slow_read(
            F"{Fore.CYAN}You get a large coffee AND a big slice of cake.\n")
        # variables created so can be used in text of story:
        fighting_spirit_bonus = 100
        calories_to_burn_bonus = 300
        self_esteem_bonus = 200
        heroine.fighting_spirit += fighting_spirit_bonus
        heroine.calories_to_burn += calories_to_burn_bonus
        heroine.self_esteem += self_esteem_bonus
        time.sleep(game_speed / 2)
        slow_read(
            f"\nYour fighting spirit increases by\
{fighting_spirit_bonus}pts...\n")
        slow_read(
            f"\n up to {heroine.fighting_spirit}.\n")
        slow_read(f"Your calories to use for fighting\
increase by {calories_to_burn_bonus},\n")
        slow_read(f"up to {heroine.calories_to_burn}.\n")
        slow_read(
            f"& your self-esteem has gone up by {self_esteem_bonus}pts\n")
        slow_read(f"up to: {heroine.self_esteem}.\n")
        sleep(game_speed)
    elif perk_chance < 6:
        time.sleep(game_speed / 2)
        slow_read(F"\n{Fore.GREEN}Heads!\n")
        fight_spirit_bonus = 50
        heroine.fighting_spirit += fight_spirit_bonus
        time.sleep(game_speed)
        slow_read(
            F"\n{Fore.CYAN}You grab coffee.")
        slow_read("\nCaffiene ups your fighting spirit...\n")
        time.sleep(game_speed / 2)
        slow_read(
            f"\nby {fight_spirit_bonus} points, to\
                {heroine.fighting_spirit}:)\n\n")


def Fight_Trump(heroine, enemy):
    """a fight for medical care"""
    time.sleep(game_speed / 2)
    slow_read(F"\n{Fore.YELLOW}CHAPTER THREE:\n")
    time.sleep(game_speed)
    print(
        F"\n{Fore.WHITE}You're feeling pretty damn good about yourself...\n")

    accident = """and you cross the road to a tall, glass building.
These are the offices where you work.
You push at the revolving door...
and bang your face. Someone pushed it in the opposite direction...
Blood streams from your nose. It feels broken.
Holding your nose, you run to the hospital.
It's only a block away... and work would make you go anyway.
But at the main entrance to the emergency department...
stands a squarish, tanned man shaking his head."""

    for line in accident.splitlines():
        print(line)
        sleep(game_speed)

    slow_read(f"\n'No free medical care for you, {heroine.name}.\n")
    slow_read(
        "\n'I've called the cops on you. Your insurance ran out years ago.'")
    time.sleep(game_speed)
    print("\nThree black vans pull up by the hospital gate.")
    time.sleep(game_speed)
    print("\nThe men who get out...")
    time.sleep(game_speed)
    print("\nThey don't look like police, more like private security.")
    time.sleep(game_speed)
    slow_read(F"\n{Fore.CYAN}You have three options...\n ")
    time.sleep(game_speed / 2)

    still_alive = True
    choice = input(
        F"\n{Fore.GREEN}1. Use injustice_zapper \n2. Run!\
3. Call real cops.\n")
    if choice == "1":
        time.sleep(game_speed)
        slow_read(F"\n{Fore.WHITE}You point the zapper at Trump.\n")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 3:
            time.sleep(game_speed)
            print("But his men get to you before you zapp...\n ")
            time.sleep(game_speed)
            print("They bundle you into the back of a van.\n")
            time.sleep(game_speed)
            print("Oh dear... That's the end of you.\n")
            time.sleep(game_speed)
            score_end(heroine)
            still_alive = False
            return still_alive
        elif defeat_chance < 4:
            enemy_fighting_spirit_damage = 90
            enemy.fighting_spirit -= enemy_fighting_spirit_damage
            time.sleep(game_speed)
            slow_read(
                F"\n{Fore.WHITE}You stun him, & turn and zapp the others.\n")
            time.sleep(game_speed / 2)
            slow_read(
                f"\nTrump's fighting spirit has been knocked by\
 {enemy_fighting_spirit_damage} points...\n")
            time.sleep(game_speed)
            slow_read(f"and is now down to just {enemy.fighting_spirit}\n")
            time.sleep(game_speed)
            print("It'll be a while before he poses a problem again...\n")
            print("Well done :)\n")
            time.sleep(game_speed)
            slow_read("\nYou get the medical treatment you need...\n")
            time.sleep(game_speed / 2)
            print("and are able to return to work.\n")
            time.sleep(game_speed)
            slow_read(F"\n\n{Fore.GREEN}You decide to flip a coin...\n")
            time.sleep(game_speed)
            print(F"\n{Fore.WHITE}If it's heads, you grab a coffee.\n")
            time.sleep(game_speed)
            slow_read("If it's tails, you get a smoothie.\n")
            time.sleep(game_speed)
            slow_read("And if the coin falls out of your hand...")
            time.sleep(game_speed)
            slow_read("you can have some valium.\n")
            slow_read("You probably need it and the nurse seems nice).\n")
            time.sleep(game_speed)
            print(F"{Fore.CYAN}You flip the coin and you get... \n")
            return still_alive
    elif choice == 2:
        print("\nYou run, and slip on your own blood.")
        time.sleep(game_speed)
        print("\nA black van drives straight into you.")
        time.sleep(game_speed)
        slow_read(F"\n{Fore.RED}Sorry. You died.")
        time.sleep(game_speed)
        score_end(heroine)
        still_alive = False
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
            sleep(game_speed)
        return still_alive
        

def treats():
    treats_list = ["coffee", "smoothie", "valium"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    slow_read("\nNice! :)\n")
    """ Time to go to work!"""


def Office(heroine, enemy):
    """ Last fight """
    time.sleep(game_speed)
    print("")
    slow_read(F"{Fore.YELLOW}\nCHAPTER FOUR: The Last Battle.\n")
    slow_read(F"\n{Fore.WHITE}You walk to work carefully... \n")
    slow_read("go through the revolving doors and into the office.\n")
    slow_read("Your colleagues look nervous as they look up.\n")
    time.sleep(game_speed / 2)
    print(f"Someone whispers,'{heroine.name}!'\n")
    time.sleep(game_speed)
    print("'We've got a new boss!'\n")
    time.sleep(game_speed)
    slow_read(
        F"{Fore.GREEN}'But what happened to our old one?', you ask.\n")
    time.sleep(game_speed / 2)
    slow_read(
        F"\n{Fore.CYAN}'She got voted out in a horrible takeover!'\n")
    slow_read("'It all happened last night....\n'")
    time.sleep(game_speed / 2)
    slow_read(F"\n{Fore.WHITE}Everyone looks down as a man approaches.\n")
    slow_read("He looks polite, wears a suit, and smiles kindly.\n")
    time.sleep(game_speed / 2)
    print(f"\n'Hi,{heroine.name}, my name is {enemy.get_enemy_name()}'\n")
    time.sleep(game_speed)
    print("\n'I'm so sorry but you don't work here anymore.'")
    slow_read(F"\n{Fore.CYAN}'But why?!' You ask.")
    slow_read("\n'I went through hell to get here!!!'")
    time.sleep(game_speed)
    print(F"\n{Fore.WHITE}He smiles nicely.")
    print("\n'Because my people get what they want,' he says.")
    print("")
    print("")
    slow_read("Suddenly, your workmate Conor stands up\n")
    slow_read(
        f"...and throws a stapler at {enemy.get_enemy_name()}'s head.\n")
    slow_read("Others join in.\n")
    slow_read("Your desk-neighbour Quinn throws a book at him...\n")
    print("\n(it's a copy of Tom Paine's 'The Rights of Man')\n")
    time.sleep(game_speed)
    print("")
    print("")
    print("And that was how the revolution started!\n")
    time.sleep(game_speed)
    print("")
    print("In the words of Charles Bukowski:\n")
    print("")
    print("")
    time.sleep(game_speed)
    slow_read("There is a light somewhere...\n")
    slow_read("it may not be much light but\n")
    slow_read("it beats the darkness.'\n")
    score_end(heroine)


# Main Program #

running = True
play_the_game = True

while running:
    intro_text()  
    # clear()
    play_the_game = play_or_not()  # returns true or false
    # clear()
    if play_the_game:
        heroine = heroine_select()  # returns a heroine class
        heroine.print_stats()  # display stats
        Schlafly = Enemy("Schlafly", 60, 3000)  # create first enemy
        play_the_game = Bus_Fight(Schlafly)  
        # passes enemy to Bus_Fight and returns if you survived or not
        if not play_the_game:
            running = False
        else:
            del Schlafly
            perks_select(heroine)
            Trump = Enemy("Trump", 100, 3500)
            play_the_game = Fight_Trump(heroine, Trump)
            if play_the_game:
                del Trump
                treats()
                Kavanaugh = Enemy("Kavanaugh", 40, 2500)
                Office(heroine, Kavanaugh)
    else:
        running = False
        
    player_name = score_end(heroine)  
