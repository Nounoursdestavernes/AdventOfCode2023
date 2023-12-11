# Description: Day 10 Part 1 of Advent of Code 2023

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
        

def part1(lines : list[str]) -> int:
    """ Returns the number of steps to get from the starting position to the point farthest from the starting point"""

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

    return len(visited) // 2