# Description: Day 10 Part 2 of Advent of Code
import re

def connected_horizontally(pipe1: str, pipe2: str) -> bool:
    """ Returns True if pipe1 and pipe2 are connected horizontally, False otherwise """
    match (pipe1, pipe2):
        case (_, '.'):
            return False
        case ('.', _):
            return False
        case ('|', _):
            return False
        case (_, '|'):
            return False
        case ('-', '-'):
            return True
        case (_, 'L'):
            return False
        case ('J', _):
            return False
        case ('7', _):
            return False
        case (_, 'F'):
            return False
        case ('-', 'J'):
            return True
        case ('-', '7'):
            return True
        case ('L', '-'):
            return True
        case ('F', '-'):
            return True
        case ('L', 'J'):
            return True
        case ('L', '7'):
            return True
        case ('F', 'J'):
            return True
        case ('F', '7'):
            return True
        case ('S', 'J'):
            return True
        case ('S', '7'):
            return True
        case ('S', '-'):
            return True
        case ('-', 'S'):
            return True
        case ('L', 'S'):
            return True
        case ('F', 'S'):
            return True
        
def connected_vertically(pipe1: str, pipe2: str) -> bool:
    """ Returns True if pipe1 and pipe2 are connected vertically, False otherwise """
    match (pipe1, pipe2):
        case (_, '.'):
            return False
        case ('.', _):
            return False
        case ('-', _):
            return False
        case (_, '-'):
            return False
        case ('|', '|'):
            return True
        case (_, 'F'):
            return False
        case (_, '7'):
            return False
        case ('J', _):
            return False
        case ('L', _):
            return False
        case ('|', 'J'):
            return True
        case ('|', 'L'):
            return True
        case ('F', '|'):
            return True
        case ('7', '|'):
            return True
        case ('7', 'J'):
            return True
        case ('7', 'L'):
            return True
        case ('F', 'J'):
            return True
        case ('F', 'L'):
            return True
        case ('S', 'J'):
            return True
        case ('S', 'L'):
            return True
        case ('S', '|'):
            return True
        case ('|', 'S'):
            return True
        case ('F', 'S'):
            return True
        case ('7', 'S'):
            return True
        

def solution(textfile: str) -> int:
    """ Returns the number of . inside the loop"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact
    
    # Finding the starting point
    start = (0, 0)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start = (i, j)
                break
        else:
            continue
        break


    # Searching for a cycle
    visited = set()
    stack = [start]
    beginning = True
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)

        if current in visited and current == start and not beginning: # if we found the cycle
            break
        
        current_pipe = lines[current[0]][current[1]]
        if current[1] > 0:
            pipe_bfr = lines[current[0]][current[1] - 1]
    
        if current[1] < len(lines[current[0]]) - 1:
            pipe_aft = lines[current[0]][current[1] + 1]

        if current[0] > 0:
            pipe_up = lines[current[0] - 1][current[1]]

        if current[0] < len(lines) - 1:
            pipe_down = lines[current[0] + 1][current[1]]

        if current[0] > 0 and connected_vertically(pipe_up, current_pipe) and (current[0] - 1, current[1]) not in visited:
            stack.append((current[0] - 1, current[1])) # add the node to the stack
            
        
        if current[0] < len(lines) - 1 and connected_vertically(current_pipe, pipe_down) and (current[0] + 1, current[1]) not in visited:
            stack.append((current[0] + 1, current[1]))
        
        if current[1] > 0 and connected_horizontally(pipe_bfr, current_pipe) and (current[0], current[1] - 1) not in visited:
            stack.append((current[0], current[1] - 1))
            
        
        if current[1] < len(lines[current[0]]) - 1 and connected_horizontally(current_pipe, pipe_aft) and (current[0], current[1] + 1) not in visited:
            stack.append((current[0], current[1] + 1))
        
        beginning = False


    # Converting S in the right pipe
    top = 0
    bottom = 0
    left = 0
    right = 0

    if start[0] > 0 and connected_vertically(lines[start[0] - 1][start[1]], lines[start[0]][start[1]]):
        top = 1
    if start[0] < len(lines) - 1 and connected_vertically(lines[start[0]][start[1]], lines[start[0] + 1][start[1]]):
        bottom = 1
    if start[1] > 0 and connected_horizontally(lines[start[0]][start[1] - 1], lines[start[0]][start[1]]):
        left = 1
    if start[1] < len(lines[start[0]]) - 1 and connected_horizontally(lines[start[0]][start[1]], lines[start[0]][start[1] + 1]):
        right = 1

    char = 'S'

    match (top, bottom, left, right):
        case (1, 1, 0, 0):
            char = '|'
        case (0, 0, 1, 1):
            char = '-'
        case (1, 0, 0, 1):
            char = 'L'
        case (0, 1, 1, 0):
            char = '7'
        case (1, 0, 1, 0):
            char = 'J'
        case (0, 1, 0, 1):
            char = 'F'

    lines[start[0]] = lines[start[0]][:start[1]] + char + lines[start[0]][start[1] + 1:] # replace the S with the right pipe

    
    counter = 0
    for i, line in enumerate(lines):

        # Removing the pipes that are not in the loop
        line = line.rstrip()
        tmp = ""
        for j, char in enumerate(line):
            if (i, j) in visited:
                tmp += char
            else:
                tmp += '.'
        tmp = re.sub(r"L-*7|F-*J", "|", tmp)

        # Counting the number of . inside the loop
        inside = False
        for char in tmp:
            if char == "|":
                inside = not inside
            
            if char == "." and inside:
                counter += 1
            
    return counter