DIAL_START = 50
DIAL_SIZE = 100


def solve():
    with open("input.txt") as f:
        lines = f.readlines()

    zero_count = 0
    dial_pos = DIAL_START

    # Naive solution, terrible time complexity,
    # but runs fine for the input size.
    for line in lines:
        dir = line[0]
        num = int(line[1:])

        for _ in range(num):
            if dir == "R":
                dial_pos += 1
            else:
                dial_pos -= 1

            dial_pos %= DIAL_SIZE

            if dial_pos == 0:
                zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    solve()
