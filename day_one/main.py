import sys
import collections

def partOne(data):
    left, right = [int(line[0]) for line in data], [int(line[3]) for line in data]
    return sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])

def partTwo(data):
    left, right = [int(line[0].rstrip()) for line in data], [int(line[3].rstrip()) for line in data]
    right_dupes = collections.Counter(right)
            
    return sum([l * right_dupes[l] for l in left])

if __name__ == "__main__":
    lines = [line.strip().split(" ") for line in sys.stdin.readlines()]
    print("Part One: {}".format(partOne(lines)))
    print("Part Two: {}".format(partTwo(lines)))