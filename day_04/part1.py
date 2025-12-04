ROLL_CHAR = "@"
OFFSET_COORDS = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
MOVEABLE_THRESHOLD = 4


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

    moveable_rolls = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if not grid[y][x]:
                continue

            surrounding = sum(
                grid[y + y_offset][x + x_offset] for y_offset, x_offset in OFFSET_COORDS
            )
            if surrounding < MOVEABLE_THRESHOLD:
                moveable_rolls += 1

    print(moveable_rolls)


if __name__ == "__main__":
    solve()
