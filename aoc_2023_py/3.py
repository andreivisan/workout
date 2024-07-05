#!/usr/bin/env python3
'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; 
it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in 
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, 
but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to 
a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''
import re

input_matrix = []
number_pattern = re.compile(r'\d+')
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def part_1():
    input_matrix = build_matrix()
    numbers = []
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[0])):
            if input_matrix[row][col] != 0 and input_matrix[row][col] != 1:
                if is_adjacent(input_matrix, row, col):
                    numbers.append(input_matrix[row][col])
    print(sum(numbers))

def build_matrix(): 
    with open('3.txt', encoding='utf-8') as input_file:
        for index_ln, line in enumerate(input_file):
            line_len = len(line)
            i = 0
            cols = [] 
            while i < line_len:    
                ch = line[i]
                if ch == '.':
                    cols.append(0)
                    i += 1
                elif not ch.isdigit():
                    cols.append(1)
                    i += 1
                elif ch.isdigit():
                    match = number_pattern.match(line, i)
                    if match:
                        cols.append(int(match.group()))
                        i += len(match.group())
            input_matrix.append(cols)
    return input_matrix

def is_adjacent(input_matrix, cur_row, cur_col):
    len_rows = len(input_matrix)
    len_cols = len(input_matrix[0])
    for dr, dc in directions:
        row = cur_row + dr
        col = cur_col + dc
        if 0 <= row < len_rows and 0 <= col < len_cols:
            if input_matrix[dr][dc] == 1:
                return True
    return False


if __name__ == "__main__":
    part_1()
