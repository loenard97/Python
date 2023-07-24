import pathlib
from dataclasses import dataclass


@dataclass
class TerminalFile:
    name: str
    size: int

    def __str__(self):
        return f"{self.name} (file, size={self.size})"


@dataclass
class TerminalDirectory:
    name: str
    parent: "None | TerminalDirectory"
    files: list[TerminalFile]
    directories: list["TerminalDirectory"]

    def __str__(self):
        return f"{self.name} (dir)"

    def print_recursively(self, depth):
        space = " " * 4 * depth
        return (
            f"{self}\n"
            + "\n".join([f"{space}{f}" for f in self.files])
            + "\n"
            + "\n".join(
                [f"{space}{d.print_recursively(depth+1)}" for d in self.directories]
            )
        )

    def total_sizes(self, cache):
        size = sum(list(map(lambda x: int(x.size), self.files))) + sum(
            list(map(lambda x: x.total_sizes(cache), self.directories))
        )
        cache[self.name] = size
        return size


@dataclass
class FileSystemBuilder:
    root: TerminalDirectory
    working_directory: TerminalDirectory

    @classmethod
    def from_file(cls, path):
        root = TerminalDirectory("/", None, [], [])
        new_file_system = FileSystemBuilder(root, root)

        with open(path, "r") as file:
            for line in file:
                line = line.rstrip("\n")

                if line.startswith("$ cd"):
                    if line == "$ cd ..":
                        new_file_system.working_directory = (
                            new_file_system.working_directory.parent
                        )
                        continue

                    for directory in new_file_system.working_directory.directories:
                        if directory.name == line[5:]:
                            new_file_system.working_directory = directory

                elif line.startswith("$ ls"):
                    pass

                elif line.startswith("dir"):
                    new_dir = TerminalDirectory(
                        line[4:], new_file_system.working_directory, [], []
                    )
                    new_file_system.working_directory.directories.append(new_dir)

                else:
                    size, name = line.split()
                    new_file = TerminalFile(name, size)
                    new_file_system.working_directory.files.append(new_file)

        return new_file_system

    def __str__(self):
        return self.root.print_recursively(depth=1)

    def dir_sizes(self):
        cache = {}
        self.root.total_sizes(cache)
        return cache


def aoc_07():
    file_path = pathlib.Path("../data/07-terminal.txt")
    file_system = FileSystemBuilder.from_file(file_path)
    # print(file_system)

    sizes = dict(
        filter(lambda item: item[1] < 100_000, file_system.dir_sizes().items())
    )
    sum_total = sum(sizes.values())

    print(f"Files smaller 100_000: {sizes}")
    print(f"Total size of those files: {sum_total}")


if __name__ == "__main__":
    aoc_07()
