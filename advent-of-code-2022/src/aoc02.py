import pathlib


def aoc_02():
    file_path = pathlib.Path("../data/02-rock_paper_scissors.txt")
    score_a = 0
    score_b = 0

    scores = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3],
    ]
    replacements = {
        "A X": "A Z",
        "B X": "B X",
        "C X": "C Y",
        "A Y": "A X",
        "B Y": "B Y",
        "C Y": "C Z",
        "A Z": "A Y",
        "B Z": "B Z",
        "C Z": "C X",
    }

    with open(file_path, "r") as file:
        for line in file.readlines():
            line = line.strip()
            replaced_line = replacements[line]

            opponent, me = line.split()
            opponent = ord(opponent) - ord("A")
            me = ord(me) - ord("X")
            score_a += me + 1 + scores[opponent][me]

            opponent, me = replaced_line.split()
            opponent = ord(opponent) - ord("A")
            me = ord(me) - ord("X")
            score_b += me + 1 + scores[opponent][me]

        print(f"Total score in part A is {score_a}.")  # 12794
        print(f"Total score in part B is {score_b}.")  # 14979


if __name__ == "__main__":
    aoc_02()
