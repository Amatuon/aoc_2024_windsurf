import re
from pathlib import Path

def parse_input(input_path):
    """Parse the input file and return the corrupted memory content."""
    with open(input_path, 'r') as file:
        return file.read().strip()

def find_valid_multiplications(memory, handle_conditionals=False):
    """
    Find all valid mul(X,Y) instructions in the corrupted memory.
    If handle_conditionals is True, respect do() and don't() instructions.
    """
    if not handle_conditionals:
        # Part 1: Simple pattern matching
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = re.finditer(pattern, memory)
        return [int(x) * int(y) for x, y in (match.groups() for match in matches)]
    
    # Part 2: Process instructions sequentially
    results = []
    enabled = True  # Initially enabled
    pos = 0
    
    while pos < len(memory):
        # Check for do() instruction
        if memory[pos:].startswith('do()'):
            enabled = True
            pos += 4
            continue
            
        # Check for don't() instruction
        if memory[pos:].startswith("don't()"):
            enabled = False
            pos += 7
            continue
        
        # Check for mul instruction if enabled
        if enabled and memory[pos:].startswith('mul('):
            # Look for the closing parenthesis
            end_pos = memory.find(')', pos)
            if end_pos != -1:
                instruction = memory[pos:end_pos+1]
                match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', instruction)
                if match:
                    x, y = map(int, match.groups())
                    results.append(x * y)
                    pos = end_pos + 1
                    continue
        
        pos += 1
    
    return results

def part1(input_data):
    """Find and sum all valid multiplication results."""
    multiplications = find_valid_multiplications(input_data)
    return sum(multiplications)

def part2(input_data):
    """Find and sum all enabled multiplication results."""
    multiplications = find_valid_multiplications(input_data, handle_conditionals=True)
    return sum(multiplications)

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
