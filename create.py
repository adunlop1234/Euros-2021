import jinja2

# Load the templates
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# Loop over each file and create
template_files = ["index.html", "draw.html", "table.html", "betting.html"]
for template_file in template_files:
    template = templateEnv.get_template(template_file)
    template_render = template.render()

    # Save as a html file
    with open(template_file, 'w') as f:
        f.write(template_render)