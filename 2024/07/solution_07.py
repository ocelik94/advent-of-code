"""Solution to Day 07 of Advent of Code 2024"""

from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    results = []
    operands = []
    for row in input_file:
        if not row.strip():
            continue
        sections = row.split(":")
        results.append(int(sections[0].strip()))
        operands.append(sections[1].strip().split(" "))


def evaluate_left_to_right(expression):
    expression = expression.split(" ")
    result = int(expression[0])

    for i in range(1, len(expression), 2):
        operator = expression[i]
        next_val = int(expression[i + 1])
        if operator == "+":
            result += next_val
        elif operator == "*":
            result *= next_val
        elif operator == "||":
            result = int(str(result) + str(next_val))

    return result


def generate_combos_recursive(operators, ops, idx, current):
    if idx == len(ops) - 1:
        yield current
    else:
        for op in operators:
            yield from generate_combos_recursive(operators, ops, idx + 1, current + f" {op} {ops[idx + 1]}")


def can_be_made_true(data, operands, operators):
    verified = {}

    for target, operand_list in zip(data, operands):
        for combo in generate_combos_recursive(operators, operand_list, 0, operand_list[0]):
            try:
                if evaluate_left_to_right(combo) == target and "".join(operand_list) not in verified:
                    verified["".join(operand_list)] = target
            except ValueError:
                continue

    return sum(verified.values())


if __name__ == "__main__":
    print("Part 1 of the puzzle:", can_be_made_true(results, operands, ["+", "*"]))
    print("Part 2 of the puzzle:", can_be_made_true(results, operands, ["+", "*", "||"]))
