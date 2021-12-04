#--------------------------
# D&D 5e stat roller
# Rolls either 3d6 or 4d6 drop lowest in order 
#
# Created by Jeremy, Dec 4 2021
#--------------------------

import random
import math
from typing import Counter
#random.seed() # sets the RNG seed

#Global lists
stat_names = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
stat_numbers = [10, 10, 10, 10, 10 , 10]
stat_mods = [0, 0, 0, 0, 0, 0]

#Functions
def d6(): #Random number 1-6, simulates a d6
    return random.randint(1,6)

def stat_roller(n): #rolls N dice and keeps the 3 highest
    dice = [0, 0, 0 , 0]
    #Asign random number to each spot in the list
    for counter in range(0,n):
        dice[counter] = d6()
    
    #picks the 3 higest dice
    dice.sort()
    total = dice[3] + dice[2] + dice[1]
    return str(total)

def convert_modifer(n): #Converts the stat to a modifer
    return str(math.floor((n - 10)/2))

#Fills all positions of stat_numbers with a random number from 3 - 18
#N is the number of dice to roll when generating the number 
def create_stats(n): 
    for counter in range(0,6):
        stat_numbers[counter] = stat_roller(n)
    return 0

#Fills all positions of stat_mods with a modifer basied on the stat in the same list location
# ie mod[2] is created from stat[2]
def create_modiders():
    for counter in range(0,6):
        stat_mods[counter] = convert_modifer(int(stat_numbers[counter]))

#Fancy print funcations, each one will add the approprate spaces for the length of the string
def print_name(list):
    for counter in range(0,6):
        print("| "+ list[counter] + " ", end ="" ) 
    print("|") 

def print_stat(list):
    for counter in range(0,6):
        if len(list[counter]) == 2:
            print("| " + " " + list[counter] + " ", end ="" )
        elif len(list[counter]) == 1:
            print("| " + "  " + list[counter] + " ", end ="" )

    print("|") 

def print_mod(list): #Adds a + for positive modifers 
    for counter in range(0,6):
        if len(list[counter]) == 2:
            print("| " + " " + list[counter] + " ", end ="" )
        elif len(list[counter]) == 1:
            print("| " + " +" + list[counter] + " ", end ="" )

    print("|") 

def print_line():
    print("-------------------------------------")

#Main
print("How to generate stats?")
number = int(input("(3)d6 or (4)d6 drop lowest: "))

create_stats(int(number))
create_modiders()

print_line()
print_name(stat_names)
print_stat(stat_numbers)
print_mod(stat_mods)
print_line()
