from pathlib import Path
from itertools import product

def parse_input(input_path):
    """Parse the input file and return a list of equations."""
    equations = []
    with open(input_path, 'r') as file:
        for line in file:
            test_value, numbers_str = line.strip().split(': ')
            numbers = list(map(int, numbers_str.split()))
            equations.append((int(test_value), numbers))
    return equations

def concatenate(a, b):
    """Concatenate two numbers."""
    return int(str(a) + str(b))

def evaluate_equation(numbers, operators):
    """
    Evaluate an equation with given numbers and operators.
    Operators are applied left-to-right.
    Supports +, *, and || (concatenation) operators.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
        else:  # '||'
            result = concatenate(result, numbers[i+1])
    return result

def is_equation_possible(test_value, numbers):
    """
    Check if the equation can be made true by inserting operators.
    """
    # Number of operator positions is one less than number of numbers
    num_positions = len(numbers) - 1
    
    # Try all possible operator combinations (now including ||)
    for ops in product(['+', '*', '||'], repeat=num_positions):
        try:
            if evaluate_equation(numbers, ops) == test_value:
                return True
        except Exception:
            # In case of overflow or other calculation issues
            continue
    
    return False

def part1(equations):
    """
    Calculate the total calibration result by summing test values 
    of possible equations.
    """
    return sum(test_value for test_value, numbers in equations 
               if is_equation_possible(test_value, numbers))

def part2(equations):
    """
    Calculate the total calibration result using all three operators.
    """
    return sum(test_value for test_value, numbers in equations 
               if is_equation_possible(test_value, numbers))

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()