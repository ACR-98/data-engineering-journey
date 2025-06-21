# Number Guessing Game

A fun Python console game where players guess a random number between 0-10 with limited attempts.

## Features
- Random number generation (0-10)
- 10 attempts to guess correctly
- Helpful "higher/lower" hints
- Input validation (numbers only, within range)
- Clear attempt counter
- Colorful console feedback

## Requirements
- Python 3.x

## How to Run
1. Save the code as number_guesser.py
2. Run in terminal:
   python number_guesser.py

## Game Rules
1. The game selects a secret number between 0-10
2. You have 10 attempts to guess it
3. After each wrong guess, you'll get:
   - A "higher/lower" hint
   - Your remaining attempt count

## Development
Key components:
- random.randrange(11) for number generation
- while loop with attempt counter
- try/except blocks for input validation
- if/elif/else structure for game logic

## Sample Gameplay
Guess a number between 0 and 10, you have 10 guesses left: 5
Incorrect! try a higher number, you have 9 attempts left
Guess a number between 0 and 10, you have 9 guesses left: 8
Correct! you got it, the number was 8

## License
MIT License - free to use and modify