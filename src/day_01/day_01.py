from pathlib import Path
from collections import Counter

def parse_input(input_path):
    """Parse the input file into left and right lists."""
    with open(input_path, 'r') as file:
        lines = file.read().strip().split('\n')
        left_list = []
        right_list = []
        for line in lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list

def part1(input_data):
    """
    Calculate total distance between lists by pairing sorted numbers
    and summing their absolute differences.
    """
    left_list, right_list = input_data
    
    # Sort both lists
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))
    
    return total_distance

def part2(input_data):
    """
    Calculate similarity score by multiplying each left number
    by its frequency in the right list.
    """
    left_list, right_list = input_data
    
    # Count occurrences in right list
    right_counts = Counter(right_list)
    
    # Calculate similarity score
    similarity_score = sum(num * right_counts[num] for num in left_list)
    
    return similarity_score

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
