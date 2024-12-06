"""Solution to Day 06 of Advent of Code 2024"""

from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    grid = {(y, x): char for y, line in enumerate(input_file) for x, char in enumerate(line.strip())}


def move_through_grid(grid, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_index = 0
    current_position = start
    seen = set()

    while current_position in grid and (current_position, directions[current_direction_index]) not in seen:
        seen.add((current_position, directions[current_direction_index]))

        while True:
            next_position = (
                current_position[0] + directions[current_direction_index][0],
                current_position[1] + directions[current_direction_index][1],
            )
            if grid.get(next_position) != "#":
                break
            current_direction_index = (current_direction_index + 1) % len(directions)
        current_position = next_position

    return seen, current_position in grid


def search_the_way(grid):
    start = next((k for k in grid if grid[k] == "^"), None)
    seen, _ = move_through_grid(grid, start)
    return len(set(pos for pos, _ in seen))


def search_for_a_loop(grid):
    start = next((k for k in grid if grid[k] == "^"), None)
    seen, _ = move_through_grid(grid, start)
    positions = {pos for pos, _ in seen}

    total = 0
    for pos in positions:
        _, length = move_through_grid(grid | {pos: "#"}, start)
        total += length

    return total


if __name__ == "__main__":
    print("Part 1 of the puzzle:", search_the_way(grid))
    print("Part 2 of the puzzle:", search_for_a_loop(grid))
