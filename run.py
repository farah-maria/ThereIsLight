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
    """ She's an awesome heroine, and high-energy """
    fightingSpirit = 500
    selfEsteem = 4000
    energyLevels = 6000
    intelligence = 500
    bodyImage = 1000
    calories = 2000
    sleep = 8


class WorkFiend:
    """ She's a fantastic heroine, but just a bit tired. """
    fightingSpirit = 1000
    selfEsteem = 30
    energyLevels = 1000
    intelligence = 3000
    bodyImage = 2000
    calories = 500
    sleep = 5


class NiceyNorah:
    """ Norah is a nice heroine. And niceness is underrated. """
    fightingSpirit = 200
    selfEsteem = 200
    energyLevels = 1000
    intelligence = 200
    bodyImage = 1000
    calories = 2000
    sleep = 7


class HighPriestess:
    " A very powerful heroine to play."
    fightingSpirit = 3000
    selfEsteem = 1000
    energyLevels = 2000
    intelligence = 500
    bodyImage = 2000
    calories = 2980
    sleep = 12


class Feminist:
    """ Super Top Allies of the player """
    fightingSpirit = 5000
    selfEsteem = 3000
    energyLevels = 4000
    intelligence = 1000
    bodyImage = 4000
    calories = 3900
    sleep = 8

# Enemies of the player!!!


class goblin (object):
    name = "Goblin"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0, 2)