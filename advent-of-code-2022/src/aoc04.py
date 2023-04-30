import re
import pathlib


def aoc_04():
    overlaps = 0
    file_path = pathlib.Path("../data/04-assignments.txt")

    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            start1, end1, start2, end2 = list(map(int, re.split(r'[,|-]', line)))
            if start1 <= start2 and end1 >= end2 or start1 >= start2 and end1 <= end2:
                overlaps += 1

    print(f"There are a total of {overlaps} overlaps.")


if __name__ == '__main__':
    aoc_04()
