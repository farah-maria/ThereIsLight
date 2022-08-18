""" These modules allow for random selection and scores record """
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


class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn


    def printStats_and_start(self): #STARTS THE GAME AFTER PLAYER CHOOSES 'Y' (PART OF PART 1 IN NARRATIVE)
        """ Calls stats on player's choice of Heroine,""" 
        """ & starts the story (with a bus fight!)"""
        global selectedCharacter
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
