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
class EarthGoddess:
    """ She's an awesome heroine, with high-energy vibes """
    def __init__(self, fighting_spirit, self_esteem, calories, sleep):
        self.fighting_spirit = 500
        self.self_esteem = 4000
        self.calories = 2000
        self.sleep = 8


class WorkFiend:
    """ She's a fantastic heroine, but just a bit tired. """
    def __init__(self, fighting_spirit, self_esteem, calories, sleep):
        self.fighting_spirit = 2000
        self.self_esteem = 40
        self.calories = 2000
        self.sleep = 5


class NiceyNorah:
    """ Norah is a nice heroine. And niceness is underrated. """
    def __init__(self, fighting_spirit, self_esteem, calories, sleep):
        self.fighting_spirit = 12
        self.self_esteem = 40
        self.calories = 700  # she's on a slimfast diet
        self.sleep = 5  # it's tough worrying about doing the right thing!


class HighPriestess:
    " A very powerful heroine to play. She knows in her gut what's right."
    def __init__(self, fighting_spirit, self_esteem, calories, sleep):
        self.fighting_spirit = 3000
        self.self_esteem = 3000
        self.calories = 2690  # she eats cake when she WANTS to eat cake, ok?!
        self.sleep = 12  # sleep is essential for her powers.


class CoolFeminist:
    """ A very powerful heroine with a mind that's sharp as a magical sword """
    def __init__(self, fighting_spirit, self_esteem, calories, sleep):
        self.fighting_spirit = 5000
        self.self_esteem = 3000
        self.calories = 3000  # fighting patriarchy takes a lot of energy
        self.sleep = 8


# Enemies of the player!!!


class RandomMansplainer:
    """ Enemy who reduces player's power through the game """
    def __init__(self, strength, defence):
        name = "mansplainer"
        strength = 20
        defence = 9000
        heroine_points = random.randint(0, 2)


class RandomUnWoke:
    """ Enemy who reduces player's power through the game """
    def __init__(self, strength, defence):
        name = "random sexist-in-pub type"
        strength = 60
        defence = 900
        heroine_points = random.randint(0, 2)


class TerribleBoss:
    """ Enemy who reduce player's power through the game """
    def __init__(self, strength, defence):
        name = "male boss from another company with no diverisity training"
        strength = 30
        defence = 10000
        heroine_points = random.randint(0, 2)


def play_or_not():
    answer = input(" Answer 'y' or 'n': ")
    if answer.lower().strip() == "y":
        print("You are on a bus...")
        # lots of code
    elif answer.lower().strip() == "n":
        print("I don't blame you. Bye!")
        quit()
    else:
        print("Incorrect input! Try again. Just one letter and press enter.")
        return play_or_not()


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
print("The aim is to just get through 24 hours. Not in real time.")
print("There will be enemies! And enemies are a drag!")
print("But you can score points, and maybe even win.")
print("You will always have options: either y/n...")
print("...or a number you need to select to choose a pathway.")
print("Remember to press 'enter' afterwards.")
print("Also, you can pick up energy points through this 'adventure' from...")
print("...eating and sleeping. And winning fights.")
print("Would you like to play?")
play_or_not()
