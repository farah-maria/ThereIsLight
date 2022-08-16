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
class Character:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn, hrs_of_sleep):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn
        self.hrs_of_sleep = hrs_of_sleep

    def printStats(self):
        print(f"You have selected {self.name}. These are their stats: ")
        print(f"fighting spirit - {self.fighting_spirit}")
        print(f"self esteem - {self.self_esteem}")
        print(f"calories to burn - {self.calories_to_burn}")
        print(f"hours of sleep - {self.hrs_of_sleep}")


EarthGoddess = Character("Earth Goddess", 80, 80, 2500, 11)
""" She's an awesome heroine with high-energy vibes """

OfficeFiend = Character("Office Fiend", 100, 60, 1500, 5)
""" She's a fantastic heroine, but just a bit tired. """

NiceyNorah = Character("Nicey Norah", 30, 40, 3, 4)
""" Norah is a nice heroine. And niceness is underrated. """

HighPriestess = Character("High Priestess", 100, 100, 3500, 15)
""" A very powerful heroine to play. She knows in her gut what's right."""

CoolFeminist = Character("Cool Feminist", 100, 120, 3000, 8)

# Enemies of the player!!!


class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn


MansplainingMick = Enemy("MansplainingMick", 40, 2500)
heroine_points = random.randint(0, 2)
UnwokeEddie = Enemy("UnwokeEddie", 60, 3000)
heroine_points = random.randint(0, 2)
PatriarchialPete = Enemy("PatriarchialPete", 100, 3500)
heroine_points = random.randint(0, 2)
    
    
def heroine_select():
    selection = input(
        "1. EarthGoddess \n2. OfficeFiend  \n3. NiceyNorah \n4. HighPriestess \n5. CoolFeminist \n")
   
    if selection == "1":
        selectedCharacter = EarthGoddess
        print("You have selected the Earth Goddess. These are their stats: ")
        EarthGoddess.printStats()

    elif selection == "2":
        selectedCharacter = OfficeFiend
        print("You have selected the Office Fiend. These are their stats: ")
        OfficeFiend.printStats()
        return selectedCharacter

    elif selection == "3":
        selectedCharacter = NiceyNorah
        print("You have selected NiceyNorah. These are their stats: ")
        NiceyNorah.printStats()
        return selectedCharacter
    
    elif selection == "4":
        selectedCharacter = HighPriestess
        print("You have selected the High Priestess. These are their stats: ")
        HighPriestess.printStats()
        return selectedCharacter

    elif selection == "5":
        selectedCharacter = CoolFeminist
        print("You have selected the Cool Feminist. These are their stats: ")
        CoolFeminist.printStats()
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
print("...but in a 'Ah Jesus, really?! This again?' kinda way.")
print("The aim is to just get through a morning. Not in real time.")
print("There will be enemies! And enemies are a drag!")
print("But you can score points, and maybe even win.")
print("You will always have options: either y/n...")
print("...or a number you need to select to choose a pathway.")
print("Remember to press 'enter' afterwards.")
print("Also, you can pick up energy points through this 'adventure' from...")
print("...eating and sleeping. And winning fights.")
print("Would you like to play?")

play_or_not()
