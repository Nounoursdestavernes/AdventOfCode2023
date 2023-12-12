# Description: Day 12 Part 1 of Advent of Code 2023
import re

def validation(record: str, duplicate: str) -> bool:
    """ Check if the record is valid """
    nb_occ = record.count('#')
    total_occ = sum(duplicate)

    if nb_occ > total_occ:
        return False
    
    indice = record.find('?')
    if total_occ > nb_occ:
        if indice == -1:
            return False
        else:
            s = record[0:indice]
            elements = re.findall('#+', s)
            for i in range(len(elements)-1):
                if len(elements[i]) != duplicate[i]:
                    return False
            return True
    
    record.replace('?', '.')
    breaks = re.findall('#+', record)
    if len(breaks) != len(duplicate):
        return False
    else:
        for i in range(len(duplicate)):
            if len(breaks[i]) != duplicate[i]:
                return False
        return True


def part1(lines: list[str]) -> int:
    """ Return the number of valid combinations """
    possibilities = 0

    for line in lines:

        res = line.rstrip().split(' ')
        record, duplicate = res 
        duplicate = [int(x) for x in duplicate.split(',')]

        stack = [(record, duplicate)]
        while len(stack) != 0:
            current_record, current_duplicate = stack.pop()
            indice = current_record.find('?')
            for possible in ['#', '.']:
                tmp_record = current_record[0:indice] + possible + current_record[indice+1:]
                if validation(tmp_record, current_duplicate):
                    if tmp_record.count('?') == 0:
                        possibilities += 1
                    else:
                        stack.append((tmp_record, current_duplicate))
    return possibilities