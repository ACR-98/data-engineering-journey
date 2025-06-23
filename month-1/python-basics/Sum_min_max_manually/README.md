# List Statistics Calculator

A Python script that calculates the sum, maximum, and minimum of a list of numbers without using built-in functions like sum(), max(), or min().

## Features
- Manual calculation of sum, max, and min
- Robust input validation
- Error handling for non-numeric inputs
- Clean, modular code structure

## How It Works
1. Input Validation:
   - Accepts numbers separated by spaces (e.g., "10 5 20 3")
   - Validates input type (only numbers allowed)

2. Core Logic:
   - Iterates through the list to compute:
     - Sum: Accumulates total
     - Max/Min: Compares each value

## Code Structure
```python
def calculate_stats(numbers):
    """Calculates sum, max, and min of a list."""
    total = 0
    maximum = minimum = numbers[0]
    for num in numbers:
        total += num
        if num > maximum: maximum = num
        if num < minimum: minimum = num
    return total, maximum, minimum

def get_valid_numbers():
    """Prompts user until valid input is received."""
    while True:
        user_input = input("Enter numbers separated by spaces: ").strip()
        try:
            return [float(num) for num in user_input.split()]
        except ValueError:
            print("Error: Only numbers allowed (e.g., '3 5 2.1')")

if __name__ == "__main__":
    numbers = get_valid_numbers()
    total, maximum, minimum = calculate_stats(numbers)
    print(f"Sum: {total}, Max: {maximum}, Min: {minimum}")