# File name:    Exercise4_6.py
# Author:       Eerik Vainio
# Description:  A game of dice, the player with the highest roll wins.
#               Players are also assigned mammals as pets, and can name them.

import random

class Die:
    def __init__(self, index):
        self.index = index
        self.total_value = 0
        self.rolls = []
        self.player = None

    def __str__(self):
        return f'Die #{self.index}'
    
    def roll(self):
        value = random.randint(1,6)
        self.total_value += value
        self.rolls.append(value)
        return value

    def clear_value(self):
        self.total_value = 0

    def assign_to_player(self, player):
        self.player = player

class Player:
    def __init__(self, name, id, pet, die):
        self.name = name
        self.id = id
        self.pet = pet
        self.die = die

    def __str__(self):
        return f'{self.name} (Person ID #{self.id})'
    
class Mammal:
    def __init__(self, species, name, size, weight):
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

# Function for rolling all dice in a list 3 times
def Roll_dice(dice, rolls):
    for die in dice:
        for y in range(rolls):
            die.roll()
        print(f"{die.player}'s die: {die.total_value} ({die.rolls})")

# Function to check for all dice that have the highest value
def Check_winners(dice):
    highest_score = 0
    winning_dice = []
    for die in dice:
        if (die.total_value > highest_score):
            highest_score = die.total_value
            winning_dice.clear()
            winning_dice.append(die)
        elif (die.total_value == highest_score):
            winning_dice.append(die)
    return winning_dice

# List of mammals
list_of_mammals = [
    ["Black-footed ferret", "45cm", "1,02kg"],
    ["Japanese giant flying squirrel", "90cm", "1,65kg"],
    ["Large bamboo rat", "50cm", "3,00kg"],
    ["Black-tailed jack rabbit", "61cm", "4,17kg"],
    ["Sun-tailed monkey", "56cm", "5,40kg"],
    ["Side-striped jackal", "81cm", "10,25kg"],
    ["Indian crested porcupine", "91cm", "20,00kg"],
    ["Eastern roe deer", "146cm", "39,45kg"],
    ["Pacific white-sided dolphin", "2,4m", "103,00kg"],
    ["Caribbean manatee", "3,5m", "322,00kg"],
    ["Northern elephant seal", "5m", "1600,00kg"]
    ]


    
# The game

# Asking for the number of players
while True:
    amount_of_players = input("Give the number of players: ")
    if (not amount_of_players.isnumeric()):
        print(f'"{amount_of_players}" is not a valid number')
    else:
        amount_of_players = int(amount_of_players)
        break

# Asking for number of dice rolls
while True:
    amount_of_rolls = input("How many times do the players roll their dice: ")
    if (not amount_of_rolls.isnumeric()):
        print(f'"{amount_of_rolls}" is not a valid number')
    else:
        amount_of_rolls = int(amount_of_rolls)
        break

# Creating the Die objects
for player in range(amount_of_players):
    list_of_dice = [Die(x) for x in range(amount_of_players)]

# Assigning pets to players and adding the players to a dictionary
dict_of_players = {}
mammal_die1 = Die(0)
mammal_die2 = Die(0)
for x in range(amount_of_players):
    player_name = input(f'Input the name of player #{x}: ')
    player_roll = list_of_mammals[mammal_die1.roll() + mammal_die2.roll() - 3]
    print(f'{player_name} got a {player_roll[0]} as their pet. It is {player_roll[1]} tall and weighs {player_roll[2]}')
    player_pet_name = input(f'Give a name to the {player_roll[0]}: ')
    player_pet = Mammal(player_roll[0], player_pet_name, player_roll[1], player_roll[2])
    player_die = list_of_dice[x]

    created_player = Player(player_name, x, player_pet, player_die)

    dict_of_players.update({created_player.id: created_player})

    list_of_dice[x].player = created_player.name

# Rolling the dice and checking for winners until there's only one winner
winning_dice = list_of_dice
while (len(winning_dice) > 1):
    for winning_die in winning_dice:
        winning_die.clear_value()
    print(f'Rolling {len(winning_dice)} dice:')
    Roll_dice(winning_dice, amount_of_rolls)
    winning_dice = Check_winners(winning_dice)

for x in dict_of_players:
    if dict_of_players[x].die == winning_dice[0]:
        winning_player = dict_of_players[x]

print(f'With a score of {winning_dice[0].total_value}, the winners are {winning_player.name} and their {winning_player.pet.species} {winning_player.pet.name}!')