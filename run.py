""" Modules allow random selection, colour, time delay and scores record """
import random
import colorama
import gspread
import time
from colorama import Fore
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
# (pre-story set up of code


class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def printStats_and_start(self): 
        # STARTS THE GAME AFTER PLAYER CHOOSES 'Y' (in PART 1)
        """ Calls stats on player's choice of Heroine,""" 
        """ & starts the story (with a bus fight!)"""
        global heroine
        print(f"You have selected {self.name}. These are their stats: ")
        print(f"fighting spirit - {self.fighting_spirit}")
        print(f"self esteem - {self.self_esteem}")
        print(f"calories to burn - {self.calories_to_burn}")  
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

###################################################################
# STORY: start at the bottom of the page for part 1 and move up.
###################################################################

# PART EIGHT of EIGHT: FIGHTING KAVANAUGH AT WORK. THE OFFICE IS UNSAFE!


def Office():
    global heroine
    print("You walk to work carefully...")
    print("go through the revolving doors and into the office.")
    print("Your colleagues look nervous as they look up to greet you.")
    print(f"Someone whispers, '{heroine.name}...'")
    print("'We've got a new boss!'")
    print("'But what happened to our old one?', you ask.")
    print("'She got voted out in some kind of horrible takeover!'")
    print("'It all happened last night....'")
    print("Everyone looks down as a man approaches.")
    print("He looks polite, and smiles kindly.")
    print(f"'Hi, {heroine.name}, my name is Kavanaugh...'")
    print("'I'm sorry, but you don't work here anymore.'")
    print("'But why?!' You ask. 'I went through hell to get here!!!'")
    print("He smiles nicely. 'Because my people like to get what they want,'")
    print("At this point, your workmate Conor stands up...")
    print("and throws a stapler at Kavanaugh's head.")
    print("Others do the same. Your desk-neighbour Paul throws a book at him.")
    print("And that was how the revolution started.")
    print("Have a great day, and stand up for yourself.")
    print("In the words of Charles Bukowski:")
    print("'There is a light somewhere.")
    print("it may not be much light but")
    print("it beats the darkness.'")
    print("Game over.")
    exit()


# PART SEVEN: IF PLAYER BEAT TRUMP, TREATS!! AND TIME TO GO TO WORK.


