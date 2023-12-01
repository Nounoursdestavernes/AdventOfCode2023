# Description: Day 1 Part 2 of Advent of Code 2023
import string

also_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

lines = []
with open("input.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

sum = 0 # sum of all calibrations

for i, line in enumerate(lines): # for each lines
    first_digit = 0 # first digit in the line
    last_digit = 0 # last digit in the line
    for j, char in enumerate(line): # for each character in the line
        
        if char in string.digits: # if the character is a digit
            if first_digit == 0: # if the first digit is not set
                first_digit = char # set the first digit
            last_digit = char # set the last digit
        
        for k in range(3, 6): # for each possible length of a also_digits
            if line[j:j+k] in also_digits: # if the next k characters are a also_digit
                real_digit = also_digits.index(line[j:j+k]) + 1 # get the real digit
                if first_digit == 0: # if the first digit is not set
                    first_digit = real_digit # set the first digit
                last_digit = real_digit # set the last digit
                j += k # skip the next k characters
                break # break the loop


    sum += 10 * int(first_digit) + int(last_digit) # add the first_digit (*10) and last_digit digit to the sum

print(sum) # print the sum

    


