import sys
import re


def part_one(data):
    total_sum = 0
    regex = r"mul\((\d+),(\d+)\)"
    
    for line in data:
        for match in re.finditer(regex, line):
            x = int(match.group(1))
            y = int(match.group(2))
            total_sum += x * y
    
    return total_sum

def part_two(data):
    mul_enabled = True
    total_sum = 0
    
    # Regex to match do(), don't(), and mul(x, y) instructions
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
    
    for line in data:
        for match in re.finditer(pattern, line):
            instruction = match.group(0)
            
            if instruction == "do()":
                mul_enabled = True
            elif instruction == "don't()":
                mul_enabled = False
                continue
            elif instruction.startswith("mul"):
                x = int(match.group(2))
                y = int(match.group(3))
                
                if mul_enabled:
                    total_sum += x * y
    
    return total_sum
        

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")