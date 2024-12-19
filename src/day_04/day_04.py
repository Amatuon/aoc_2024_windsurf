from pathlib import Path

def parse_input(input_path):
    """Parse the input file and return the word search grid."""
    with open(input_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def check_mas(grid, row, col, dx, dy):
    """Check if MAS exists starting from (row, col) in direction (dx, dy)."""
    height = len(grid)
    width = len(grid[0])
    
    # Check bounds
    if not (0 <= row + 2*dx < height and 0 <= col + 2*dy < width):
        return False
    
    # Check forwards (MAS)
    forwards = (grid[row][col] == 'M' and
               grid[row + dx][col + dy] == 'A' and
               grid[row + 2*dx][col + 2*dy] == 'S')
               
    # Check backwards (SAM)
    backwards = (grid[row][col] == 'S' and
                grid[row + dx][col + dy] == 'A' and
                grid[row + 2*dx][col + 2*dy] == 'M')
                
    return forwards or backwards

def find_xmas(grid):
    """Find all occurrences of XMAS in the grid in all directions."""
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # Direction vectors for all 8 possible directions
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]
    
    def check_direction(row, col, dx, dy):
        """Check if XMAS exists starting from (row, col) in direction (dx, dy)."""
        if not (0 <= row + 3*dx < height and 0 <= col + 3*dy < width):
            return False
        
        return (grid[row][col] == 'X' and
                grid[row + dx][col + dy] == 'M' and
                grid[row + 2*dx][col + 2*dy] == 'A' and
                grid[row + 3*dx][col + 3*dy] == 'S')
    
    # Check each starting position
    for row in range(height):
        for col in range(width):
            # Try each direction from this position
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    count += 1
    
    return count

def find_x_mas(grid):
    """Find all X-shaped patterns with MAS on each diagonal."""
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # For each possible center point of the X
    for row in range(1, height - 1):  # Center needs space above and below
        for col in range(1, width - 1):  # Center needs space left and right
            # Check if we have MAS in both diagonals
            # Top-left to bottom-right diagonal
            tlbr = check_mas(grid, row - 1, col - 1, 1, 1)
            # Top-right to bottom-left diagonal
            trbl = check_mas(grid, row - 1, col + 1, 1, -1)
            
            # Both diagonals must contain MAS
            if tlbr and trbl:
                count += 1
    
    return count

def part1(grid):
    """Count all occurrences of XMAS in the word search."""
    return find_xmas(grid)

def part2(grid):
    """Count all occurrences of X-MAS patterns in the word search."""
    return find_x_mas(grid)

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
