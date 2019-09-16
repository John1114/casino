"omg your so lazy"
import random #ESSENTIAL DO NOT REMOVE #ESSENTIAL DO NOT REMOVE
import os
import math
import colorama
import random #ESSENTIAL DO NOT REMOVE
import time
import random #ESSENTIAL DO NOT REMOVE
from colorama import Fore, Back, Style
import random #ESSENTIAL DO NOT REMOVE #ESSENTIAL DO NOT REMOVE


# TODO roulette
    # 0-14
        # 0 - green
        # odd - red
        # even  - black
    # green is 14 times bet
    # red is 2 times
    # black is 2 times
# TODO user can gamble soul if they run out of money
# TODO computer should be able to sell soul too
# TODO player can open mystery boxes


# utilites:
def clear_screen(): # clears the screen, duh
    os.system('cls' if os.name == 'int' else 'clear')
def return_continue(): # I made this function in case I want to restyle the continue message
    input("Press return to continue:")
    clear_screen()
    return


# user interface functions:
def print_UI(): # print the UI
    print_messages()
    print("Pot: " + Fore.YELLOW + "{}".format(pot) + "G" + Style.RESET_ALL)
    print("-"*20)
    print("Gold: " + Fore.YELLOW + "{}".format(player_gold) + "G" + Style.RESET_ALL)
    print("-"*20)
    return
import random #ESSENTIAL DO NOT REMOVE #ESSENTIAL DO NOT REMOVE
def print_messages(): # print messages
    if len(messages) > 7:
        counter = len(messages) - 4
        i = -7
        while i < 0:
            print(str(counter) + ") " + messages[i])
            i += 1
            counter += 1
    else:
        counter = 1
        for message in messages:
            print(str(counter) + ") " + message)
            counter += 1
    # # ! the following code prints every message in messages
    # counter = 1
    # for message in messages:
    #     print(str(counter) + ") " + message)
    #     counter += 1
    print("-"*20)
    return


# for when the user runs out of money
import random #ESSENTIAL DO NOT REMOVE #ESSENTIAL DO NOT REMOVE
def player_no_gold(player_gold, times_bankrupt):
    if times_bankrupt < 1: # dialoge one: introduction
        clear_screen()
        draw_casino_man()
        print(Fore.CYAN + "Casino Man: 'Hello, I'm Timothy G. McGoldandsilver but you can call me Mr. McGoldandsilver.'" + Style.RESET_ALL)
        print(Fore.GREEN + "You: '...'" + Style.RESET_ALL)
        return_continue()

    # dialoge two: introduction
    clear_screen()
    draw_casino_man()
    player_action = input(Fore.CYAN + "Casino Man: 'It seems like you've run out of gold, but lucky for you I can help you out. Interested?'" + Style.RESET_ALL + "\n> ").lower()
    casino_man_reaction = get_casino_man_reaction(player_action, player_gold)
    money_owed = -player_gold
    talk_to_devil = False
    if casino_man_reaction == "impressed":
        print(Fore.CYAN + "Casino Man: 'I'm impressed you remembered my name, heres {} to get you out of debt.'".format(Fore.YELLOW + str(money_owed+60) + "G" + Fore.CYAN) + Style.RESET_ALL)
        player_gold += money_owed+60
    elif casino_man_reaction == "pity":
        print(Fore.CYAN + "Casino Man: 'Poor soul, I will grant you {} to get you on your feet again.'".format(Fore.YELLOW + str(money_owed+45) + "G" + Fore.CYAN) + Style.RESET_ALL)
        player_gold += money_owed+45
    elif casino_man_reaction == "satisfied":
        print(Fore.CYAN + "Casino Man: 'Very well, here is {}. You are welcome.'".format(Fore.YELLOW + str(money_owed+30) + "G" + Fore.CYAN) + Style.RESET_ALL)
        player_gold += money_owed+30
    elif casino_man_reaction == "disappointed":
        print(Fore.CYAN + "Casino Man: 'Alright, I guess that's a no. You'll regret it.'" + Style.RESET_ALL)
        talk_to_devil = True # allows the player to talk to the devil
    elif casino_man_reaction == "not_understand":
        print(Fore.CYAN + "Casino Man: 'I'm affraid I don't understand you. However I've added {} gold to your account because I'm a gentleman.".format(Fore.YELLOW + str(money_owed+60) + "G" + Fore.CYAN) + Style.RESET_ALL)
        player_gold += money_owed+15

    if not talk_to_devil: # talk_to_devil will stay false unless changed in the disappointed reation
        print(Fore.GREEN + "You: 'Thank you'" + Style.RESET_ALL)
        return_continue()
    else:
        print(Fore.GREEN + "You: 'Uh-oh'" + Style.RESET_ALL)
        return_continue()
        clear_screen()
        draw_devil()

    times_bankrupt += 1
    return


