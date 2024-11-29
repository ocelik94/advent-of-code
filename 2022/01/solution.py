"""Solution to Day 01 of Advent of Code 2022"""

import timeit
from pathlib import Path
from typing import List

# Define the path to the input data
DATA_PATH = Path(__file__).parent.resolve()

# Read the input data
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.read()


def parse_data_to_summation(data: str, delimiter: str = "") -> List[int]:
    """
    Parses the input data and computes summations split by a delimiter.

    Parameters
    ----------
    data : str
        The input data as a string.
    delimiter : str, optional
        The delimiter used to split the summations (default is an empty string).

    Returns
    -------
    List[int]
        A list of integer summations for each elf.
    """
    summation = []
    current_sum = 0

    for line in data.split("\n"):
        if line != delimiter:
            current_sum += int(line)
        else:
            summation.append(current_sum)
            current_sum = 0

    if current_sum > 0:  # Add the last group if not already added
        summation.append(current_sum)

    return summation


# Part 1: Find the maximum summation
part_1_start_time = timeit.default_timer()
part_1_result = max(parse_data_to_summation(DATA))
part_1_duration_ms = (timeit.default_timer() - part_1_start_time) * 1000

# Part 2: Find the sum of the top 3 summations
part_2_start_time = timeit.default_timer()
top_3_sums = sum(sorted(parse_data_to_summation(DATA), reverse=True)[:3])
part_2_duration_ms = (timeit.default_timer() - part_2_start_time) * 1000

# Output results
if __name__ == "__main__":
    print(f"Part 1:\nMost calories carried by a single elf: {part_1_result} cal\n")
    print(f"Part 2:\nTotal calories carried by the top 3 elves: {top_3_sums} cal\n")
    print("Timed Results:")
    print(f"Part 1 Duration: {part_1_duration_ms:.3f} ms")
    print(f"Part 2 Duration: {part_2_duration_ms:.3f} ms")
