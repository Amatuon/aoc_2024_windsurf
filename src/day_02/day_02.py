from pathlib import Path

def parse_input(input_path):
    """Parse the input file for the day's challenge."""
    with open(input_path, 'r') as file:
        return [list(map(int, line.split())) for line in file.readlines()]

def is_safe_report(report):
    """
    Check if a report is safe based on two conditions:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    """
    # Check if levels are strictly increasing
    increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(len(report)-1))
    
    # Check if levels are strictly decreasing
    decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(len(report)-1))
    
    return increasing or decreasing

def is_safe_with_problem_dampener(report):
    """
    Check if a report is safe by potentially removing one level
    """
    # If already safe, return True
    if is_safe_report(report):
        return True
    
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        # Create a new report without the i-th level
        modified_report = report[:i] + report[i+1:]
        
        # Check if the modified report is safe
        if is_safe_report(modified_report):
            return True
    
    return False

def part1(input_data):
    """Solve Part 1 of the challenge."""
    safe_reports = [report for report in input_data if is_safe_report(report)]
    return len(safe_reports)

def part2(input_data):
    """Solve Part 2 of the challenge with Problem Dampener."""
    safe_reports = [report for report in input_data if is_safe_with_problem_dampener(report)]
    return len(safe_reports)

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