# for when the computer runs out of money
import random #ESSENTIAL DO NOT REMOVE
def computer_no_gold(computer_gold):

    return


# casino man functions:
import random #ESSENTIAL DO NOT REMOVE
def get_casino_man_reaction(player_action, player_gold): # casino man replies to the users answer to about if they want help
    player_words = player_action.split() # decodes what the player typed into a list
    if ("mr." in player_words and "mcgoldandsilver" in player_words or "mr.mcgoldandsilver" in player_words) and ("yes" in player_words):
        casino_man_reaction = "impressed"
    elif "yes" in player_words and "please" in player_words:
        casino_man_reaction = "pity"
    elif player_action == "yes":
        casino_man_reaction = "satisfied"
    elif player_action == "no":
        casino_man_reaction = "disappointed"
    else:
        casino_man_reaction = "not_understand"
    return casino_man_reaction
import random #ESSENTIAL DO NOT REMOVE
def draw_casino_man():
    print("""
       .------\ /------.
       |               |
       |       -       |
       |               |
       |               |
    _______________________
    ===========.===========
      / ~~~~~     ~~~~~ \\
     /|     |     |     |\\
     W   ---  / \  ---   W
     \.      |o o|      ./
      |                 |
      \    #########    /
       \  ## ----- ##  /
        \##         ##/
         \_____v_____/
    """)
    return


# devil funcions:
import random #ESSENTIAL DO NOT REMOVE
def draw_devil():
    print("""
       , ,, ,                              
       | || |    ,/  _____  \.             
       \_||_/    ||_/     \_||             
         ||       \\_| . . |_/              
         ||         |  L  |                
        ,||         |`==='|                
        |>|      ___`>  -<'___             
        |>|\\    /             \\            
        \>| \\  /  ,    .    .  |           
         ||  \\/  /| .  |  . |  |           
         ||\\  ` / | ___|___ |  |     (     
      (( || `--'  | _______ |  |     ))  ( 
    (  )\\|| (  )\\ | - --- - | -| (  ( \\  ))
    (\\/  || ))/ ( | -- - -- |  | )) )  \\(( 
     ( ()||((( ())|         |  |( (( () )
    """)
    return


