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
print(data)


# Player heroine options. You get to choose which you want to be in the game.

class EarthGoddess:
    """ She's an awesome heroine, with high-energy vibes """
    def __init__(self, fightingSpirit, selfEsteem, calories, sleep):
        self.fightingSpirit = 500
        self.selfEsteem = 4000
        self.calories = 2000
        self.sleep = 8


class WorkFiend:
    """ She's a fantastic heroine, but just a bit tired. """
    def __init__(self, fightingSpirit, selfEsteem, calories, sleep):
        self.fightingSpirit = 2000
        self.selfEsteem = 40
        self.calories = 2000
        self.sleep = 5


class NiceyNorah:
    """ Norah is a nice heroine. And niceness is underrated. """
    def __init__(self, fightingSpirit, selfEsteem, calories, sleep):
        self.fightingSpirit = 12
        self.selfEsteem = 40
        self.calories = 700  # she's on a slimfast diet
        self.sleep = 5  # it's tough worrying about the right thing!


class HighPriestess:
    " A very powerful heroine to play. She knows in her gut what's right."
    def __init__(self, fightingSpirit, selfEsteem, calories, sleep):
        self.fightingSpirit = 3000
        self.selfEsteem = 3000
        self.calories = 2690  # she eats cake when she WANTS to eat cake, ok?!
        self.sleep = 12  # sleep is essential for her powers. 


class EducatedFeminist:
    """ A very powerful heroine with a mind that's sharp as a magical sword """
    def __init__(self, fightingSpirit, selfEsteem, calories, sleep):
        self.fightingSpirit = 5000
        self.selfEsteem = 3000
        self.calories = 3000  # fighting patriarchy takes a lot of energy
        self.sleep = 8  

# Enemies of the player!!!


class RandomMansplainer:
    name = "mansplainer"
    health = 20
    strength = 20
    defence = 9000
    HeroinePoints = random.randint(0, 2)


class RandomTotalSexist:
    name = "random sexist-in-pub type"
    health = 10
    strength = 60
    defence = 900
    HeroinePoints = random.randint(0, 2)


class TerribleManager:
    name = "male manager from another company with no diveristy training"
    health = 800
    strength = 30
    defence = 10000
    HeroinePoints = random.randint(0, 2)