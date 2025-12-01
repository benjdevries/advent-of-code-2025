DIAL_START = 50
DIAL_SIZE = 100


def solve():
    with open("input.txt") as f:
        lines = f.readlines()

    zero_count = 0
    dial_pos = DIAL_START

    for line in lines:
        dir = line[0]
        num = int(line[1:])
        if dir == "R":
            num *= -1

        dial_pos += num
        dial_pos %= DIAL_SIZE

        if dial_pos == 0:
            zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    solve()
