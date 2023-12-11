#!/usr/bin/env python3
import os
import sys
from jinja2 import Environment, FileSystemLoader
from create_launchers import create_launcher

# Define the Jinja2 Environment
env = Environment(
    loader=FileSystemLoader("templates"),
)

def help():
    print("Usage: python3 create_day.py <day_number>")
    print("day_number must be between 1 and 25")
    sys.exit(1)


def create_day(day_number: str) -> None:
    """ Creates a launcher.py file for the given day """
    # Load the template
    template = env.get_template("part.jinja2")
    os.chdir("src")

    # Create the day folder
    if os.path.exists(f"day{day_number}"):
        print(f"Day {day_number} already exists")
        sys.exit(1)

    os.mkdir(f"day{day_number}")
    os.chdir(f"day{day_number}")

    # Create the inputs folder
    os.mkdir("inputs")
    
    # Create the part1 folder
    os.mkdir("Part1")

    # Create the part2 folder
    os.mkdir("Part2")

    # Create the part1.py file
    
    with open(os.path.join("Part1", "part1.py"), "w") as f:
        f.write(template.render(day_number=day_number, part_number="1"))

    # Create the part2.py file
    with open(os.path.join("Part2", "part2.py"), "w") as f:
        f.write(template.render(day_number=day_number, part_number="2"))

    # Create the input file
    with open(os.path.join("inputs", "input.txt"), "w") as f:
        pass

    # Create the launcher.py file
    os.chdir(os.path.join("..", ".."))
    create_launcher(day_number)
   

if __name__ == "__main__":
    authorized_args = [i for i in range(1, 26)]
    args = sys.argv[1:]
    if len(args) != 1:
        help()
    elif not args[0].isdigit():
        help()
    elif int(args[0]) not in authorized_args:
        help()
    else:
        day_number = sys.argv[1]
        create_day(day_number)
        print(f"Day {day_number} created")
        sys.exit(0)