import sys


# Helper functions
def all_is_increasing(report):
    return all(i < j and (j - i) < 4 for i, j in zip(report, report[1:]))

def all_is_decresing(report):
    return all(i > j and (i - j) < 4 for i, j in zip(report, report[1:]))

def problem_dapner(report):
    for i, _ in enumerate(report):
        new_list = report[:i] + report[i+1:]
        if all_is_increasing(new_list):
            return 1
        elif all_is_decresing(new_list):
            return 1
    return 0

def solve(data):
    # Part One
    safe_reports = 0 
    # Part Two
    pd_reports = 0
    
    for line in data:
        if all_is_increasing(line):
            safe_reports += 1
            continue
        elif all_is_decresing(line):
            safe_reports += 1
            continue
        else:
            pd_reports += problem_dapner(line)

    return safe_reports, (safe_reports + pd_reports)


if __name__ == "__main__":
    lines = [line.rstrip().split(" ") for line in sys.stdin.readlines()]
    lines = [list(map(int, line)) for line in lines if line != ['']]

    part_one, part_two = solve(lines)
    
    print(f"Part one: {part_one}")
    print(f"Part two: {part_two}")