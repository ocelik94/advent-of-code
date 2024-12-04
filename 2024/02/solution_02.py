"""Solution to Day 02 of Advent of Code 2024"""

from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    rows = [list(map(int, line.split())) for line in input_file]


def check_either_increasing_or_decreasing(row_input):
    increasing = all(row_input[r] <= row_input[r + 1] for r in range(len(row_input) - 1))
    decreasing = all(row_input[r] >= row_input[r + 1] for r in range(len(row_input) - 1))
    return increasing or decreasing


def has_valid_differences(row_input):
    return all(1 <= abs(row_input[r] - row_input[r + 1]) <= 3 for r in range(len(row_input) - 1))


def is_valid_after_removal(row_input):
    for r in range(len(row_input)):
        modified_row = row_input[:r] + row_input[r + 1 :]
        if check_either_increasing_or_decreasing(modified_row) and has_valid_differences(modified_row):
            return True
    return False


if __name__ == "__main__":
    number_of_safe_reports = 0
    for i, row in enumerate(rows, start=1):
        is_ordered = check_either_increasing_or_decreasing(row)
        has_valid_diffs = has_valid_differences(row)
        if is_ordered and has_valid_diffs:
            number_of_safe_reports += 1
    print("Part 1 of the puzzle: " + str(number_of_safe_reports))

    number_of_safe_reports = 0
    for i, row in enumerate(rows, start=1):
        if check_either_increasing_or_decreasing(row) and has_valid_differences(row):
            number_of_safe_reports += 1
        elif is_valid_after_removal(row):
            number_of_safe_reports += 1
    print("Part 2 of the puzzle: " + str(number_of_safe_reports))
