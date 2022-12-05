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


def read_groups(filename: str, strip: bool = True) -> list:
    with open(filename) as file:
        data = file.read()
        if strip:
            data = data.strip()
    return [s.split('\n') for s in data.split('\n\n')]


def read(filename: str) -> str:
    with open(filename) as file:
        data = file.read().strip()
    return data
