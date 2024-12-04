"""Solution to Day 04 of Advent of Code 2024"""

from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    grid = [list(line.strip()) for line in input_file.readlines()]


def search_for_xmas_in_grid(input_grid):
    word = "XMAS"
    count = 0

    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            # Right
            if col + len(word) <= len(input_grid[0]) and all(
                input_grid[row][col + w] == word[w] for w in range(len(word))
            ):
                count += 1

            # Down
            if row + len(word) <= len(input_grid) and all(
                input_grid[row + w][col] == word[w] for w in range(len(word))
            ):
                count += 1

            # Down/Right
            if (
                row + len(word) <= len(input_grid)
                and col + len(word) <= len(input_grid[0])
                and all(input_grid[row + w][col + w] == word[w] for w in range(len(word)))
            ):
                count += 1

            # Down/Left
            if (
                row + len(word) <= len(input_grid)
                and col - len(word) >= -1
                and all(input_grid[row + w][col - w] == word[w] for w in range(len(word)))
            ):
                count += 1

            # Left
            if col - len(word) >= -1 and all(input_grid[row][col - w] == word[w] for w in range(len(word))):
                count += 1

            # Up
            if row - len(word) >= -1 and all(input_grid[row - w][col] == word[w] for w in range(len(word))):
                count += 1

            # Up/Left
            if (
                row - len(word) >= -1
                and col - len(word) >= -1
                and all(input_grid[row - w][col - w] == word[w] for w in range(len(word)))
            ):
                count += 1

            # Up/Right
            if (
                row - len(word) >= -1
                and col + len(word) <= len(input_grid[0])
                and all(input_grid[row - w][col + w] == word[w] for w in range(len(word)))
            ):
                count += 1

    return count


def search_for_xmas_in_grid_x_shaped(input_grid):
    count = 0

    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            try:
                # M.S
                # .A.
                # M.S
                if (
                    input_grid[row][col] == "M"
                    and input_grid[row][col + 2] == "S"
                    and input_grid[row + 1][col + 1] == "A"
                    and input_grid[row + 2][col] == "M"
                    and input_grid[row + 2][col + 2] == "S"
                ):
                    count += 1

                # M.M
                # .A.
                # S.S
                if (
                    input_grid[row][col] == "M"
                    and input_grid[row][col + 2] == "M"
                    and input_grid[row + 1][col + 1] == "A"
                    and input_grid[row + 2][col] == "S"
                    and input_grid[row + 2][col + 2] == "S"
                ):
                    count += 1

                # S.M
                # .A.
                # S.M
                if (
                    input_grid[row][col] == "S"
                    and input_grid[row][col + 2] == "M"
                    and input_grid[row + 1][col + 1] == "A"
                    and input_grid[row + 2][col] == "S"
                    and input_grid[row + 2][col + 2] == "M"
                ):
                    count += 1

                # S.S
                # .A.
                # M.M
                if (
                    input_grid[row][col] == "S"
                    and input_grid[row][col + 2] == "S"
                    and input_grid[row + 1][col + 1] == "A"
                    and input_grid[row + 2][col] == "M"
                    and input_grid[row + 2][col + 2] == "M"
                ):
                    count += 1
            except IndexError:
                continue

    return count


if __name__ == "__main__":
    result = search_for_xmas_in_grid(grid)
    print("Part 1 of the puzzle: " + str(result))

    result = search_for_xmas_in_grid_x_shaped(grid)
    print("Part 2 of the puzzle: " + str(result))
