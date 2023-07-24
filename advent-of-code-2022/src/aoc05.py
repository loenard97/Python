from dataclasses import dataclass
import pathlib
from collections import deque


@dataclass
class CargoBay:
    bay: list[deque]

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.rstrip()
                if line.startswith(" 1"):
                    n_bay = len(line.split())
                    break

        bay_list = []
        for _ in range(n_bay):
            bay_list.append(deque())
        cargo_bay = CargoBay(bay_list)

        with open(file_path, "r") as file:
            for line in file.readlines():
                line = line.rstrip("\n")
                if line.startswith(" 1"):
                    break

                for n in range(n_bay):
                    idx = 4 * n + 1
                    if line[idx] != " ":
                        cargo_bay.bay[n].appendleft(line[idx])

        return cargo_bay

    def __str__(self):
        return (
            "\n".join(
                [
                    "".join(
                        [
                            f"{f'[{self.bay[n][row]}]' if row < len(self.bay[n]) else '   '} "
                            for n in range(len(self.bay))
                        ]
                    )
                    for row in reversed(range(max(list(map(len, self.bay)))))
                ]
            )
            + "\n "
            + "   ".join([str(i + 1) for i in range(len(self.bay))])
        )

    @property
    def top_crates(self):
        return "".join([bay[-1] for bay in self.bay])

    def apply_move(self, move):
        for _ in range(move.move_number):
            crate = self.bay[move.move_from - 1].pop()
            self.bay[move.move_to - 1].append(crate)

    def apply_multiple_move(self, move):
        crates = []
        for _ in range(move.move_number):
            crates.append(self.bay[move.move_from - 1].pop())

        for crate in reversed(crates):
            self.bay[move.move_to - 1].append(crate)


@dataclass
class CargoMove:
    move_from: int
    move_to: int
    move_number: int

    @classmethod
    def from_file(cls, file_path):
        move_ops = []

        with open(file_path, "r") as file:
            for line in file.readlines():
                if line.startswith("move"):
                    splits = line.strip().split(" ")
                    move_ops.append(
                        CargoMove(int(splits[3]), int(splits[5]), int(splits[1]))
                    )

        return move_ops

    def __str__(self):
        return f"move {self.move_number} from {self.move_from} to {self.move_to}"


def aoc_05():
    file_path = pathlib.Path("../data/05-cargo.txt")
    bay = CargoBay.from_file(file_path)
    print(f"Initial cargo bay state:\n{bay}\n")

    move_ops = CargoMove.from_file(file_path)
    for move in move_ops:
        bay.apply_multiple_move(move)

    print(f"Final cargo bay state:\n{bay}\n")
    print(f"Crates on top: {bay.top_crates}")


if __name__ == "__main__":
    aoc_05()
