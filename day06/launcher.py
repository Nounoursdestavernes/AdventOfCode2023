import sys
import time
import platform
from Part1.part1 import part1
from Part2.part2 import part2


def help():
    print("Usage: python3 launcher.py [Options] <filename>")
    print("Options:")
    print("    -h: print this help message")
    print("    -p1: Run only Part 1")
    print("    -p2: Run only Part 2")
    print("    -t: print the time took to run each part")
    print("    -b: benchmark the code")
    sys.exit(1)

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        help()

    if '-h' in args:
        help()

    if '-p1' in args and '-p2' in args:
        print("Error: To run both Part 1 and Part 2 use no options")
        sys.exit(1)

    filename = args[-1]
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if '-b' in args:
        print("Benchmarking...")
        print("System:", platform.system())
        print("Processor:", platform.processor())
        print("Python version:", platform.python_version())
        
        print("Day: 06\n")
        print("Part 1:")
        start = time.time()
        part1(lines)
        time_p1 = time.time() - start
        print("Time took to run Part 1 :", time_p1)
        print("Part 2:")
        start = time.time()
        part2(lines)
        time_p2 = time.time() - start
        print("Time took to run Part 2 :", time_p2)
        print("Total time took to run both parts:", time_p1 + time_p2)

        sys.exit(0)

    if '-p1' in args:
        if '-t' in args:
            start = time.time()
        print("Part 1:", part1(lines))
        if '-t' in args:
            print("Time took to run Part 1:", time.time() - start)
        sys.exit(0)
    if '-p2' in args:
        if '-t' in args:
            start = time.time()
        print("Part 2:", part2(lines))
        if '-t' in args:
            print("Time took to run Part 2:", time.time() - start)
        sys.exit(0)
    
    if '-t' in args:
        start = time.time()
    print("Part 1:", part1(lines))
    if '-t' in args:
        print("Time took to run Part 1:", time.time() - start)
    if '-t' in args:
        start = time.time()
    print("Part 2:", part2(lines))
    if '-t' in args:
        print("Time took to run Part 2:", time.time() - start)
    sys.exit(0)
    

if __name__ == '__main__':
    main()