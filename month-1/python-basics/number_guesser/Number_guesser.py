import random #random number generator

def guessing_game():
    num_real = random.randrange(11) #we generate a random number from 0-10 (10 not included)
    guess_count = 10

    print("Welcome to the number guessing game!")
    while guess_count > 0:
        try:
            num_guess = int(input(f"Guess a number between 0 and 10, you have {guess_count} guesses left:  "))
            if num_guess == num_real:
                print(f"Correct! you got it, the number was {num_real}")
                return # Stops the whole function
            elif num_guess < 0 or num_guess > 10:
                print("<UNK> Please enter a number between 0 and 10.")
                continue # does not continue with the next else
            else:
                guess_count -= 1
                hint = "higher" if num_guess < num_real else "lower"
                print(f"Incorrect! try a {hint} number, you have {guess_count} attempts left")

        except ValueError:
            print("Entry must be a number. Try again.")

    print(f"\n💔 Game over! The secret number was {num_real}.")

if __name__ == "__main__": #Prevents the function from running automatically when called
    guessing_game()
