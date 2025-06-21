# Temperature Converter (Celsius to Fahrenheit)

A simple Python program that converts temperatures from Celsius to Fahrenheit with error handling and interactive input.

## Features
- Precise conversion: Uses the formula (°C × 9/5) + 32 = °F
- Error handling: Validates user input (only accepts numbers)
- Interactive: Runs in a loop until valid input is provided
- Clean output: Formatted results with degree symbols

## Installation
1. Clone the repository:
   git clone https://github.com/your-username/temperature-converter.git
2. Navigate to the project directory:
   cd temperature-converter

## Usage
Run the program:
python temperature_converter.py

Example session:
What's the temperature in Celsius? (or 'quit' to exit): 25
25.0°C = 77.0°F
──────────────────────────────

## Code Structure
def celsius_fahrenheit(temp_c: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return (temp_c * 9/5) + 32

# Main interactive loop
while True:
    user_input = input("What's the temperature in Celsius? (or 'quit' to exit): ")
    # ... (full code in repository)

## Documentation
### Conversion Formula
F = (C × 9/5) + 32
Where:
- F = Temperature in Fahrenheit
- C = Temperature in Celsius

### Error Handling
The program will:
- Reject non-numeric inputs
- Display clear error messages
- Allow graceful exit with 'quit' command