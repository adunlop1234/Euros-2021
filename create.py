import jinja2
import os, sys
import csv
from get_info import Game

# Read in the team - assignation
with open(os.path.join('data', 'draw.csv'), 'r', newline='') as f:
    reader = csv.reader(f)
    team_assignation = list(reader)

# Order team assignation in alphabetical order of name
team_assignation = sorted(team_assignation, key=lambda x: (x[1], x[0]))

# Read in the games
with open(os.path.join('data', 'games.csv'), 'r', newline='') as f:
    reader = csv.reader(f)
    games_list = list(reader)
    games = []
    for game in games_list:
        if game[0] == 'Home':
            continue
        if game[6] and game[7]:
            games.append(Game(game[0], game[1], game[2], game[3], game[4], game[5], game[6], game[7]))
        else:
            games.append(Game(game[0], game[1], game[2], game[3], game[4], game[5]))

# Load the templates
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# Loop over each file and create
template_files = ["index.html", "draw.html", "table.html", "betting.html", "groups.html", "knockout.html"]

for template_file in template_files:
    template = templateEnv.get_template(template_file)
    if template_file == 'draw.html':
        template_render = template.render({"team_assignation" : team_assignation})
    elif template_file == 'groups.html':
        template_render = template.render({"games" : games})
    else:
        template_render = template.render()

    # Save as a html file
    with open(template_file, 'w') as f:
        f.write(template_render)