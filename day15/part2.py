# Description: Day 15 Part 2 of Advent of Code


def h(s:str) -> int:
    """ Hash function """
    h_value = 0
    for char in s:
        h_value += ord(char)
        h_value *= 17
        h_value %= 256
    
    return h_value


def solution(textfile: str) -> int:
    """ Returns the focus power of the resulting configuration """


    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    instructions = lines[0].split(',')

    boxes = [ {} for _ in range(256) ]
    
    for instruction in instructions:
        replacement = True
        if instruction[-1] == '-':
            replacement = False
            instruction = instruction[:-1]
        else:
            focal_length = instruction[-1]
            instruction = instruction[:-2]

        box_index = h(instruction)
        if replacement:
            boxes[box_index][instruction] = focal_length
        else:
            boxes[box_index].pop(instruction, None) 

    res = 0
    for i, box in enumerate(boxes):
        if len(box) == 0:
            continue
        tmp_box = list(box)
        for j, el in enumerate(tmp_box):
            res += (i + 1) * (j + 1) * int(box[el])

    return res