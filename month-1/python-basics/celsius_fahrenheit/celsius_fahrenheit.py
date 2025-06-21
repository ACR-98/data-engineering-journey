def celsius_fahrenheit(temp_c: float) -> float:
    """
    Converts temperature from Celsius to Fahrenheit.
    Formula: (0°C × 9/5) + 32 = 32°F

    Args:
        temp_c: Temperature in Celsius (float).

    Returns:
        Temperature in Fahrenheit (float).
    """
    return (temp_c * 9 / 5) + 32


while True:
    user_input = input("What's the temperature in Celsius? (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        temp_c = float(user_input)
        temp_f = celsius_fahrenheit(temp_c)
        print(f"\n{temp_c}°C = {temp_f}°F\n{'─' * 30}")
        break  # Exit after successful conversion
    except ValueError:
        print("Error: Please enter a valid number or 'quit'.\n{'─'*30}")
