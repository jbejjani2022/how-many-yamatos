#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python calculate.py <x> <y>")
        print("Calculates: x / (y * 1.07 + y * 0.18)")
        sys.exit(1)
    
    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        
        result = x / (y * 1.07 + y * 0.18)
        print(result)
        
    except ValueError:
        print("Error: Please provide valid floating point numbers")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Division by zero")
        sys.exit(1)

if __name__ == "__main__":
    main()