from typing import Literal

type Grid = list[list[Literal[0, 1]]]
type RollSet = set[tuple[int, int]]

ROLL_CHAR = "@"
OFFSET_COORDS = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
MOVEABLE_THRESHOLD = 4


def get_removable_rolls(grid: Grid) -> RollSet:
    removeable_rolls: RollSet = set()
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if not grid[y][x]:
                continue

            surrounding = sum(
                grid[y + y_offset][x + x_offset] for y_offset, x_offset in OFFSET_COORDS
            )
            if surrounding < MOVEABLE_THRESHOLD:
                removeable_rolls.add((x, y))

    return removeable_rolls


def remove_rolls(grid: Grid, rolls_to_remove: RollSet) -> None:
    for x, y in rolls_to_remove:
        grid[y][x] = 0


def solve():
    grid = []

    with open("input.txt") as f:
        for line in f:
            rolls = [0]
            for char in line.strip():
                rolls.append(1 if char == ROLL_CHAR else 0)
            rolls.append(0)
            grid.append(rolls)

        grid.insert(0, [0] * len(grid[0]))
        grid.append([0] * len(grid[0]))

    total = 0

    while True:
        removeable_rolls = get_removable_rolls(grid)
        if not removeable_rolls:
            break

        total += len(removeable_rolls)
        remove_rolls(grid, removeable_rolls)

    print(total)


if __name__ == "__main__":
    solve()
