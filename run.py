# Write your code to expect a terminal of 80 characters wide and 24 rows high
""" These modules allow for random selection and scores record """
import random
import gspread
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

selectedCharacter = {}
# Pre-action definitions... Heroine info (player chooses which to play):


class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def printStats_and_start(self):
        global selectedCharacter
        """ Calls stats on choice of Heroine, & starts story (bus fight)"""
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


# random functions sprinkled through game to help player


def treats():
    treats_list = ["coffee", "coffee & cake", "coffee & a pain au chocolat"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    print("Nice! :)")


def perks_select():
    """ heroine gets a perk that raises score """
    global selectedCharacter
    perk_chance = random.randint(0, 10)
    if perk_chance > 5:
        print("Tails!")
        print("You get a large coffee AND a big slice of chocolate cake.")
        selectedCharacter.fighting_spirit += 100
        selectedCharacter.calories_to_burn += 300
        selectedCharacter.self_esteem += 200
        print("Your fighting spirit increases by 100pts...")
        print(
            f"to {selectedCharacter.fighting_spirit}.")
        print("Your calories to use for fighting increase by 200,") 
        print(f"to {selectedCharacter.calories_to_burn}.")
        print("& your self-esteem has gone up by 200pts")
        print(f"to: {selectedCharacter.self_esteem}.")

    elif perk_chance < 6:
        print("Heads!")
        selectedCharacter.fighting_spirit += 50
        print("You grab a coffee. Caffiene boosts your fighting spirit...")
        print(f"by 50 points, to {selectedCharacter.fighting_spirit} :)")
                

# PART THREE: The bus fight! first part of real story


def Bus_Fight():
    global selectedCharacter
    """ First battle of heroine Vs opponent """
    print("You get on a bus. It is 8am. You have 20mins to read before work.")
    print("Just as you get your book out of your bag...")
    print("a dangerous enemy sits next to you...")
    print("...blocking your way out into the aisle.")
    print("Hello', she says. 'My name's Schlafly...")
    print("'I don't think you should be going to work,' she continues...") 
    print("She draws a tiny gun from the pocket of her cardigan.")
    print("You have two choices: ")
    choice = input("1. Use your injustice_zapper \n2. Push her and run!")
    if choice == "1":
        print("You point the anti-injustice zapper at Schlafly.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 5:
            print("Schlafly knocks the zapper out of your hands... ")
            print("and shoots you.")
            print("Oh dear. You're dead. You'll never get to work, now.")
            print("Game over. Sorry!")
            exit()
        elif defeat_chance < 6:
            Schlafly.fighting_spirit -= 40 
            print("You managed to stun her. She falls to the ground.")
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


# PART TWO: a) User chooses to play game or quit
    # b) If choose to play, they select a character & move to a bus fight

# b)


def heroine_select():
    """ Allows player to choose which heroine they play as"""
    global selectedCharacter
    selection = input(
        "1. Demeter \n2. Persephone  \n3. Flora \n4. Lilith \n5. Roe \n")
   
    if selection == "1":
        selectedCharacter = Demeter
        Demeter.printStats_and_start()
        return selectedCharacter
        """Heroine is taken to first part of the story"""
    elif selection == "2":
        selectedCharacter = Persephone
        Persephone.printStats_and_start()
        return selectedCharacter
    elif selection == "3":
        selectedCharacter = Athena
        Athena.printStats_and_start()
        return selectedCharacter
        """Heroine is taken to first part of the story"""
    elif selection == "4":
        selectedCharacter = Lilith
        Lilith.printStats_and_start()
        return selectedCharacter
        """Heroine is taken to first part of the story"""
    elif selection == "5":
        selectedCharacter = Roe
        Roe.printStats_and_start()
        """Heroine is taken to first part of the story"""
        return selectedCharacter
        """Heroine is taken to first part of the story"""
    else:
        print("Error! Only press 1, 2, 3, 4 or 5 and press enter")
        heroine_select()


# a)
characterSelect = None


def play_or_not():
    global characterSelect
    """ player chooses to continue to game or quit """
    answer = input(" Answer 'y' or 'n': ")
    if answer.lower().strip() == "y":
        print("Choose which heroine you want to play as...")
        heroine_select()
    elif answer.lower().strip() == "n":
        print("I don't blame you. Bye!")
        quit()
    else:
        print("Incorrect input! Try again. Just one letter and press enter.")
        play_or_not()


# PART ONE: start and intro to game

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
print("Would you like to play?")

characterSelect = None
play_or_not()        
