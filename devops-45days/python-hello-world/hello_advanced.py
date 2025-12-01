#!/usr/bin/env python3
import sys

def greet(name="World"):
    """Print a greeting message."""
    print(f"Hello {name}")

def main():
    """Main function with command line argument support."""
    if len(sys.argv) > 1:
        name = sys.argv[1]
        greet(name)
    else:
        greet()

if __name__ == "__main__":
    main()
