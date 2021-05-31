import os, sys
from bs4 import BeautifulSoup
import requests
import csv

class Game:

    def __init__(self, home, away, time, date, home_person="", away_person="", home_score=None, away_score=None):
        self.home_team = home
        self.away_team = away
        self.time = time
        self.date = date
        self.home_person = home_person
        self.away_person = away_person
        self.home_score = home_score
        self.away_score = away_score

    def __str__(self):
        return(self.home_team + " vs. " + self.away_team + " at " + self.time + " on " + self.date)

    def add_result(self, input_dict):
        self.home_score = input_dict[self.home_team]
        self.away_score = input_dict[self.away_team]

    def assign_people(self, person_dict):
        self.home_person = person_dict[self.home_team]
        self.away_person = person_dict[self.away_team]

def main():

    url = 'https://www.eurosport.com/football/calendar-result_evt36881.shtml'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    divs = soup.find_all('div')

    teams = []
    games = []
    time = ""
    date = ""
    for div in divs:
        try:

            if div['class'][0] == 'team__name':
                teams.append(div.get_text())
            if div['class'][0] == 'match__time':
                time = div.get_text()
            if div['class'][0] == 'date-caption':
                date = div.get_text()
        except:
            pass
        
        if len(teams) == 2 and len(time) > 0 and len(date) > 0:
            games.append(Game(teams[0], teams[1], time, date))
            teams = []
            time = ""

    # Get list of all teams
    all_teams = set()
    for game in games:
        all_teams.add(game.home_team)
        all_teams.add(game.away_team)

    with open(os.path.join("data", "teams.txt"), "w") as f:
        for team in all_teams:
            f.write(team + ",\n")

    # Assign all the people to games
    with open(os.path.join('data', 'draw.csv'), 'r', newline='') as f:
        reader = csv.reader(f)
        team_assignation = dict(reader)

    for game in games:
        print(game)
        print(team_assignation)
        game.assign_people(team_assignation)

    # Write a csv with home, away, people etc.
    with open(os.path.join("data", "games.csv"), "w") as f:
        f.write("Home, Away, Time, Date, Home Person, Away Person, Home Score, Away Score\n")
        for game in games:
            f.write(f"{game.home_team},{game.away_team},{game.time},{game.date},{game.home_person},{game.away_person},{game.home_score},{game.away_score}\n")

if __name__ == "__main__":
    main()