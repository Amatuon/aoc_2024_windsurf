from pathlib import Path
from collections import defaultdict, deque

def parse_input(input_path):
    """Parse the input file and return the ordering rules and updates."""
    with open(input_path, 'r') as file:
        content = file.read().strip()
        rules_section, updates_section = content.split('\n\n')
        
        # Parse rules into a graph (adjacency list)
        rules = defaultdict(set)
        for line in rules_section.split('\n'):
            before, after = map(int, line.split('|'))
            rules[before].add(after)
        
        # Parse updates into lists of page numbers
        updates = []
        for line in updates_section.split('\n'):
            update = list(map(int, line.split(',')))
            updates.append(update)
        
        return rules, updates

def is_valid_order(pages, rules):
    """Check if a sequence of pages follows the ordering rules."""
    # Create a position lookup for O(1) position checks
    positions = {page: i for i, page in enumerate(pages)}
    
    # Check each rule that applies to pages in this update
    for page in pages:
        if page in rules:
            # For each page that should come after this one
            for after_page in rules[page]:
                # If the after_page is in this update
                if after_page in positions:
                    # Check if it actually comes after
                    if positions[page] >= positions[after_page]:
                        return False
    
    return True

def get_middle_page(pages):
    """Get the middle page number from a sequence."""
    return pages[len(pages) // 2]

def topological_sort(pages, rules):
    """Sort pages according to the ordering rules using Kahn's algorithm."""
    # Build adjacency list and in-degree count for this subset of pages
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Only consider rules involving pages in this update
    page_set = set(pages)
    for page in pages:
        if page in rules:
            for after_page in rules[page]:
                if after_page in page_set:
                    graph[page].add(after_page)
                    in_degree[after_page] += 1
    
    # Initialize queue with nodes that have no incoming edges
    queue = deque([page for page in pages if in_degree[page] == 0])
    result = []
    
    # Process queue
    while queue:
        page = queue.popleft()
        result.append(page)
        
        # Remove edges from this node
        for next_page in graph[page]:
            in_degree[next_page] -= 1
            if in_degree[next_page] == 0:
                queue.append(next_page)
    
    return result

def part1(input_data):
    """Find sum of middle pages from correctly ordered updates."""
    rules, updates = input_data
    
    # Find correctly ordered updates and sum their middle pages
    total = 0
    for update in updates:
        if is_valid_order(update, rules):
            total += get_middle_page(update)
    
    return total

def part2(input_data):
    """Find sum of middle pages from reordered incorrect updates."""
    rules, updates = input_data
    
    # Find incorrectly ordered updates, sort them, and sum their middle pages
    total = 0
    for update in updates:
        if not is_valid_order(update, rules):
            sorted_update = topological_sort(update, rules)
            total += get_middle_page(sorted_update)
    
    return total

def main():
    # Load input from the current working directory
    input_data = parse_input(Path.cwd() / 'input.txt')
    
    # Solve parts
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == "__main__":
    main()
