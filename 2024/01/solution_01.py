"""Solution to Day 01 of Advent of Code 2024"""

from collections import Counter
from pathlib import Path

with open(
    Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8"
) as input_file:
    data = [list(map(int, line.split())) for line in input_file]
    columns = list(zip(*data))
    sorted_columns = [sorted(list(col)) for col in columns]

if __name__ == "__main__":
    differences = [abs(c1 - c2) for c1, c2 in zip(sorted_columns[0], sorted_columns[1])]
    total_difference = sum(differences)
    print("Part 1 of the puzzle: " + str(total_difference))

    right_counts = Counter(sorted_columns[1])
    similarity_score = sum(num * right_counts[num] for num in sorted_columns[0])
    print("Part 2 of the puzzle: " + str(similarity_score))
