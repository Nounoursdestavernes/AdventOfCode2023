import sys
import time
from Part1.day01_Part1 import part1
from Part2.day01_Part2 import part2

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python3 launcher.py [Options] <filename>")
        print("Options:")
        print("    -p1: Run only Part 1")
        print("    -p2: Run only Part 2")
        print("    -t: print the time took to run each part")
        sys.exit(1)

    filename = args[-1]

    if '-p1' in args:
        if '-t' in args:
            start = time.time()
        print("Part 1:", part1(filename))
        if '-t' in args:
            print("Time took to run Part 1:", time.time() - start)
        sys.exit(0)
    if '-p2' in args:
        if '-t' in args:
            start = time.time()
        print("Part 2:", part2(filename))
        if '-t' in args:
            print("Time took to run Part 2:", time.time() - start)
        sys.exit(0)
    
    if '-t' in args:
        start = time.time()
    print("Part 1:", part1(filename))
    if '-t' in args:
        print("Time took to run Part 1:", time.time() - start)
    if '-t' in args:
        start = time.time()
    print("Part 2:", part2(filename))
    if '-t' in args:
        print("Time took to run Part 2:", time.time() - start)
    sys.exit(0)
    

if __name__ == '__main__':
    main()