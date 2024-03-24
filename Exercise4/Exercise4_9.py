# File name:    Exercise4_9.py
# Author:       Eerik Vainio
# Description:  A program for examining hockey league statistics
#               from a json file.

import os
import json

def read_data(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def search_player(data, player_name):
    for player in data:
        if player['name'] == player_name:
            print_player(player)
            break
    else:
        print("Player not found.")

def list_teams(data):
    teams = sorted(set(player['team'] for player in data))
    print("".join(teams))

def list_countries(data):
    countries = sorted(set(player['nationality'] for player in data))
    print("".join(countries))

def print_player(player):
    points = player['goals'] + player['assists']
    print(f"{player['name']:20}{player['team']:5}{player['goals']:2} + {player['assists']:2} = {points:3}")

def list_players_in_team(data, team):
    team_players = [player for player in data if player['team'] == team]
    team_players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)
    for player in team_players:
        print_player(player)

def list_players_from_country(data, country):
    country_players = [player for player in data if player['nationality'] == country]
    country_players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)
    for player in country_players:
        print_player(player)

def list_most_points(data, n):
    sorted_players = sorted(data, key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)[:n]
    for player in sorted_players:
        print_player(player)

def list_most_goals(data, n):
    sorted_players = sorted(data, key=lambda x: (-x['goals'], -x['games']))[:n]
    for player in sorted_players:
        print_player(player)

filename = input("file name: ")
data = read_data(filename)

while True:
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")
    userInput = input("command: ")
    
    if userInput == "0":
        break
    elif userInput == "1":
        name = input("name: ")
        search_player(data, name)
    elif userInput == "2":
        list_teams(data)
    elif userInput == "3":
        list_countries(data)
    elif userInput == "4":
        team = input("team: ")
        list_players_in_team(data, team)
    elif userInput == "5":
        country = input("country: ")
        list_players_from_country(data, country)
    elif userInput == "6":
        n = int(input("how many: "))
        list_most_points(data, n)
    elif userInput == "7":
        n = int(input("how many: "))
        list_most_goals(data, n)
    else:
        print("Invalid userInput. Please try again.")
