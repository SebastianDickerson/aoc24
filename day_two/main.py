import sys


def solve(data):
    pass


if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    
    part_one, part_two = solve(lines)

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")