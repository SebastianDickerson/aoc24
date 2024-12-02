import sys
import collections


def solve(data):
    filtered = [(int(line[0]), int(line[3])) for line in data if len(line) > 3 and line[3] != ""]
    
    left, right = zip(*filtered) if filtered else ([], [])
    right_dupes = collections.Counter(right)

    differences = sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])
    similarities = sum([l * right_dupes[l] for l in left])
      
    return differences, similarities

if __name__ == "__main__":
    lines = [line.rstrip().split(" ") for line in sys.stdin.readlines()]
    result_one, result_two = solve(lines)

    print(f"Part One: {result_one}")
    print(f"Part Two: {result_two}")