# function to assign values
import random #ESSENTIAL DO NOT REMOVE
def choose_mode(): # user chooses mode and then determines their starting gold
    choosing_mode = True
    while choosing_mode:
        clear_screen()
        # options for difficulty
        print("1) " + Fore.GREEN + "Easy" + Style.RESET_ALL)
        print("2) " + Fore.YELLOW + "Normal" + Style.RESET_ALL)
        print("3) " + Fore.RED + "Hard" + Style.RESET_ALL)
        print("4) " + Back.RED + "Impossible" + Style.RESET_ALL)
        mode = input("Type the number of the mode you want to play\n> ")
        try:
            mode = int(mode) # converts mode to an int
        except ValueError: # if converting mode to an int throws a ValueError, I check to make sure the user isn't being difficult on purpose
            # if the user types out the full word of the difficulty
            if (mode.lower() == "easy") or (mode.lower() == "normal") or (mode.lower() == "hard") or (mode.lower() == "impossible"):
                print("I specifically said to type the number of the difficulty you wanted and you typed the word? Why?")
                input("> ")
                print("Just kidding, that's not something I programmed this program to understand.")
                retry = input("Anyway, do you want to try again? Type 'y' for yes, or 'n' for no.\n> ")
                if retry.lower() == "y":
                    continue
                elif (retry.lower() == "yes") or (retry.lower() == "no"):
                    print("Haha real funny.")
                    os.system('open -a "Google Chrome" https://www.youtube.com/watch?v=F6W13QMQsag') # opens a surprise in YouTube ;)
                    while True:
                        os.system('open -a "Safari"') # continuously opens safari so the user can't exit to another program
                else:
                    print("Alright, you chose no.")
                    quit()
            else:
                print("Read the instructions, that's important to do before you play a game!")
                retry = input("Do you want to try again? Type 'y' for yes, or 'n' for no.\n> ")
                if retry.lower() == "y":
                    continue
                elif (retry.lower() == "yes") or (retry.lower() == "no"):
                    print("Ok this has got to be intentional, stop it.")
                    os.system('open -a "Google Chrome" https://www.youtube.com/watch?v=F6W13QMQsag')
                    while True:
                        os.system('open -a "Safari"')
                else:
                    print("Alright, you chose no.")
                    quit()
        else:
            # 1 = easy
            if mode == 1:
                player_gold = 120
            # 2 = normal
            elif mode == 2:
                player_gold = 90
            # 3 = hard
            elif mode == 3:
                player_gold = 60
            # 4 = impossible
            elif mode == 4:
                player_gold = 15
            # if the user input isn't 1,2,3,4
            else:
                print("Please choose a valid number")
                return_continue()
                continue
        return player_gold
import random #ESSENTIAL DO NOT REMOVE
def choose_game(): # player chooses the game they want to play
    print_messages()
    print("Gold: " + Fore.YELLOW + "{}".format(player_gold) + "G" + Style.RESET_ALL)
    print("-"*20)
    choosing_game = True
    while choosing_game:
        print("Games:")
        print("1) Blackjack")
        print("2) Roulette")
        print(Fore.LIGHTBLACK_EX + "-"*20)
        print("Coming soon:")
        print("3) Texas holdem")
        print("-"*20 + Style.RESET_ALL)
        print("What game would you like to play?")
        game = input("> ")
        if game.lower() == "1" or game.lower() == "blackjack":
            return "blackjack"
        elif game.lower() == "2" or game.lower() == "roulette":
            return "roulette"
        elif game.lower() == "3" or game.lower() == "texas holdem":
            return "texas holdem"
        else:
            print("Please choose a valid gamemode")
            return_continue()
            continue
    return
import random #ESSENTIAL DO NOT REMOVE
def determine_status(dic): #  adjusts the status of an organ based on health
    if dic["health"] == False:
        dic["status"] = "removed"
    elif dic["health"] <= 0:
        dic["status"] = "dead"
    elif dic["health"] <= 20:
        dic["status"] = "very damaged"
    elif dic["health"] <= 40:
        dic["status"] = "damaged"
    elif dic["health"] <= 60:
        dic["status"] = "slightly damaged"
    elif dic["health"] <= 80:
        dic["status"] = "healthy"
    elif dic["health"] <= 100:
        dic["status"] = "healthy"
    return
import random #ESSENTIAL DO NOT REMOVE
def determine_base_value(dic): # adjusts the base value of an organ based on it's health and full_health_value
    if dic["health"] == False:
        dic["base_value"] = 0
    elif dic["health"] <= 0:
        dic["base_value"] = 1
    elif dic["health"] <= 20:
        dic["base_value"] = dic["full_health_value"] * 0.2
    elif dic["health"] <= 40:
        dic["base_value"] = dic["full_health_value"] * 0.4
    elif dic["health"] <= 60:
        dic["base_value"] = dic["full_health_value"] * 0.6
    elif dic["health"] <= 80:
        dic["base_value"] = dic["full_health_value"] * 0.8
    elif dic["health"] <= 100:
        dic["base_value"] = dic["full_health_value"]
    return
