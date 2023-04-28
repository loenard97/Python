import pathlib


def aoc_03():
    file_path = pathlib.Path("../data/03-rucksacks.txt")
    priorities = 0

    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            half_length = len(line) // 2

            doubles_char = ''.join(set([c if c in line[half_length:] else '' for c in line[:half_length]]))

            if doubles_char.islower():
                priorities += ord(doubles_char) - 96
            else:
                priorities += ord(doubles_char) - 38

    print(f"The sum of priorities is {priorities}.")


if __name__ == '__main__':
    aoc_03()
