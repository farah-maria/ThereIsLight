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
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn, hrs_of_sleep):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn
        self.hrs_of_sleep = hrs_of_sleep

    def printStats(self):
        """ Calls the stats on the choice of Heroine  """
        print(f"You have selected {self.name}. These are their stats: ")
        print(f"fighting spirit - {self.fighting_spirit}")
        print(f"self esteem - {self.self_esteem}")
        print(f"calories to burn - {self.calories_to_burn}")
        print(f"hours of sleep - {self.hrs_of_sleep}")


Demeter = Heroine("Demeter", 80, 80, 2500, 11)
""" She's an awesome heroine with high-energy vibes """

Persephone = Heroine("Persephone", 100, 60, 1500, 5)
""" She's a fantastic heroine, but just a bit tired. """

Athena = Heroine("Athena", 30, 40, 3, 4)
""" Norah is a nice heroine. And niceness is underrated. """

Lilith = Heroine("Lilith", 100, 100, 3500, 15)
""" A very powerful heroine to play. She knows in her gut what's right."""

Roe = Heroine("Roe", 100, 120, 3000, 8)

# Enemies of the player!!!


class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn


Kavanaugh = Enemy("Kavanaugh", 40, 2500)
heroine_points = random.randint(0, 2)
Schlafly = Enemy("Schlafly", 60, 3000)
heroine_points = random.randint(0, 2)
Trump = Enemy("Trump", 100, 3500)
heroine_points = random.randint(0, 2)


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
        print("You have selected Demeter. These are their stats: ")
        Demeter.printStats()

    elif selection == "2":
        selectedCharacter = Persephone
        print("You have selected Persephone. These are their stats: ")
        Persephone.printStats()
        return selectedCharacter

    elif selection == "3":
        selectedCharacter = Athena
        print("You have selected Athena. These are their stats: ")
        Athena.printStats()
        return selectedCharacter
    
    elif selection == "4":
        selectedCharacter = Lilith
        print("You have selected Lilith. These are their stats: ")
        Lilith.printStats()
        return selectedCharacter

    elif selection == "5":
        selectedCharacter = Roe
        print("You have selected Roe. These are their stats: ")
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
print("When it's not hard, it can get monotonous.")
print("When it's neither of the above...")
print("a surprising breakthrough may be in store :)")
print("The situation is as follows... ")
print("You wake up trapped in a patriarchial nightmare.")
print("The odds are staked against you.")
print("Not even in an interesting way...")
print("...but in a 'Meh, really' kinda way.")
print("The aim is to get through a morning. Not in real time.")
print("There will be enemies! And enemies are a drag!")
print("But you can score points, and maybe even win.")
print("You will always have options: either y/n...")
print("...or a number you need to select to choose a pathway.")
print("Remember to press 'enter' afterwards.")
print("Also, you can pick up points, which increases your score...")
print("... by eating cake and winning fights.")
print("Would you like to play?")

play_or_not()