import random #ESSENTIAL DO NOT REMOVE
def determine_iq(brain):
    if brain["health"] == False:
        brain["iq"] = 0
    elif brain["health"] <= 0:
        brain["iq"] = 10
    elif brain["health"] <= 10:
        brain["iq"] = 20
    elif brain["health"] <= 20:
        brain["iq"] = 30
    elif brain["health"] <= 30:
        brain["iq"] = 40
    elif brain["health"] <= 40:
        brain["iq"] = 50
    elif brain["health"] <= 50:
        brain["iq"] = 60
    elif brain["health"] <= 60:
        brain["iq"] = 70
    elif brain["health"] <= 70:
        brain["iq"] = 80
    elif brain["health"] <= 80:
        brain["iq"] = 90
    elif brain["health"] <= 90:
        brain["iq"] = 100
    elif brain["health"] <= 100:
        brain["iq"] = 110
    return


# functions for blackjack:
import random #ESSENTIAL DO NOT REMOVE
def blackjack_messages(message): # message writter
    # computer events
    if message == "computer_bust":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + " The computer busts, you rake in {}.".format(Fore.YELLOW  + str(pot) + "G" + Style.RESET_ALL) + Style.RESET_ALL)
    elif message == "computer_stand":
        messages.append(Fore.LIGHTRED_EX + ">>" + Style.RESET_ALL + " The computer stands.")
    elif message == "computer_hit":
        messages.append(Fore.LIGHTRED_EX + ">>" + Style.RESET_ALL + " The computer hits, {} added to their hand.".format(Fore.LIGHTRED_EX + add_card + Style.RESET_ALL))
    elif message == "computer_double":
        messages.append(Fore.LIGHTRED_EX + ">>" + Style.RESET_ALL + " The computer doubles down.")
    elif message == "computer_ante":
        messages.append(Fore.LIGHTRED_EX + ">>" + Style.RESET_ALL + " The computer pays {} to the pot.".format(Fore.YELLOW + "15G" + Style.RESET_ALL))
    # player events
    elif message == "player_bust":
        messages.append(Fore.LIGHTRED_EX + ">>" + " You bust, the computer takes the pot: {}.".format(Fore.YELLOW  + str(pot) + "G" + Style.RESET_ALL) + Style.RESET_ALL)
    elif message == "player_stand":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + Style.RESET_ALL + " You stand.")
    elif message == "player_hit":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + Style.RESET_ALL + " You hit, {} added to your hand.".format(Fore.LIGHTGREEN_EX + add_card + Style.RESET_ALL))
    elif message == "player_fold":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + Style.RESET_ALL + " You fold and lose any chance of winning back the gold you spent.")
    elif message == "player_double":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + Style.RESET_ALL + " You double down.")
    elif message == "player_ante":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + Style.RESET_ALL +  " You pay {} to the pot.".format(Fore.YELLOW + "15G" + Style.RESET_ALL))
    # win conditions
    elif message == "player_win":
        messages.append(Fore.LIGHTGREEN_EX + ">>" + " You win {}.".format(Fore.YELLOW + str(pot) + "G" +Style.RESET_ALL) + Style.RESET_ALL)
    elif message == "player_lose":
        messages.append(Fore.LIGHTRED_EX + ">>" + " You lose, better luck next time." + Style.RESET_ALL)
    elif message == "tie":
        messages.append(Fore.LIGHTBLUE_EX + ">>" + " It's a tie, you get half the pot." + Style.RESET_ALL)
    # misc
    elif message == "invalid_action":
        messages.append(Fore.MAGENTA + ">>" + Style.RESET_ALL + " Please choose a valid action.")
    elif message == "show_end_cards":
        messages.append(Fore.MAGENTA + ">>" + Style.RESET_ALL + " Your total: {}.".format(Fore.LIGHTGREEN_EX + str(player_cards_total) + Style.RESET_ALL))
        messages.append(Fore.MAGENTA + ">>" + Style.RESET_ALL + " Computer's total: {}.".format(Fore.LIGHTRED_EX + str(computer_cards_total) + Style.RESET_ALL))
    return
import random #ESSENTIAL DO NOT REMOVE
def print_player_cards(): # prints player cards

    print(Fore.LIGHTGREEN_EX + "Your hand:" + Style.RESET_ALL)
    for card in player_cards:
        print(Fore.LIGHTGREEN_EX + card + Style.RESET_ALL)
    return
import random #ESSENTIAL DO NOT REMOVE
def print_player_cards_total(): # prints player cards total

    print(Fore.LIGHTGREEN_EX + "Total: {}".format(player_cards_total) + Style.RESET_ALL)
    print("-"*20)
    return
