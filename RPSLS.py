#--------------------------
# Rock Paper Scissors Lizard Spock
# Plays a game vs the 'AI'
# Includes rules if needed
#
# Created by Jeremy, Dec 5 2021
#--------------------------

import random

score = [0,0] # score tracker [0] = Player

#Adds 1 to a given players score
def increase_score(n):
    score[n] += 1

#unused in this version
def reset_score():
    score = [0,0]

#print a line, used for formatting
def print_line():
    print("--------------")

#print the Score in a fancy way
def print_score():
    print("Player: " + str(score[0]))
    print("Ai    : " + str(score[1]))

#Picks the Ai's hand and reports on it
def get_ai_hand():
    number = random.randint(0,4)
    print("Ai picked: " + convert_hand_toString(number))
    return number

#Gets the player's hand and reports on it
def get_player_hand():
    print_line()
    print("Rock (1) Paper (2) Scissors (3) Lizard (4) Spock (5)")
    print_line()
    number = int(input("Which hand do you use? "))
    print("You picked: " + convert_hand_toString(number))
    return number

#Compares the two hands retuns 1 if the player wins
def compare_hands(player, ai): # See convert_hand_toString for hand meanings
    if player == ai:
        return -1 #tie
    elif player == 1 and (ai == 3 or ai == 4):
        return 0 #player wins
    elif player == 2 and (ai == 1 or ai == 5):
        return 0 #player wins
    elif player == 3 and (ai == 2 or ai == 4):
        return 0 #player wins
    elif player == 4 and (ai == 2 or ai == 5):
        return 0 #player wins
    elif player == 5 and (ai == 1 or ai == 3):
        return 0 #player wins
    else:
        return 1 #ai wins

# Prints the results and counts the score
def results(result):
    print_line()
    if result == -1: #Tie
        print ("Tie Game!")
    elif result == 0: #player win
        print("You Win! :) ")
        increase_score(result)
    else: #player lose
        print("You Lost :( ")
        increase_score(result)
    print("==============")
    
#Converts the hands to strings so they can be printed
def convert_hand_toString(n):
    match n:
        case 1:
            hand = "Rock"
        case 2:
            hand = "Paper"
        case 3:
            hand = "Scissors"
        case 4:
            hand = "Lizard"
        case 5:
            hand = "Spock"
    return hand


#Game Play loop
def game():
    again = True
    while again == True: 
        # get hands
        player = get_player_hand()
        ai = get_ai_hand()
        # compare hands
        result = compare_hands(player, ai)
        results(result)
        print_score()

        if input("Play again? (T) or (F): ").upper() != "T":
            again = False

#prints the rules of the game
def rules():
    print("The rules are:")
    print(" Scissors cuts paper,")
    print(" Paper covers rock, ")
    print(" Rock crushes lizard,")
    print(" Lizard poisons Spock,")
    print(" Spock smashes scissors, ")
    print(" Scissors decapitates lizard, ")
    print(" Lizard eats paper, ")
    print(" Paper disproves Spock, ")
    print(" Spock vaporizes rock, ")
    print(" and as it always has, Rock crushes scissors.")
    print_line()

    # Lets you read the rules again, if you want to
    if input("Ready to play? (T)rue or (F)alse: ").upper() != "T":
        rules()
    else:
        return


# Main
print("Play Rock Paper Scissors Lizard Spock!")
if input("Read the rules? (T)rue or (F)alse: ").upper() != "T":
    game()
else: 
    rules()
    game()
