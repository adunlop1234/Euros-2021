import os
import random

# 
random.seed(2021)

with open(os.path.join("data", "people.csv"), "r") as f:
    people = list(f.read().splitlines())

with open(os.path.join("data", "teams.csv"), "r") as f:
    teams = list(f.read().splitlines())

with open(os.path.join("data", "draw.csv"), "w") as f:
    while len(teams) > 0:
        team = teams.pop(random.randint(0, len(teams)-1))
        person = people.pop(random.randint(0, len(people)-1))
        f.write(team + "," + person + "\n")