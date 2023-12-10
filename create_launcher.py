from jinja2 import Environment, FileSystemLoader
import configparser

# Load the config file
config = configparser.ConfigParser()
config.read("config.ini")

# Define the Jinja2 Environment
env = Environment(
    loader=FileSystemLoader("template"),
)

def create_launcher(day_number: str, res_part1: str, res_part2: str) -> None:
    """ Creates a launcher.py file for the given day """
    # Load the template
    template = env.get_template("template_launcher.jinja2")
    # Create the launcher.py file
    with open(f"day{day}/launcher.py", "w") as f:
        f.write(template.render(day_number=day_number, res_part1=res_part1, res_part2=res_part2))

if __name__ == "__main__":
    # Create the launcher.py files
    for day in config["Days"]:
        res_part1, res_part2 = config["Days"][day].split(",")
        create_launcher(day, res_part1, res_part2)