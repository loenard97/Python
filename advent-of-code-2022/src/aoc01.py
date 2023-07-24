import pathlib

from src.lib.file__line_generator import FileLines


def aoc_01():
    file_path = pathlib.Path("../data/01-calories.txt")
    calories = [0]

    with open(file_path, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                calories[-1] += int(line)
            else:
                calories.append(0)

    max_value = max(calories)
    max_index = calories.index(max_value)

    # print("List of all calories:", calories)
    print(
        f"The most calories has elf {max_index + 1} with {max_value} calories."
    )  # 67658

    calories.sort(reverse=True)
    top_three_total = sum(calories[:3])
    print(f"The top three elves have a total of {top_three_total} calories.")  # 200158


if __name__ == "__main__":
    aoc_01_b()
