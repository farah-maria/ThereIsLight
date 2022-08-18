""" These modules allow for random selection and scores record """
import random
import gspread
from google.oauth2.service_account import Credentials
import stats

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


# PART EIGHT of EIGHT: FIGHTING KAVANAUGH AT WORK. THE OFFICE IS UNSAFE!

selectedCharacter = {}


def Office():
    global selectedCharacter
    print("You walk to work carefully...")
    print("go through the revolving doors and into the office.")
    print("Your colleagues look nervous as they look up to greet you.")
    print(f"Someone whispers, '{selectedCharacter.name}...'")
    print("'We've got a new boss!'")
    print("'But what happened to our old one?', you ask.")
    print("'She got voted out in some kind of horrible takeover!'")
    print("'It all happened last night....'")
    print("Everyone looks down as a man approaches.")
    print("He looks polite, and smiles kindly.")
    print(f"'Hi, {selectedCharacter.name}, my name is Kavanaugh...'")
    print("'I'm sorry, but you don't work here anymore.'")
    print("'But why?!' You ask. 'I went through hell to get here!!!'")
    print("He smiles nicely. 'Because my people like to get what they want,'")
    print("'... and boys will be boys. There's no point arguing.'")
    print("At this point, your workmate Kevin stands up...")
    print("and throws a stapler at Kavanaugh's head.")
    print("Others do the same. Your desk-neighbour Paul throws a book at him.")
    print("And that was how the revolution started...")
    print("You won. Well done.")
    print("Have a great day, and stand up for yourself.")
    print("In the words of Charles Bukowski...")
    print("'There is a light somewhere.")
    print("'it may not be much light but '")
    print("'it beats the darkness.'")
    print("Game over")
    exit()


# PART SEVEN: IF PLAYER BEAT TRUMP, TREATS!! AND TIME TO GO TO WORK.


def treats():
    treats_list = ["coffee", "smoothie", "valium"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    print("Nice! :)")
    Office()
    """ Time to go to work!"""


# PART SIX - FIGHT TRUMP, OR NO FREE MEDICAL TREATMENT!
selectedCharacter = {}


def Fight_Trump():
    global selectedCharacter
    """a fight for medical care"""
    print("You're feeling pretty damn good about yourself...")
    print("and you cross the road to a tall, glass building.")
    print("These are the offices where you work.")
    print("With a coffee still in one hand, you push at the revolving door...")
    print("And bang your face. Someone pushed it in the opposite direction...")
    print("... because they were on their phone & didn't see you.")
    print("Blood streams from your nose. It might be broken.")
    print("Holding your nose, you run to the hospital.") 
    print("It's only a block away... and work would make you go anyway.")
    print("But at the main entrance to the emergency department...")
    print("stands a squarish, tanned man shaking his head.")
    print(f"'No free medical care for you, {selectedCharacter.name}.")
    print("'I've called the cops on you. Your insurance ran out years ago.'")
    print("Three black vans pull up by the hospital gate.")
    print("The men who get out...")
    print("They don't look like police officers, more like private security.")
    print("You have three options... ")
    choice = input(
        "1. Use your injustice_zapper \n2. Run! \n3. Call the police.")
    if choice == "1":
        print("You point the anti-injustice zapper at Trump.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 3:
            print("But Trump's men get to you before you zapp anyone... ")
            print("They bundle you into the back of a van.")
            print("Oh dear.")
            print("Game over.")
            exit()
        elif defeat_chance < 4:
            Trump.fighting_spirit -= 90 
            print("You manage to stun him, then turn and zapp all the others.")
            print("Trump's fighting spirit has been knocked by 90 points...")
            print(f"and is now down to just {Trump.fighting_spirit}.")
            print("It'll be a while before he poses a problem again...")
            print("Though, most likely he'll be back. Well done, anyway.")
            print("You get the medical treatment you need...")
            print("and are able to return to work.")
            print("You decide to flip a coin...")
            print("If it's heads, you grab a coffee.")
            print("If it's tails, you get a smoothie.")
            print("And if the coin falls out of your hand...")
            print("you can have some valium. (You probably need it).")
            print("You flip the coin and you get... ")
            treats()
            """ treats for if you beat Trump """
 
    elif choice == 2:
        print("You run, and slip on your own blood.")
        print("A black van drives straight into you.")
        print("Sorry. You died.")
        print("Game over.")
    else:
        print("The police don't arrive for another hour.")
        print("But...")
        print("You didn't need them. Some medical staff run out the building.")
        print("A nurse gets Trump in the neck with a needle...")
        print("The security men scatter.")
        print("You get the care you need, and everyone is smiling.")
        print("You decide to flip a coin...")
        print("If it's heads, you grab a coffee.")
        print("If it's tails, you get a smoothie.")
        print("And if the coin falls out of your hand...")
        print("you can have some valium. (You probably need it).")
        print("You flip the coin and you get... ")
        treats()
        """Treats for if you beat Trump"""


# PART FIVE - IF BEAT SCHLAFLY, GO TO CAFE & GET READY TO FIGHT TRUMP!


def perks_select():
    """ heroine gets a perk that raises score after defeating Schlafly """
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

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
    elif perk_chance < 6:
        print("Heads!")
        selectedCharacter.fighting_spirit += 50
        print("You grab a coffee. Caffiene boosts your fighting spirit...")
        print(f"by 50 points, to {selectedCharacter.fighting_spirit} :)")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
                

# PART FOUR: A BUS FIGHT WITH SCHLAFLY!

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
    else:
        print("Schlafly gets right back up...")
        print("... and shoots you in the back as you try to run.")
        print("Sorry. She won. You died.")
        print("Game over.")


# PART THREE: If 'Y', choose a character & move to a bus fight!!


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


# PART TWO - WANNA PLAY OR NOT?
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


# PART ONE: Intro to game. Takes player to decision: play or not 

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
