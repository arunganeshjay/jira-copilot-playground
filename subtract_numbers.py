"""Simple program to subtract two numbers from command-line input."""

import sys


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def main():
    """Read two numbers from the user and print their difference."""
    if len(sys.argv) == 3:
        # Numbers provided as command-line arguments
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers.")
            sys.exit(1)
    else:
        # Interactive prompt
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please provide valid numbers.")
            sys.exit(1)

    result = subtract(a, b)
    print(f"The difference of {a} and {b} is {result}")


if __name__ == "__main__":
    main()
