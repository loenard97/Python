import re
import pathlib


def aoc_04():
    overlaps_total = 0
    overlaps_small = 0
    file_path = pathlib.Path("../data/04-assignments.txt")

    with open(file_path, "r") as file:
        for line in file.readlines():
            line = line.strip()
            start1, end1, start2, end2 = list(map(int, re.split(r"[,|-]", line)))

            if start1 <= start2 and end1 >= end2 or start1 >= start2 and end1 <= end2:
                overlaps_total += 1

            l1 = [i for i in range(start1, end1 + 1)]
            l2 = [i for i in range(start2, end2 + 1)]

            for i in l1:
                if i in l2:
                    overlaps_small += 1
                    break

    print(f"There are a total of {overlaps_total} overlaps.")  # 513
    print(f"There are a total of {overlaps_small} overlaps.")  # 878


if __name__ == "__main__":
    aoc_04()
