import os

class FootballPlayer:
    def __init__(self, pid, name, country, age, goals, assists, team_titles, indiv_titles, mvp):
        self.pid = pid
        self.name = name
        self.country = country
        self.age = age
        self.goals = goals
        self.assists = assists
        self.team_titles = team_titles
        self.indiv_titles = indiv_titles
        self.mvp = mvp

    def display_row(self):
        return f"{self.pid:<4}{self.name:<20}{self.country:<12}{self.age:<12}{self.goals:<14}{self.assists:<16}{self.team_titles:<12}{self.indiv_titles:<12}{self.mvp}"

# File name
filename = "t.txt"

# Create file with header if not exists
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("ID  Name                Country     Age (2025)   Goals         Assists         TeamTitles        IdvTitles      Ballon d'Or\n")

# Read existing players
players = []
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines[1:]:  # skip header
        data = line.strip().split(maxsplit=8)
        if data:
            players.append(FootballPlayer(*data))

# Display header
print(f"{'ID':<4}{'Name':<20}{'Country':<12}{'Age (2025)':<12}{'Goals':<14}{'Assists':<16}{'TeamTitles':<12}{'IdvTitles':<12}{'Ballon d\'Or'}")
print("-"*140)

# Display all players
for p in players:
    print(p.display_row())

# Input new player
print("\nEnter new player details:")
pid = input("ID: ")
name = input("Name: ")
country = input("Country: ")
age = input("Age (2025): ")
goals = input("Goals: ")
assists = input("Assists: ")
team_titles = input("Team Titles: ")
indiv_titles = input("Individual Titles: ")
mvp = input("Ballon d'Or: ")

new_player = FootballPlayer(pid, name, country, age, goals, assists, team_titles, indiv_titles, mvp)

# Append new player to file
with open(filename, "a", encoding="utf-8") as file:
    file.write(f"{new_player.pid} {new_player.name} {new_player.country} {new_player.age} {new_player.goals} {new_player.assists} {new_player.team_titles} {new_player.indiv_titles} {new_player.mvp}\n")

players.append(new_player)

# Display updated table
print("\n⚽ Updated Football Player Stats ⚽")
print(f"{'ID':<4}{'Name':<20}{'Country':<12}{'Age (2025)':<12}{'Goals':<14}{'Assists':<16}{'Titles':<12}{'Titles':<12}{'Ballon d\'Or'}")
print("-"*140)
for p in players:
    print(p.display_row())
