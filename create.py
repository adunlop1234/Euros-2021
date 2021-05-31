import jinja2
import os, sys
import csv

# Read in the team - assignation
with open(os.path.join('data', 'draw.csv'), 'r', newline='') as f:
    reader = csv.reader(f)
    team_assignation = list(reader)

# Order team assignation in alphabetical order of name


# Load the templates
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# Loop over each file and create
template_files = ["index.html", "draw.html", "table.html", "betting.html"]

for template_file in template_files:
    template = templateEnv.get_template(template_file)
    if template_file == 'draw.html':
        template_render = template.render({"team_assignation" : team_assignation})
    else:
        template_render = template.render()

    # Save as a html file
    with open(template_file, 'w') as f:
        f.write(template_render)