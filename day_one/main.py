import sys
import collections

def partOne(data):
    left, right = [int(line[0].rstrip()) for line in data], [int(line[3].rstrip()) for line in data]
    return sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])

def partTwo(data):
    left, right = [int(line[0].rstrip()) for line in data], [int(line[3].rstrip()) for line in data]
    right_dupes = collections.Counter(right)
    sim_scores = []
    for l in left:
        sim_scores.append(l * right_dupes[l])
        
        
    print("Part Two: {}".format(sum(sim_scores)))
    

if __name__ == "__main__":
    lines = [line.split(" ") for line in sys.stdin.readlines()]
    print("Part One: {}".format(partOne(lines)))
    partTwo(lines)