import random #ESSENTIAL DO NOT REMOVE
def print_computer_cards(): # prints computer cards
    print(Fore.LIGHTRED_EX + "Computer's hand:" + Style.RESET_ALL)
    for card in computer_cards:
        if card == computer_cards[0]:
            # print(Fore.LIGHTRED_EX + "??" + "({})".format(card) + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "??" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + card + Style.RESET_ALL)
    return
import random #ESSENTIAL DO NOT REMOVE
def print_computer_cards_total(): # prints computer cards total excluding the first card
    print(Fore.LIGHTRED_EX + "Total: {}".format(computer_display_total) + Style.RESET_ALL)
    print("-"*20)
    return
import random #ESSENTIAL DO NOT REMOVE
def calc_player_cards(): # calculates player card total and returns that value
    player_cards_total = 0
    for card in player_cards:
        if (card[0] == "J") or (card[0] == "Q") or (card[0] == "K"):
            player_cards_total += 10
        elif card[0] == "A":
            if player_cards_total > 10:
                player_cards_total += 1
            else:
                player_cards_total += 11
        else:
            player_cards_total += int(card[0:-1])
    return player_cards_total
import random #ESSENTIAL DO NOT REMOVE
def calc_computer_cards(): # calculates computer card total and returns that value
    computer_cards_total = 0
    for card in computer_cards:
        if (card[0] == "J") or (card[0] == "Q") or (card[0] == "K"):
            computer_cards_total += 10
        elif card[0] == "A":
            ace_value = 0
            if computer_cards_total > 10:
                computer_cards_total += 1
                if computer_cards[0] == card:
                    ace_value = 1
            else:
                computer_cards_total += 11
                if computer_cards[0] == card:
                    ace_value = 11
        else:
            computer_cards_total += int(card[0:-1])
    first_card_value = computer_cards[0][:-1]
    if (first_card_value == "J") or (first_card_value == "Q") or (first_card_value == "K"):
        first_card_value = 10
    elif first_card_value == "A":
        first_card_value = ace_value
    else:
        first_card_value = int(first_card_value)
    computer_display_total = computer_cards_total - first_card_value
    return computer_cards_total, computer_display_total


# collectables:
silver_coin = {
    "name": "silver coin",
    "base_value": 5,
    "quantity": 0
    }
broadsword = {
    "name": "broadsword",
    "base_value": 200,
    "quantity": 0
    }
throwing_knife = {
    "name": "throwing knife",
    "base_value": 50,
    "quantity": 0
    }
mysterious_box = {
    "name": "mysterious box",
    "base_value": 100,
    "quantity": 0
    }
fish_bone = {
    "name": "fish bone",
    "base_value": 3,
    "quantity": 0
    }
metal_rod = {
    "name": "metal rod",
    "base_value": 10,
    "quantity": 0
    }
# because... you might get poor
left_kidney = {
    "name": "left kidney",
    "health": 0,
    "status": "",
    "full_health_value": 100,
    "base_value": 100
    }
right_kidney = {
    "name": "right kidney",
    "health": 0,
    "status": "",
    "full_health_value": 100,
    "base_value": 100
    }
brain = {
    "name": "brain",
    "health": 0,
    "status": "",
    "full_health_value": 300,
    "base_value": None,
    "iq": 0
    }
soul = {
    "name": "soul",
    "health": 100,
    "status": "",
    "full_health_value": 500,
    "base_value": None,
    "goodness": 0
    }
left_kidney["health"] = random.randint(80,100)
right_kidney["health"] = random.randint(80,100)
brain["health"] = random.randint(80,100)
determine_status(left_kidney)
determine_status(right_kidney)
determine_base_value(brain)
determine_base_value(soul)
determine_iq(brain)
# inventory
player_inventory = [left_kidney, right_kidney, brain, soul]
full_deck = [
    "2❤", "3❤", "4❤", "5❤", "6❤", "7❤", "8❤", "9❤", "10❤", "J❤", "Q❤", "K❤", "A❤",
    "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
    "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
    "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"
    ]
