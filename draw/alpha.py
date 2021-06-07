import os, sys
import csv

with open(os.path.join("data", "people.csv"), "r") as f:
    reader = csv.reader(f)
    data = list(reader)

sorted_data = sorted(data)

with open(os.path.join("data", "people.csv"), "w") as f:
    for person in sorted_data:
        f.write(str(person[0]) + "\n")

with open(os.path.join("data", "teams.csv"), "r") as f:
    reader = csv.reader(f)
    data = list(reader)

sorted_data = sorted(data)

with open(os.path.join("data", "teams.csv"), "w") as f:
    for person in sorted_data:
        f.write(str(person[0]) + "\n")