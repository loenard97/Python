import pathlib


def aoc_06_a():
    file_path = pathlib.Path("../data/06-stream.txt")

    with open(file_path, "r") as file:
        idx_4 = -1
        idx_14 = -1
        for line in file:
            line = line.rstrip("\n")

            for i in range(len(line)):
                if len(set(line[i : i + 4])) == 4:
                    idx_4 = i + 4
                    break

            for i in range(len(line)):
                if len(set(line[i : i + 14])) == 14:
                    idx_14 = i + 14
                    break

            print(f"The package index is {idx_4}.")  # 1760
            print(f"The message index is {idx_14}.")  # 2974


def aoc_06_b():
    file_path = pathlib.Path("../data/06-stream.txt")

    with open(file_path, "r") as file:
        line = file.readline().rstrip("\n")

        def get_index(window_size):
            return (
                list(
                    map(
                        lambda x: len(set(x)),
                        [line[i : i + window_size] for i in range(len(line))],
                    )
                ).index(window_size)
                + window_size
            )

        print(f"The package index is {get_index(4)}.")  # 1760
        print(f"The message index is {get_index(14)}.")  # 2974


if __name__ == "__main__":
    aoc_06_b()
