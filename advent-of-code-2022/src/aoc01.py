import pathlib


def aoc_01():
    file_path = pathlib.Path("../data/01-calories.txt")
    calories = [0]

    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                calories[-1] += int(line)
            else:
                calories.append(0)

    max_value = max(calories)
    max_index = calories.index(max_value)

    print("List of all calories:", calories)
    print(f"The most calories has elf {max_index} with {max_value} calories.")


if __name__ == '__main__':
    aoc_01()
