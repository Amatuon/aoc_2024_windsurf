#!/usr/bin/env python3

import importlib
import os
import sys

def run_day(day_number):
    """
    Run a specific day's solution.
    
    Args:
        day_number (int): The day number to run (1-25)
    """
    try:
        # Construct the module name
        module_name = f"src.day_{day_number:02d}.day_{day_number:02d}"
        
        # Import the module dynamically
        day_module = importlib.import_module(module_name)
        
        # Print day header
        print(f"\n{'='*20}")
        print(f"Day {day_number}")
        print(f"{'='*20}")
        
        # Run the main function
        day_module.main()
    
    except ImportError:
        print(f"No solution found for Day {day_number}")
    except Exception as e:
        print(f"Error running Day {day_number}: {e}")

def main():
    # Get the directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add the base directory to Python path
    sys.path.insert(0, base_dir)
    
    # Run all days from 1 to 25
    for day in range(1, 26):
        run_day(day)

if __name__ == "__main__":
    main()
