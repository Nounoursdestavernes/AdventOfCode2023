# Description: Day 12 Part 2 of Advent of Code 2023
from functools import cache

### Special thanks to u/yawnick on Reddit for the idea of part 2. Particulary, the number_of_combinaisons function ###

@cache
def number_of_combinaisons(record:str, duplicate:tuple[int]) -> int:    
    """Return the number of valid combinations of the record with the duplicate """
    if duplicate == ():
        if '#' in record: # We have already found all the groups of #, so we can stop the search
            return 0
        else: # We found a valid combination
            return 1
    
    record_len = len(record)
    duplicate_len = len(duplicate)

    next_group = duplicate[0] # The length of the next group of #
    res = 0 # The number of valid combinations

    # We can skip the next_group first characters of the record because they are all #
    record_len -= next_group
    
    # We can skip the duplicate_len-1 next characters of the record because they are all ?
    record_len -= duplicate_len-1

    # We can skip the sum(duplicate[1:]) next characters of the record because they are all #
    record_len -= sum(duplicate[1:])

    for i in range(record_len):
        if record[i+next_group] == '#': # If the next character is a #, it is not a valid combination because it is not a group of #
            continue
        if '#' in record[:i]: # If there is a # before the next group of #, it is not a valid combination
            break
        if '.' not in record[i:i+next_group]: # If there is no . in the next group of #, it is a valid combination
            res += number_of_combinaisons(record[i+next_group+1:], duplicate[1:])  # We continue the search in the rest of the record and the rest of the duplicate
    return res # We return the number of valid combinations


def part2(lines: list[str]) -> int:
    """ Return the number of valid combinations """

    possibilities = 0
    
    for line in lines:
        res = line.rstrip().split(' ')
        record, duplicate = res
        duplicate = [int(x) for x in duplicate.split(',')]

        record_add = record
        duplicate_add = duplicate.copy()
        for _ in range(4):
            record += '?' + record_add
            duplicate.extend(duplicate_add)

        record += '.' # To know when we reach the end of the line

        possibilities += number_of_combinaisons(record, tuple(duplicate))
    
    return possibilities

        