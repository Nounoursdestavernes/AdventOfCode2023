# Description: Day 13 Part 2 of Advent of Code

def verif_sym(lines: list[str]) -> bool:
    """ Verifies if the lines are symetric """
    repaire = False
    for i in range(len(lines) // 2):
        diff = number_of_differences(lines[i], lines[-i - 1]) # we count the number of differences between the two lines
        if diff > 1: # if there is more than one difference, we return False
            return False
        elif diff == 1 and not repaire: # if there is one difference and we haven't repaired yet, we continue
            repaire = True
            continue
        elif diff == 1 and repaire: # if there is one difference and we have already repaired, we return False
            return False
        
    return repaire

def number_of_differences(line1, line2) -> int:
    """ Return the number of differences between the two lines """
    return sum([1 if line1[i] != line2[i] else 0 for i in range(len(line1))])


def solution(textfile: str) -> int:
    """ Returns the total of the sum of the symetric parts """
    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    parts = []
    tmp = []
    for line in lines: 
        if len(line) == 1:
            parts.append(tmp)
            tmp = []
        else:
            tmp.append(line.rstrip())

    parts.append(tmp)

    total = 0
    repaired_parts = []

    for i, part in enumerate(parts):
        part_len = len(part)
        for j in range(part_len-1, 0, -1): # we start from the end
            if (j-1) % 2 == 0 and verif_sym(part[:j+1]): 
                total += 100 * (int(j // 2 + 0.5) + 1)
                repaired_parts.append(i) # we add the part to the repaired parts
                break

        if i not in repaired_parts:
            for j in range(part_len-1): # we start from the beginning
                if (part_len - j) % 2 == 0 and verif_sym(part[j:]):
                    total += 100 * int((part_len + j) // 2 + 0.5)
                    repaired_parts.append(i)
                    break             
    
    translate_parts = []
    for part in parts:
        translate_parts.append([''.join([part[j][i] for j in range(len(part))]) for i in range(len(part[0]))])        

    for i, part in enumerate(translate_parts):
        part_len = len(part)
        if i in repaired_parts: # if the part is already repaired, we continue
                continue
        for j in range(part_len-1, 0, -1):
            if (j-1) % 2 == 0 and verif_sym(part[:j+1]):
                total += int(j // 2 + 0.5) + 1
                repaired_parts.append(i)
                break
        
        if i not in repaired_parts:
            for j in range(part_len-1):
                if (part_len - j) % 2 == 0 and verif_sym(part[j:]):
                    total += int((part_len + j) // 2 + 0.5)
                    repaired_parts.append(i)
                    break



    return total