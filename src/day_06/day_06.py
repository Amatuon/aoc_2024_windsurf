from pathlib import Path
from enum import Enum
from typing import Set, Tuple, Optional, List
from copy import deepcopy
from tqdm import tqdm

class Direction(Enum):
    UP = (0, -1, '^')
    RIGHT = (1, 0, '>')
    DOWN = (0, 1, 'v')
    LEFT = (-1, 0, '<')
    
    def __init__(self, dx: int, dy: int, symbol: str):
        self.dx = dx
        self.dy = dy
        self.symbol = symbol
    
    def turn_right(self) -> 'Direction':
        """Return the direction after turning 90 degrees right."""
        directions = list(Direction)
        current_index = directions.index(self)
        return directions[(current_index + 1) % 4]

def parse_input(input_path):
    """Parse the input file and return the map and guard's starting position and direction."""
    with open(input_path, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
        
        # Find guard's starting position and direction
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell in '^>v<':
                    direction = next(d for d in Direction if d.symbol == cell)
                    return grid, (x, y), direction
    
    raise ValueError("No guard found in input")

def is_valid_position(x: int, y: int, grid: list) -> bool:
    """Check if a position is within the grid."""
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def simulate_guard_path(grid: list, start_pos: Tuple[int, int], start_dir: Direction, max_steps: int = 10000) -> set:
    """Simulate the guard's path and return visited positions."""
    visited = set()
    x, y = start_pos
    direction = start_dir
    steps = 0
    
    while steps < max_steps:
        # Calculate next position
        next_x = x + direction.dx
        next_y = y + direction.dy
        
        # Check if next position is valid and not blocked
        if not is_valid_position(next_x, next_y, grid):
            break
        
        if grid[next_y][next_x] == '#' or grid[next_y][next_x] == 'O':  # Include new obstacle
            # Turn right if blocked
            direction = direction.turn_right()
        else:
            # Move forward
            x, y = next_x, next_y
            pos = (x, y)
            
            visited.add(pos)
            steps += 1
    
    return visited

def find_loop_positions(grid: list, start_pos: Tuple[int, int], start_dir: Direction) -> List[Tuple[int, int]]:
    """Find all positions where adding an obstacle creates a loop."""
    height = len(grid)
    width = len(grid[0])
    loop_positions = []
    
    # First, simulate the original path
    original_path = simulate_guard_path(grid, start_pos, start_dir)
    
    # Try each empty position
    for y in tqdm(range(height), desc="Searching loop positions", total=height):
        for x in tqdm(range(width), desc=f"Row {y}", total=width, leave=False):
            # Skip positions that are already occupied or the start position
            if grid[y][x] != '.' or (x, y) == start_pos:
                continue
            
            # Create a copy of the grid and add an obstacle
            test_grid = deepcopy(grid)
            test_grid[y][x] = 'O'
            
            # Simulate path with obstacle
            obstructed_path = simulate_guard_path(test_grid, start_pos, start_dir)
            
            # Check if the paths are different (indicating a loop)
            if len(obstructed_path) < len(original_path):
                loop_positions.append((x, y))
    
    return loop_positions

def part1(input_data):
    """Count distinct positions the guard will visit."""
    grid, start_pos, start_dir = input_data
    print(f"Start position: {start_pos}, Start direction: {start_dir}")
    print(f"Grid size: {len(grid)}x{len(grid[0])}")
    visited = simulate_guard_path(grid, start_pos, start_dir, max_steps=10000)
    print(f"Visited positions: {len(visited)}")
    return len(visited)

def part2(input_data):
    """Count positions where adding an obstacle creates a loop."""
    grid, start_pos, start_dir = input_data
    print(f"Start position: {start_pos}, Start direction: {start_dir}")
    print(f"Grid size: {len(grid)}x{len(grid[0])}")
    loop_positions = find_loop_positions(grid, start_pos, start_dir)
    print(f"Loop positions: {len(loop_positions)}")
    return len(loop_positions)

def main():
    # Load input from the script's directory
    input_data = parse_input(Path(__file__).parent / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()