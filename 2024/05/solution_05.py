"""Solution to Day 05 of Advent of Code 2024"""

from pathlib import Path

with open(Path(__file__).parent.resolve() / "input.txt", encoding="UTF-8") as input_file:
    content = input_file.read()

ordering_rules_raw, page_numbers_raw = content.strip().split("\n\n")

list_of_rules = [list(map(int, line.strip().split("|"))) for line in ordering_rules_raw.split("\n")]
list_of_pages = [list(map(int, line.strip().split(","))) for line in page_numbers_raw.split("\n")]


def check_rule(list_of_pages, rule):
    if set(rule) <= set(list_of_pages):
        left, right = rule
        if list_of_pages.index(left) > list_of_pages.index(right):
            return False
    return True


def check_all_rules(list_of_pages):
    if all((check_rule(list_of_pages, rule) for rule in list_of_rules)):
        return list_of_pages[len(list_of_pages) // 2]
    return 0


def check_and_reorder(list_of_pages, rule):
    if set(rule) <= set(list_of_pages):
        left, right = rule
        post_left, post_right = list_of_pages.index(left), list_of_pages.index(right)
        if post_left > post_right:
            list_of_pages[post_left], list_of_pages[post_right] = right, left
    return list_of_pages


def check_and_correct(list_of_pages, initial=True):
    if initial and check_all_rules(list_of_pages):
        return 0

    for rule in list_of_rules:
        list_of_pages = check_and_reorder(list_of_pages, rule)

    if check_all_rules(list_of_pages):
        return list_of_pages[len(list_of_pages) // 2]

    return check_and_correct(list_of_pages, False)


if __name__ == "__main__":
    print("Part 1 of the puzzle:", sum(map(check_all_rules, list_of_pages)))
    print("Part 2 of the puzzle:", sum(map(check_and_correct, list_of_pages)))
