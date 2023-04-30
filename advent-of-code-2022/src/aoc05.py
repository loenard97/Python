import pathlib
from collections import deque


class CargoBay:

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    @classmethod
    def from_file(cls, file_path):
        first = deque()
        second = deque()
        third = deque()

        with open(file_path, 'r') as file:
            for line in file.readlines():
                if line == " 1   2   3 \n":
                    break
                if line[1] != ' ':
                    first.appendleft(line[1])
                if line[5] != ' ':
                    second.appendleft(line[5])
                if line[9] != ' ':
                    third.appendleft(line[9])

        return CargoBay(first, second, third)

    def to_str(self):
        return '\n'.join([
            f"{f'[{self.first[row]}]' if row < len(self.first) else '   '} "
            f"{f'[{self.second[row]}]' if row < len(self.second) else '   '} "
            f"{f'[{self.third[row]}]' if row < len(self.third) else '   '}"
            for row in reversed(range(max(len(self.first), len(self.second), len(self.third))))]) \
            + "\n 1   2   3 "

    def apply_move(self, move):
        for _ in range(move.move_number):
            elem = ''
            if move.move_from == 1:
                elem = self.first.pop()
            elif move.move_from == 2:
                elem = self.second.pop()
            elif move.move_from == 3:
                elem = self.third.pop()

            if move.move_to == 1:
                self.first.append(elem)
            elif move.move_to == 2:
                self.second.append(elem)
            elif move.move_to == 3:
                self.third.append(elem)


class CargoMove:

    def __init__(self, move_from, move_to, move_number):
        self.move_from = move_from
        self.move_to = move_to
        self.move_number = move_number

    @classmethod
    def from_file(cls, file_path):
        move_ops = []

        with open(file_path, 'r') as file:
            for line in file.readlines():
                if line.startswith("move"):
                    splits = line.strip().split(' ')
                    move_ops.append(CargoMove(int(splits[3]), int(splits[5]), int(splits[1])))

        return move_ops

    def to_str(self):
        return f"move {self.move_number} from {self.move_from} to {self.move_to}"


def aoc_05():
    file_path = pathlib.Path("../data/05-cargo.txt")
    bay = CargoBay.from_file(file_path)
    move_ops = CargoMove.from_file(file_path)

    for move in move_ops:
        bay.apply_move(move)

    print(f"Final cargo bay state:\n{bay.to_str()}\n")
    print(f"Crates on top: {bay.first[-1]}, {bay.second[-1]}, {bay.third[-1]}")


if __name__ == '__main__':
    aoc_05()
