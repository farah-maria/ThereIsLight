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


# Player heroine options. You get to choose which you want to be in the game.
class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def printStats(self):
        """ Calls the stats on the choice of Heroine  """
        print(f"You have selected {self.name}. These are their stats: ")
        print(f"fighting spirit - {self.fighting_spirit}")
        print(f"self esteem - {self.self_esteem}")
        print(f"calories to burn - {self.calories_to_burn}")


Demeter = Heroine("Demeter", 80, 80, 2800)

Persephone = Heroine("Persephone", 90, 50, 1500)

Athena = Heroine("Athena", 100, 90, 2000)

Lilith = Heroine("Lilith", 75, 40, 3500)

Roe = Heroine("Roe", 100, 95, 3000)

# Enemies of the player!!!


class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn
    heroine_perks = random.randint(0, 2)


Kavanaugh = Enemy("Kavanaugh", 40, 2500)

Schlafly = Enemy("Schlafly", 60, 3000)

Trump = Enemy("Trump", 100, 3500)


def heroine_perks():
    heroine_perks = ["coffee", "anti_patriarchial_zapper", "cake"]
    perk_rand_select = random.randint(0, 2)
    perk_appear = heroine_perks[perk_rand_select]
    return perk_appear


def perk_effect(perk_appear, Heroine):
    if perk_appear == "coffee":
        Heroine.fighting_spirit + 10
        print("You drink the super-strong, delicious coffee.")
        print("It's boosted your fighting spirit by 10 points! :) ")
        print(f"Your new fighting spirit score is {Heroine.fighting_spirit}")
        return Heroine


def enemySelect(Kavanaugh, Schlafly, Trump):
    """ Randomly chooses one of the three enemies to fight player"""
    enemiesList = [Kavanaugh, Schlafly, Trump]
    chance = random.randint(0, 2)
    opponent = enemiesList[chance]
    return opponent


def heroine_select():
    """ Allows player to choose which heroine they play as"""
    selection = input(
        "1. Demeter \n2. Persephone  \n3. Flora \n4. Lilith \n5. Roe \n")
   
    if selection == "1":
        selectedCharacter = Demeter
        Demeter.printStats()

    elif selection == "2":
        selectedCharacter = Persephone
        Persephone.printStats()
        return selectedCharacter

    elif selection == "3":
        selectedCharacter = Athena
        Athena.printStats()
        return selectedCharacter
    
    elif selection == "4":
        selectedCharacter = Lilith
        Lilith.printStats()
        return selectedCharacter

    elif selection == "5":
        selectedCharacter = Roe
        Roe.printStats()
        return selectedCharacter

    else:
        print("Error! Only press 1, 2, 3, 4 or 5 and press enter")
        heroine_select()


def play_or_not():
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


# Start and intro to game

print("This is a game where winning is hard.")
print("The situation is as follows... ")
print("You wake up trapped in a patriarchial nightmare.")
print("The odds are staked against you.")
print("Not even in an interesting way...")
print("...but in a 'Meh, really? Pfft.' kinda way.")
print("The aim is to get to work. Not in real time.")
print("There will be enemies! And enemies are a drag!")
print("You will always have options: either y/n...")
print("...or a number you need to select to choose a pathway.")
print("Remember to press 'enter' afterwards.")
print("Also, you can pick up points, which increases your score...")
print("... by eating cake and winning fights.")
print("Would you like to play?")

play_or_not()