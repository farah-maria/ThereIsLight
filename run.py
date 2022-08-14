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
class EarthGoddess(object):
    """ She's an awesome heroine with high-energy vibes """
    fighting_spirit = 10 
    self_esteem = 8
    calories_to_burn = 2000 
    hrs_of_sleep = 8


class OfficeFiend(object):
    """ She's a fantastic heroine, but just a bit tired. """
    fighting_spirit = 20 
    self_esteem = 10
    calories_to_burn = 1500 
    hrs_of_sleep = 4


class NiceyNorah(object):
    """ Norah is a nice heroine. And niceness is underrated. """
    fighting_spirit = 4 
    self_esteem = 3
    calories_to_burn = 1000 
    hrs_of_sleep = 4


class HighPriestess(object):
    " A very powerful heroine to play. She knows in her gut what's right."
    fighting_spirit = 50
    self_esteem = 50
    calories_to_burn = 3000 
    hrs_of_sleep = 12
    

class CoolFeminist(object):
    fighting_spirit = 50 
    self_esteem = 50
    calories_to_burn = 2500 
    hrs_of_sleep = 8

# Enemies of the player!!!


class RandomMansplainer(object):
    """ Enemy who reduces player's power through the game """
    name = "mansplainer"
    strength = 20
    defence = 9000
    heroine_points = random.randint(0, 2)


class RandomUnWoke(object):
    """ Enemy who reduces player's power through the game """
    name = "random sexist-in-pub type"
    strength = 60
    defence = 900
    heroine_points = random.randint(0, 2)


class TerribleBoss(object):
    """ Enemy who reduces player's power through the game """
    name = "male boss from another company with no diverisity training"
    strength = 30
    defence = 10000
    heroine_points = random.randint(0, 2)


def heroine_select():
    selection = input(
        "1. EarthGoddess \n2. OfficeFiend  \n3. NiceyNorah \n4. HighPriestess \n5. CoolFeminist \n")
    if selection == "1":
        character = EarthGoddess
        print("You have selected the Earth Goddess. These are their stats: ")
        print("Fighting spirit - ", character.fighting_spirit)
        print("Self esteem - ", character.self_esteem)
        print("Calories 2 burn - ", character.calories_to_burn)
        print("Hours of sleep - ", character.hrs_of_sleep)
        return character

    elif selection == "2":
        character = OfficeFiend()
        print("You have selected the Office Fiend. These are their stats: ")
        print("Fighting spirit - ", character.fighting_spirit)
        print("Self esteem - ", character.self_esteem)
        print("Calories 2 burn - ", character.calories_to_burn)
        print("Hours of sleep - ", character.hrs_of_sleep)
        return character

    elif selection == "3":
        character = NiceyNorah
        print("You have selected NiceyNorah. These are their stats: ")
        print("Fighting spirit - ", character.fighting_spirit)
        print("Self esteem - ", character.self_esteem)
        print("Calories 2 burn - ", character.calories_to_burn)
        print("Hours of sleep - ", character.hrs_of_sleep)
        return character
    
    elif selection == "4":
        character = HighPriestess
        print("You have selected the High Priestess. These are their stats: ")
        print("Fighting spirit - ", character.fighting_spirit)
        print("Self esteem - ", character.self_esteem)
        print("Calories 2 burn - ", character.calories_to_burn)
        print("Hours of sleep - ", character.hrs_of_sleep)
        return character
    
    elif selection == "5":
        character = CoolFeminist
        print("You have selected the Cool Feminist. These are their stats: ")
        print("Fighting spirit - ", character.fighting_spirit)
        print("Self esteem - ", character.self_esteem)
        print("Calories 2 burn - ", character.calories_to_burn)
        print("Hours of sleep - ", character.hrs_of_sleep)
        return character
    
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
