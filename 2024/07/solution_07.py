"""Solution to Day 07 of Advent of Code 2024"""

import itertools
from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    data = {}
    for line in input_file:
        key, value = line.strip().split(":")
        data[int(key)] = list(map(int, value.strip().split()))


def evaluate_left_to_right(numbers, operations):
    result = numbers[0]
    expression = str(numbers[0])
    for i in range(len(operations)):
        if operations[i] == "+":
            result += numbers[i + 1]
        elif operations[i] == "*":
            result *= numbers[i + 1]
        expression += f" {operations[i]} {numbers[i + 1]}"
    return result, expression


def can_be_made_true(equations):
    operations = ["+", "*"]
    possible_numbers = []

    for target, numbers in equations.items():
        for ops in itertools.product(operations, repeat=len(numbers) - 1):
            try:
                result, expr = evaluate_left_to_right(numbers, ops)
                if result == target:
                    possible_numbers.append(target)
                    break
            except Exception:
                pass

    return sum(possible_numbers), len(possible_numbers)


if __name__ == "__main__":
    print("Part 1 of the puzzle:", can_be_made_true(data))
    # print("Part 2 of the puzzle:", can_be_made_true(data))
