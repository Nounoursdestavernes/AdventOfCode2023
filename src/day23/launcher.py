import sys
import time
import timeit
import platform
from Part1.part1 import part1
from Part2.part2 import part2

ALLOWED_OPTIONS = ['-h', '-p1', '-p2', '-t', '-b', '-a']

def help():
    print("Usage: python3 launcher.py [Options] <filename>")
    print("Options:")
    print("    -h: print this help message")
    print("    -p1: Run only Part 1")
    print("    -p2: Run only Part 2")
    print("    -t: print the time to run")
    print("    -b: benchmark the code")
    print("    -a: assert that the script works, use this option with input.txt")
    sys.exit(1)

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        help()
        sys.exit(0)
    
    for arg in args[:-1]:
        if arg not in ALLOWED_OPTIONS:
            print("Error: Invalid options", arg)
            help()
            sys.exit(1)

    if '-h' in args:
        help()
        sys.exit(0)

    if '-p1' in args and '-p2' in args:
        print("Error: To run both Part 1 and Part 2 use no options")
        sys.exit(1)

    filename = args[-1]
    with open(filename, 'r', encoding='utf-8') as f:
        if '-b' in args:
            start_read = time.perf_counter()
        lines = f.readlines()
        if '-b' in args:
            duration_read = time.perf_counter() - start_read

    if '-a' in args:
        print("Asserting...")
        print("Part 1:", part1(lines) == 2214)
        print("Part 2:", part2(lines) == 6594)
        sys.exit(0)

    if '-b' in args:
        print("System:", platform.system())
        print("Processor:", platform.processor())
        print("Python version:", platform.python_version())
        print("Day: 23\n")

        time_p1 = timeit.timeit(lambda: part1(lines), number=100)
        print("Time part 1 (mean time over 100 runs):", time_p1 / 100 + duration_read)
        time_p2 = timeit.timeit(lambda: part2(lines), number=100)
        print("Time part 2 (mean time over 100 runs):", time_p2 / 100 + duration_read)
        sys.exit(0)

    if '-p1' in args:
        if '-t' in args:
            start = time.perf_counter()
        print("Part 1:", part1(lines))
        if '-t' in args:
            print("Time part 1:", time.perf_counter() - start)
        sys.exit(0)

    if '-p2' in args:
        if '-t' in args:
            start = time.perf_counter()
        print("Part 2:", part2(lines))
        if '-t' in args:
            print("Time part 2:", time.perf_counter() - start)
        sys.exit(0)
    
    if '-t' in args:
        start = time.perf_counter()
    print("Part 1:", part1(lines))
    if '-t' in args:
        print("Time part 1:", time.perf_counter() - start)
    if '-t' in args:
        start = time.perf_counter()
    print("Part 2:", part2(lines))
    if '-t' in args:
        print("Time part 2:", time.perf_counter() - start)
    sys.exit(0)
    

if __name__ == '__main__':
    main()