import configparser
from jinja2 import Environment, FileSystemLoader

# Load the config file
config = configparser.ConfigParser()
config.read("config/config.ini")

# Define the Jinja2 Environment
env = Environment(
    loader=FileSystemLoader("templates"),
)

def create_launcher(day_number: str, res_part1: str = "0", res_part2: str = "0") -> None:
    """ Creates a launcher.py file for the given day """
    # Load the template
    template = env.get_template("launcher.jinja2")
    # Create the launcher.py file
    with open(f"src/day{day_number}/launcher.py", "w") as f:
        f.write(template.render(day_number=day_number, res_part1=res_part1, res_part2=res_part2))

if __name__ == "__main__":
    for day in config.sections():
        res_part1 = config[day]["res_part1"]
        res_part2 = config[day]["res_part2"]

        create_launcher(day, res_part1, res_part2)