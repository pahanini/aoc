def read_int(filename: str) -> list:
    with open(filename) as file:
        lines = [int(line.strip()) for line in file]
    return lines