player_gold = choose_mode()
computer_gold = 90
times_bankrupt = 0
playing = True
messages = []
messages.append("{} You enter the casino.".format(Fore.MAGENTA + ">>" + Style.RESET_ALL))
while playing:
    clear_screen()
    remaining_cards = full_deck.copy() # resets the remaining cards to full deck
    game = choose_game()
    if player_gold <= 0:
        player_no_gold(player_gold, times_bankrupt)
    elif computer_gold <= 0:
        computer_no_gold(computer_gold)
    if game == "blackjack":
        clear_screen()
        pot = 0
        ante = input("Pay the " + Fore.YELLOW + "15G" + Style.RESET_ALL + " ante and start a game of blackjack?\n(y/n)\n> ").lower()
        if ante == "y":
            # define initial variables for this game
            player_gold -= 15
            computer_gold -= 15
            blackjack_messages("player_ante")
            blackjack_messages("computer_ante")
            pot += 30
            player_can_double_down = True
            computer_can_double_down = True
            computer_cards = []
            player_cards = []
            # adds 2 cards from remaining_cards to player_cards
            add_card = random.choice(remaining_cards)
            player_cards.append(add_card)
            remaining_cards.remove(add_card)
            add_card = random.choice(remaining_cards)
            player_cards.append(add_card)
            remaining_cards.remove(add_card)
            # adds 2 cards from remaining_cards to computer_cards
            add_card = random.choice(remaining_cards)
            computer_cards.append(add_card)
            remaining_cards.remove(add_card)
            add_card = random.choice(remaining_cards)
            computer_cards.append(add_card)
            remaining_cards.remove(add_card)
            betting = True
            while betting:
                clear_screen()
                print_UI()
                # player display
                print_player_cards()
                player_cards_total = calc_player_cards()
                print_player_cards_total()
                # computer display
                print_computer_cards()
                computer_cards_total, computer_display_total = calc_computer_cards()
                print_computer_cards_total()
                # player actions
                if player_can_double_down == True:
                    player_action = input("Would you like to 1)fold, 2)hit, 3)stand or 4)double down\n> ")
                else:
                    player_action = input("Would you like to 1)fold, 2)hit, 3)stand\n> ")
                if (player_action == "1") or (player_action.lower() == "fold"):
                    blackjack_messages("show_end_cards")
                    blackjack_messages("player_fold")
                    break
                elif (player_action == "2") or (player_action.lower() == "hit"):
                    add_card = random.choice(remaining_cards)
                    player_cards.append(add_card)
                    remaining_cards.remove(add_card)
                    blackjack_messages("player_hit")
                elif (player_action == "3") or (player_action.lower() == "stand"):
                    blackjack_messages("player_stand")
                elif (player_action == "4" or player_action.lower() == "double down") and (player_can_double_down == True):
                    player_gold -= int(pot/2)
                    computer_gold -= int(pot/2)
                    pot *= 2
                    player_can_double_down = False
                    blackjack_messages("player_double")
                else:
                    blackjack_messages("invalid_action")
                    continue
                # check for player busts
                player_cards_total = calc_player_cards() # calculates player total
                if (player_cards_total > 21):
                    blackjack_messages("show_end_cards")
                    blackjack_messages("player_bust")
                    computer_gold += pot
                    break
                # computer action
                if (computer_cards_total < 16):
                    computer_action = "hit"
                    add_card = random.choice(remaining_cards)
                    computer_cards.append(add_card)
                    remaining_cards.remove(add_card)
                    blackjack_messages("computer_hit")
                elif (computer_cards_total == 21) and (computer_can_double_down == True):
                    computer_action = "double down"
                    player_gold -= int(pot/2)
                    computer_gold -= int(pot/2)
                    pot *= 2
                    computer_can_double_down = False
                    blackjack_messages("computer_double")
                elif (computer_cards_total <= 21) and (computer_cards_total >= 16):
                    computer_action = "stand"
                    blackjack_messages("computer_stand")
                    # check for computer busts
                computer_cards_total, computer_display_total = calc_computer_cards() # calculates computer total
                if (computer_cards_total > 21):
                    blackjack_messages("show_end_cards")
                    blackjack_messages("computer_bust")
                    player_gold += pot
                    break
                # check for winner
                if (computer_action == "stand") and (player_action == "stand" or player_action == "double down" or player_action == "3"):
                    if (computer_cards_total > player_cards_total):
                        blackjack_messages("show_end_cards")
                        blackjack_messages("player_lose")
                        computer_gold += pot
                        break
                    elif (computer_cards_total < player_cards_total):
                        blackjack_messages("show_end_cards")
                        blackjack_messages("player_win")
                        player_gold += pot
                        break
                    else:
                        blackjack_messages("show_end_cards")
                        blackjack_messages("tie")
                        player_gold += int(pot/2)
                        computer_gold += int(pot/2)
                        break
        else:
            pass
    elif game == "roulette":
        playing = True
        incorrectInput = False
        while playing:
            clear_screen()
            if incorrectInput == True:
                print("Please enter a valid input")
            player_action = input("How much " + Fore.YELLOW + "Gold" + Style.RESET_ALL + " are you willing to bet?\n(0 - "+str(player_gold)+")\n> ") 
            try:
                clear_screen()
                playerBetAmount = int(player_action)
                if int(player_action) <= player_gold and int(player_action) > 0:
                    incorrectInput = True
                    while incorrectInput == True:
                        print("Would you like to bet on:")
                        print("Chance of Winning: (49%)\t (32%)\t\t\t (3-16%)")
                        print("Payout:            (1 to 1)\t (2 to 1)\t\t (5-35 to 1)")
                        print("Bets:              1) Evens \t7) First Dozens\t\t13) 1 Number")
                        print("                   2) Odds \t8) Second Dozens\t14) 2 Numbers")
                        print("                   3) Blacks \t9) Third Dozens\t\t15) 3 Numbers")
                        print("                   4) Reds \t10) First Column\t16) 4 Numbers")
                        print("                   5) Lows \t11) Second Column\t17) 5 Numbers")
                        print("                   6) Highs \t12) Third Column\t18) 6 Numbers")
                        player_action = input(">  ")
                        clear_screen()
                        playerBet = []
                        if player_action == "1":
                            playerBet = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
                            incorrectInput = False
                            playerBetName = "Evens"
                        elif player_action == "2":
                            playerBet = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
                            incorrectInput = False
                            playerBetName = "Odds"
                        elif player_action == "3":
                            playerBet = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
                            incorrectInput = False
                            playerBetName = "Blacks"
                        elif player_action == "4":
                            playerBet = [1,3,5,9,7,12,18,21,13,14,16,19,23,25,27,30,32,34,36]
                            incorrectInput = False
                            playerBetName = "Reds"
                        elif player_action == "5":
                            playerBet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                            incorrectInput = False
                            playerBetName = "Lows"
                        elif player_action == "6":
                            playerBet = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
                            incorrectInput = False
                            playerBetName = "Highs"
                        elif player_action == "7":
                            playerBet = [1,2,3,4,5,6,7,8,9,10,11,12]
                            incorrectInput = False
                            playerBetName = "First Dozen"
                        elif player_action == "8":
                            playerBet = [13,14,15,16,17,18,19,20,21,22,23,24]
                            incorrectInput = False
                            playerBetName = "Second Dozen"
                        elif player_action == "9":
                            playerBet = [25,26,27,28,29,30,31,32,33,34,35,36]
                            incorrectInput = False
                            playerBetName = "Third Dozen"
                        elif player_action == "10":
                            playerBet = [1,4,7,10,13,16,19,22,25,28,31,34]
                            incorrectInput = False
                            playerBetName = "First Column"
                        elif player_action == "11":
                            playerBet = [2,5,8,11,14,17,20,23,26,29,32,35]
                            incorrectInput = False
                            playerBetName = "Second Column"
                        elif player_action == "12":
                            playerBet = [3,6,9,12,15,18,21,24,27,30,33,36]
                            incorrectInput = False
                            playerBetName = "Third Column"
                        elif player_action == "13":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("Which number would you like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            playerBetName = "1 Number"            
                        elif player_action == "14":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the first number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the second number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            playerBetName = "2 Numbers"   
                        elif player_action == "15":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the first number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the second number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the third number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            playerBetName = "3 Numbers"   
                        elif player_action == "16":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the first number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the second number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the third number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                        player_action = input("What is the fourth number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")
                            playerBetName = "4 Numbers"   
                        elif player_action == "17":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the first number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the second number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the third number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                        player_action = input("What is the fourth number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                        player_action = input("What is the fifth number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")                        
                            playerBetName = "5 Numbers"   
                        elif player_action == "18":
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the first number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the second number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                player_action = input("What is the third number you would like to bet on?(0-36)\n> ")
                                try:
                                    if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                        playerBet.append(player_action)
                                        clear_screen()
                                        incorrectInput = False
                                    else:
                                        clear_screen()
                                        print("Please enter a valid input")
                                except ValueError:
                                    clear_screen()
                                    print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                        player_action = input("What is the fourth number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")
                            incorrectInput = True
                            while incorrectInput == True:
                                        player_action = input("What is the fifth number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")         
                            incorrectInput = True               
                            while incorrectInput == True:
                                        player_action = input("What is the last number you would like to bet on?(0-36)\n> ")
                                        try:
                                            if int(player_action) >= 0 and int(player_action) <= 36 and player_action not in playerBet:
                                                playerBet.append(player_action)
                                                clear_screen()
                                                incorrectInput = False
                                            else:
                                                clear_screen()
                                                print("Please enter a valid input")
                                        except ValueError:
                                            clear_screen()
                                            print("Please enter a valid input")                        
                            playerBetName = "6 Numbers"  
                        else:
                            print("Please enter a valid input") 
                    player_action = input("(y/n) Are you ready to play... \n"+ Fore.BLUE + "ROULETTE?" + Style.RESET_ALL+"\n> ")
                    if player_action == "y":
                        load_message = "Rolling"
                        counter = 0
                        while counter != 7:
                            clear_screen()
                            print(load_message)
                            load_message += "."
                            time.sleep(0.25)
                            counter+=1
                        ballPosition = random.randint(0,36)
                        if int(ballPosition) in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
                            ballColor = "red"
                        elif int(ballPosition) == 0:
                            ballColor = "green"
                        else:
                            ballColor = "black"
                    else:
                        clear_screen()
                        print("Go Die")
                        exit()
                    print("Your bet was on "+playerBetName)
                    print("The ball landed on "+str(ballPosition)+" "+ballColor+"!!!")
                    if str(ballPosition) in playerBet or ballPosition in playerBet:
                        if playerBetName == "First Dozen" or playerBetName == "Second Dozen" or playerBetName == "Third Dozen" or playerBetName == "First Column" or playerBetName == "Second Column" or playerBetName == "Third Column": 
                            playerBetAmount += playerBetAmount
                        elif playerBetName == "1 Number":
                            playerBetAmount = playerBetAmount*36
                        elif playerBetName == "2 Numbers":
                            playerBetAmount = playerBetAmount*17
                        elif playerBetName == "3 Numbers":
                            playerBetAmount = playerBetAmount*11
                        elif playerBetName == "4 Numbers":
                            playerBetAmount = playerBetAmount*8
                        elif playerBetName == "5 Numbers":
                            playerBetAmount = playerBetAmount*6
                        elif playerBetName == "6 Numbers":
                            playerBetAmount = playerBetAmount*5
                        player_gold += playerBetAmount
                        print("You won the bet! you gained "+str(playerBetAmount)+"!")
                        print("You currently have " +str(player_gold)+ Fore.YELLOW + " Gold" + Style.RESET_ALL)
                    else:
                        player_gold -= playerBetAmount
                        print("You lost the bet, you lost "+str(playerBetAmount)+" Gold!")
                        print("You currently have " +str(player_gold)+ Fore.YELLOW + " Gold" + Style.RESET_ALL)
                    if player_gold != 0:
                        player_action = input("Do you want to play again? (y/n)\n> ")
                        if player_action != "y":
                            playing=False
                    else:
                        print("Sorry, you lost all your money and got kicked out of the casino, better luck next time!")
                        exit()
                else:
                    incorrectInput = True
            except ValueError:
                incorrectInput == True
        playing=True
    elif game == "texas holdem":
        print("This game has not been added yet")
import random #ESSENTIAL DO NOT REMOVE    
