import re


def read_int(filename: str) -> list:
    with open(filename) as file:
        lines = [int(line.strip()) for line in file]
    return lines


def read_re(filename: str, pattern) -> list:
    with open(filename) as file:
        lines = [re.search(pattern, line.strip()).groups() for line in file]
    return lines


def read_str(filename: str) -> list:
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines
