# Description: Day 13 Part 1 of Advent of Code


def verif_sym(lines: list[str]) -> bool:
    """ Verifies if the lines are symetric """
    for i in range(len(lines) // 2):
        if lines[i] != lines[-i - 1]:
            return False
    return True


def solution(textfile: str) -> int:
    """ Returns the total of the sum of the symetric parts """

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    parts = []
    tmp = []

    # We split the lines into parts
    for line in lines: 
        if len(line) == 1:
            parts.append(tmp)
            tmp = []
        else:
            tmp.append(line.rstrip())

    parts.append(tmp)
    
    
    total = 0

    for part in parts:
        found = False
        part_len = len(part)
        for j in range(part_len-1, 0, -1): # We start from the end of the part
            if part[0] == part[j]:
                if (j-1) % 2 == 0 and verif_sym(part[:j+1]):
                    total +=  100 * (int(j // 2 + 0.5) + 1)
                    found = True
                    break 
        
        if not found:
            for j in range(part_len-1): # We start from the beginning of the part
                if part[-1] == part[j]:
                   if (part_len - j) % 2 == 0 and verif_sym(part[j:]):
                       total += 100 * int((part_len + j) // 2 + 0.5)
                       break
                   
    translate_parts = []
    for part in parts:
        translate_parts.append([''.join([part[j][i] for j in range(len(part))]) for i in range(len(part[0]))])

    for part in translate_parts:
        found = False
        part_len = len(part)
        for j in range(part_len-1, 0, -1): # We start from the end of the part
            if part[0] == part[j]:
                if (j-1) % 2 == 0 and verif_sym(part[:j+1]):
                    val =  int(j // 2 + 0.5) + 1
                    total += val
                    found = True
                    break
        
        if not found:
            for j in range(part_len-1): # We start from the beginning of the part
                if part[-1] == part[j]:
                   if (part_len - j) % 2 == 0 and verif_sym(part[j:]):
                        val = int((part_len + j) // 2 + 0.5)
                        total += val
                        break
                   
    return total