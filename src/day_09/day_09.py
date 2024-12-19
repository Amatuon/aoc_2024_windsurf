from pathlib import Path

def parse_input(input_path):
    """Parse the input file and return the data."""
    with open(input_path, 'r') as file:
        return file.read().strip()

def compact_disk(disk_map):
    """
    Compact the disk by moving file blocks to the leftmost free space.
    
    Args:
        disk_map (str): The initial disk map configuration
    
    Returns:
        list: The compacted disk map
    """
    # Parse the disk map into files
    files = []
    i = 0
    file_id = 0
    while i < len(disk_map):
        length = int(disk_map[i])
        files.append((file_id, length))
        file_id += 1
        i += 1
    
    # Total number of blocks
    total_blocks = sum(file[1] for file in files)
    
    # Create initial representation with file blocks and free spaces
    disk = ['.' for _ in range(total_blocks)]
    
    # Place files from right to left into leftmost free spaces
    current_pos = 0
    for file_id, length in reversed(files):
        # Find the leftmost free space to place the file
        while current_pos < len(disk):
            # Check if we can place the file starting at current_pos
            if all(disk[j] == '.' for j in range(current_pos, current_pos + length)):
                # Place the file
                for j in range(length):
                    disk[current_pos + j] = file_id
                break
            current_pos += 1
    
    return disk

def part1(input_data):
    """
    Calculate the filesystem checksum after compaction.
    
    Args:
        input_data (str): The initial disk map
    
    Returns:
        int: The filesystem checksum
    """
    # Compact the disk
    compacted = compact_disk(input_data)
    
    # Calculate checksum
    checksum = 0
    for pos, block in enumerate(compacted):
        if block != '.':
            checksum += pos * block
    
    return checksum

def part2(input_data):
    """Solve Part 2 of the challenge."""
    return None

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()