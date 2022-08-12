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


# player's allies

class CloseFriends:
    """ Top helpers for the player, 2nd only to the women's support group! """
    fightingSpirit = 20
    selfEsteem = 20
    energyLevels = 500
    intelligence = 200
    bodyImage = 500
    calories = 2000
    sleep = 8


class CoWorkers:
    """ Relatively weak allies for the player """
    fightingSpirit = 5
    selfEsteem = 30
    energyLevels = 1000
    intelligence = 2
    bodyImage = 2000
    calories = 500
    sleep = 5


class NonToxicFamily:
    """ These allies are nice, and even life-savers """
    fightingSpirit = 200
    selfEsteem = 200
    energyLevels = 1000
    intelligence = 200
    bodyImage = 1000
    calories = 2000
    sleep = 7


class KindStrangers:
    "Allies who are undercover guardian angels. Very powerful."
    fightingSpirit = 3000
    selfEsteem = 1000
    energyLevels = 2000
    intelligence = 500
    bodyImage = 2000
    calories = 2980
    sleep = 12


class WomensSupportGroup:
    """ Super Top Allies of the player """
    fightingSpirit = 5000
    selfEsteem = 3000
    energyLevels = 4000
    intelligence = 1000
    bodyImage = 4000
    calories = 3900
    sleep = 8

    
