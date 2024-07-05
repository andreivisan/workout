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

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going 
so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the 
result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; 
its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
adj_stars = {}

def part_1():
    with open('3.txt', encoding='utf-8') as input_file:
        lines = [line.strip() for line in input_file]
        number = 0
        valid = False
        sum = 0
        for row_index, line in enumerate(lines):
            for col_index, ch in enumerate(line):
                if ch.isdigit():
                    number = number*10 + int(ch)
                    if not valid:
                        valid = is_valid(row_index, col_index, lines)
                else:
                    if valid:
                        sum += number
                    valid = False
                    number = 0
    print(sum)

def part_2():
    number = 0    
    gear_adj = False
    result = 0
    with open('3.txt', encoding='utf-8') as input_file:
        lines = [line.strip() for line in input_file]
        for row_index, line in enumerate(lines):
            for col_index, ch in enumerate(line):
                if ch.isdigit():
                    number = number*10 + int(ch)
                    if not gear_adj:
                        r, c, gear_adj = is_gear_adj(row_index, col_index, lines)
                else:
                    if gear_adj:
                        adj_stars.setdefault((r, c), []).append(number)
                    gear_adj = False
                    number = 0
    for adj_numbers in adj_stars.values():
        if len(adj_numbers) == 2:
            result += adj_numbers[0] * adj_numbers[1]
    print(result)


def is_valid(row, col, lines):
    for dr, dc in directions:
        r = row + dr
        c = col + dc
        if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
            if lines[r][c] != "." and not lines[r][c].isdigit():
                return True
    return False

def is_gear_adj(row, col, lines):
    for dr, dc in directions:
        r = row + dr
        c = col + dc
        if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
            if lines[r][c] == '*':
                return r, c, True
    return r, c, False



if __name__ == "__main__":
    part_2()
