from pathlib import Path

def parse_input(input_path):
    """Parse the input file for the day's challenge."""
    with open(input_path, 'r') as file:
        return file.read().strip().split('\n')

def part1(input_data):
    """Solve Part 1 of the challenge."""
    # TODO: Implement solution
    return None

def part2(input_data):
    """Solve Part 2 of the challenge."""
    # TODO: Implement solution
    return None

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