def treats():
    treats_list = ["coffee", "smoothie", "valium"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    print("Nice! :)")
    Office()
    """ Time to go to work!"""


# PART SIX - FIGHT TRUMP, OR NO FREE MEDICAL TREATMENT!


def Fight_Trump():
    global heroine
    """a fight for medical care"""
    print("You're feeling pretty damn good about yourself...")
    print("and you cross the road to a tall, glass building.")
    print("These are the offices where you work.")
    print("With a coffee still in one hand, you push at the revolving door...")
    print("And bang your face. Someone pushed it in the opposite direction...")
    print("Blood streams from your nose. It feels broken.")
    print("Holding your nose, you run to the hospital.") 
    print("It's only a block away... and work would make you go anyway.")
    print("But at the main entrance to the emergency department...")
    print("stands a squarish, tanned man shaking his head.")
    print(f"'No free medical care for you, {heroine.name}.")
    print("'I've called the cops on you. Your insurance ran out years ago.'")
    print("Three black vans pull up by the hospital gate.")
    print("The men who get out...")
    print("They don't look like police officers, more like private security.")
    print("You have three options... ")
    choice = input(
        "1. Use your injustice_zapper \n2. Run! \n3. Call the police.")
    if choice == "1":
        print("You point the anti-injustice zapper at Trump.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 3:
            print("But Trump's men get to you before you zapp anyone... ")
            print("They bundle you into the back of a van.")
            print("Oh dear.")
            print("Game over.")
            exit()
        elif defeat_chance < 4:
            Trump.fighting_spirit -= 90 
            print("You manage to stun him, then turn and zapp all the others.")
            print("Trump's fighting spirit has been knocked by 90 points...")
            print(f"and is now down to just {Trump.fighting_spirit}.")
            print("It'll be a while before he poses a problem again...")
            print("Though, most likely he'll be back. Well done, anyway.")
            print("You get the medical treatment you need...")
            print("and are able to return to work.")
            print("You decide to flip a coin...")
            print("If it's heads, you grab a coffee.")
            print("If it's tails, you get a smoothie.")
            print("And if the coin falls out of your hand...")
            print("you can have some valium. (You probably need it).")
            print("You flip the coin and you get... ")
            treats()
            """ treats for if you beat Trump """
 
    elif choice == 2:
        print("You run, and slip on your own blood.")
        print("A black van drives straight into you.")
        print("Sorry. You died.")
        print("Game over.")
        exit()
    else:
        print("The police don't arrive in time.")
        print("But some medical staff run out the building.")
        print("A nurse gets Trump in the neck with a needle...")
        print("The security men scatter.")
        print("You get the care you need, and everyone is smiling.")
        print("You decide to flip a coin...")
        print("If it's heads, you grab a coffee.")
        print("If it's tails, you get a smoothie.")
        print("And if the coin falls out of your hand...")
        print("you can have some valium. (You probably need it).")
        print("You flip the coin and you get... ")
        treats()
        """Treats for if you beat Trump"""


# PART FIVE - IF BEAT SCHLAFLY, GO TO CAFE & GET READY TO FIGHT TRUMP!


def perks_select():
    """ heroine gets a perk that raises score after defeating Schlafly """
    global heroine
    perk_chance = random.randint(0, 10)
    if perk_chance > 5:
        print("Tails!")
        print("You get a large coffee AND a big slice of chocolate cake.")
        heroine.fighting_spirit += 100
        heroine.calories_to_burn += 300
        heroine.self_esteem += 200
        print("Your fighting spirit increases by 100pts...")
        print(
            f"to {heroine.fighting_spirit}.")
        print("Your calories to use for fighting increase by 200,") 
        print(f"to {heroine.calories_to_burn}.")
        print("& your self-esteem has gone up by 200pts")
        print(f"to: {heroine.self_esteem}.")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
    elif perk_chance < 6:
        print("Heads!")
        heroine.fighting_spirit += 50
        print("You grab a coffee. Caffiene boosts your fighting spirit...")
        print(f"by 50 points, to {heroine.fighting_spirit} :)")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
                

# PART FOUR: A BUS FIGHT WITH SCHLAFLY!

def Bus_Fight():
    global heroine
    """ First battle of heroine Vs opponent """
    print(F"{Fore.WHITE}You get on a bus. It is 8am.")
    print("You have 20mins to read before work.")
    print("Just as you get your book out of your bag...")
    print("a dangerous enemy sits next to you...")
    print("...blocking your way out into the aisle.")
    print("Hello', she says. 'My name's Schlafly...")
    print("'I don't think you should be going to work,' she continues...") 
    print("She draws a tiny gun from the pocket of her cardigan.")
    print(F"{Fore.BLUE}You have two choices: ")
    choice = input("1. Use your injustice_zapper \n2. Push her and run!")
    if choice == "1":
        print("You point the anti-injustice zapper at Schlafly.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 7:
            print(F"{Fore.WHITE}Schlafly knocks the zapper out of your hands")
            print("and shoots you.")
            print("Oh dear. You're dead. You'll never get to work, now.")
            print("Game over. Sorry!")
            exit()
        elif defeat_chance < 8:
            Schlafly.fighting_spirit -= 40 
            print(F"{Fore. WHITE}You managed to stun her. She falls.")
            print("Her fighting spirit has been knocked by 40 points...")
            print(f"and is now down to just {Schlafly.fighting_spirit}.")
            print("She'll have less energy to pester other people, now :)")
            print("Well done!")
            print("The bus stops near the office and you get off.")
            print("You decide to flip a coin...")
            print("If it's heads, you grab a coffee from the cafe opposite.")
            print("If it's tails, you get coffee AND cake.")
            print("And if the coin falls out of your hand...")
            print("you can have a coffee and a pain au chocolate")
            print("You flip the coin and you get... ")
            
            perks_select()
    else:
        print(F"{Fore. WHITE}Schlafly gets right back up...")
        print("... and shoots you in the back as you try to run.")
        print("Sorry. She won. You died.")
        print("Game over.")
        exit()


# PART THREE: If 'Y', choose a character & move to a bus fight!!


def heroine_select():
    global heroine
    """ Allows player to choose which heroine they play as"""
    selection = input(
        "1. Demeter \n2. Persephone  \n3. Flora \n4. Lilith \n5. Roe \n")
   
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
        print(F"{Fore.RED}Error! Only press 1, 2, 3, 4 or 5 and press enter")
        heroine_select()


# PART TWO - WANNA PLAY OR NOT?


def play_or_not():
    """ player chooses to continue to game or quit """
    answer = input(F"{Fore.GREEN}Answer 'y' or 'n': ")
    if answer.lower().strip() == "y":
        print(F"{Fore.WHITE}Choose which heroine you want to play as...")
        heroine_select()
    elif answer.lower().strip() == "n":
        print(F"{Fore.WHITE}I don't blame you. Bye!")
        exit()
    else:
        print(F"{Fore.RED}Incorrect input!")
        print("Try again. Just one letter and press enter.")
        play_or_not()


# PART ONE: Intro to game. Takes player to decision: play or not 
print("This is a game where winning is hard.")
print("The situation is as follows... ")
print("You wake up trapped in a patriarchial nightmare.")
print("The odds are staked against you.")
print("There will be enemies! And enemies are a drag!")
print("But you will always have options: either y/n...")
print("...or a number you need to select to choose a pathway.")
print("Remember to press 'enter' afterwards.")
print("Also, you can pick up points, which increases your score...")
print("... by eating cake and winning fights.")
print(F"{Fore.GREEN}1Would you like to play?")

play_or_not()       