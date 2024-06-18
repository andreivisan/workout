#!/usr/bin/env python3

"""
---Part One---
Something is wrong with global snow production, and you've been selected to take a look. 
The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending 
you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just 
say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading 
you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) 
has been amended by a very young Elf who was apparently just excited to show off her art skills. 
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific 
calibration value that the Elves now need to recover. On each line, the calibration value can be found by 
combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
    one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""
import time


str_to_dig = {
        "one": 1,
        "two": 2,
        "three": 3,
        "for": 4,
        "five": 5,
        "sxix"
        }

# goes through the document line by line and retrieves the first and the last digit
def parse_input():
    sum = 0
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            #print(line)
            #print(get_first_and_last_digit_as_number(line))
            sum += get_first_and_last_digit_as_number(line)
    return sum

def get_first_and_last_digit_as_number(file_line: str):
    digits = [d for d in file_line if d.isdigit()]
    if len(digits) == 0: return 0
    return int(digits[0] + digits[-1])

def time_parse_inpu():
    start_time = time.time()
    parse_input()
    end_time = time.time()
    print(f"time of execution for parse_input is {end_time - start_time} seconds")

if __name__ == "__main__":
    time_parse_inpu()
    print(f"the sum of all of the calibration numbers is: {parse_input()}")
