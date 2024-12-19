from pathlib import Path
from typing import Dict, List, Tuple, Set

def parse_input(input_path):
    """Parse the input file and return a 2D grid of antenna locations."""
    with open(input_path, 'r') as file:
        return [list(line.strip()) for line in file if line.strip()]

def find_antennas(grid: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Find all antenna locations grouped by their exact frequency."""
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.' and cell != '0':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return antennas

def calculate_antinodes(antennas: List[Tuple[int, int]], grid_width: int, grid_height: int) -> Set[Tuple[int, int]]:
    """Calculate all antinodes for a given frequency."""
    antinodes = set()
    for i, (x1, y1) in enumerate(antennas):
        for j, (x2, y2) in enumerate(antennas[i+1:], start=i+1):
            # Direction vector
            dx = x2 - x1
            dy = y2 - y1
            
            # Total distance between antennas
            total_dx = x2 - x1
            total_dy = y2 - y1
            
            # Two possible antinodes (outside the parent antennas)
            antinodex1 = x2 + dx
            antinodey1 = y2 + dy
            
            antinodex2 = x1 - dx
            antinodey2 = y1 - dy
            
            # Only add if within grid bounds
            if 0 <= antinodex1 < grid_width and 0 <= antinodey1 < grid_height:
                antinodes.add((antinodex1, antinodey1))
            
            if 0 <= antinodex2 < grid_width and 0 <= antinodey2 < grid_height:
                antinodes.add((antinodex2, antinodey2))
    
    return antinodes

def part1(grid: List[List[str]]) -> int:
    """
    Calculate the number of unique antinode locations.
    
    An antinode occurs when two antennas of the EXACT SAME frequency 
    have an antinode point exactly between them.
    """
    # Grid dimensions
    grid_width = len(grid[0])
    grid_height = len(grid)
    
    # Find all antenna locations
    antennas = find_antennas(grid)
    
    # Detailed logging
    print("Antenna frequencies:")
    for freq, locations in antennas.items():
        print(f"{freq}: {len(locations)} antennas")
    
    # Collect all unique antinodes
    all_antinodes = set()
    for freq, freq_antennas in antennas.items():
        # Only process frequencies with at least 2 antennas
        if len(freq_antennas) >= 2:
            freq_antinodes = calculate_antinodes(freq_antennas, grid_width, grid_height)
            print(f"{freq}: {len(freq_antinodes)} antinodes")
            all_antinodes.update(freq_antinodes)
    
    print(f"\nTotal unique antinodes: {len(all_antinodes)}")
    return len(all_antinodes)

def part2(grid: List[List[str]]) -> int:
    """Part 2 is not specified in the problem description."""
    return None

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()