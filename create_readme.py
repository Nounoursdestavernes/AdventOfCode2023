import configparser
import os
from jinja2 import Environment, FileSystemLoader
from subprocess import check_output

# Load the config file
config = configparser.ConfigParser()
config.read("config/config.ini")

# Define the Jinja2 Environment
env = Environment(
    loader=FileSystemLoader("templates"),
)

def create_readme() -> None:
    """ Creates the README.md file """
    # Load the template
    template = env.get_template("README.jinja2")
    days = []
    for day_number in config.sections():
        name = config[day_number]["name"]
        os.chdir(f"src/day{day_number}")
        out = check_output(["python3", "launcher.py", "-b", "inputs/input.txt"]).decode("utf-8")
        days.append((day_number, name, out))
        os.chdir("../..")
    
    with open("README.md", "w") as f:
        f.write(template.render(days=days))


if __name__ == "__main__":
    print("Creating README.md...")
    create_readme()
    print("README.md created successfully")