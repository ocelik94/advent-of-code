"""Solution to Day 03 of Advent of Code 2024"""

import re
from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    text = input_file.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, text)

pattern_with_conditions = r"(mul\(\d*,?\d*\)|do\(\)|don\'t\(\))"
matches_with_conditions = re.findall(pattern_with_conditions, text)

if __name__ == "__main__":
    result = 0
    for match in matches:
        numbers = match[4:-1].split(",")
        n1, n2 = map(int, numbers)
        result += n1 * n2

    print("Part 1 of the puzzle: " + str(result))

    result = 0
    skip = False
    for match in matches_with_conditions:
        if match == "don't()":
            skip = True
        elif match == "do()":
            skip = False

        if skip is False and match != "do()":
            numbers = match[4:-1].split(",")
            n1, n2 = map(int, numbers)
            result += n1 * n2

    print("Part 2 of the puzzle: " + str(result))
