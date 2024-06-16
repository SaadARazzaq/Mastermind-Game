'''

MasterMind Game:
Programming Language: Python
Interface: CLI based

'''

import random 

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    """Generate a random secret code."""
    code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    return code

def human_guess_code():
    """Allow a human player to guess the code."""
    while True:
        guess = input("Enter your guess (space-separated colors): ").upper().split()
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        if all(color in COLORS for color in guess):
            break
        else:
            print("Invalid colors. Please try again.")
    return guess

def evaluate_guess(guess, code):
    """Evaluate the guess and return the number of correct and incorrect positions."""
    correct_pos = sum(1 for g, c in zip(guess, code) if g == c)
    total_correct = sum((guess.count(color) if guess.count(color) <= code.count(color) else code.count(color)) for color in COLORS)
    incorrect_pos = total_correct - correct_pos
    return correct_pos, incorrect_pos

def play_human_vs_human():
    """Start a new 2-player game."""
    print("Player 1, create a secret code.")
    code = generate_code()
    print("Player 2, try to guess the code!")
    for attempt in range(1, TRIES + 1):
        print(f"Attempt {attempt}:")
        guess = human_guess_code()
        correct_pos, incorrect_pos = evaluate_guess(guess, code)
        if correct_pos == CODE_LENGTH:
            print("Congratulations! Player 2 guessed the code!")
            break
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("Player 2 ran out of tries. Player 1 wins!")
    print(f"The secret code was: {' '.join(code)}")

def play_human_vs_cpu():
    """Start a new single-player game against the CPU."""
    print("The CPU will create a secret code.")
    code = generate_code()
    print("Try to guess the code!")
    for attempt in range(1, TRIES + 1):
        print(f"Attempt {attempt}:")
        guess = human_guess_code()
        correct_pos, incorrect_pos = evaluate_guess(guess, code)
        if correct_pos == CODE_LENGTH:
            print("Congratulations! You guessed the code!")
            break
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("You ran out of tries. The CPU wins!")
    print(f"The secret code was: {' '.join(code)}")

def play_campaign():
    """Start a new single-player 'campaign' against the CPU."""
    # Define multiple levels with predefined codes
    levels = [
        ['R', 'G', 'B', 'Y'],  # Level 1
        ['R', 'R', 'G', 'G'],  # Level 2
        ['B', 'B', 'B', 'W']   # Level 3
    ]

    print("Welcome to the campaign mode!")
    for level, code in enumerate(levels, 1):
        print(f"Level {level}:")
        print("The CPU has created a secret code.")
        print("Try to guess the code!")
        for attempt in range(1, TRIES + 1):
            print(f"Attempt {attempt}:")
            guess = human_guess_code()
            correct_pos, incorrect_pos = evaluate_guess(guess, code)
            if correct_pos == CODE_LENGTH:
                print("Congratulations! You guessed the code!")
                break
            print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
        else:
            print("You ran out of tries. The CPU wins!")
        print(f"The secret code was: {' '.join(code)}")
        if level < len(levels):
            next_level = input("Press Enter to proceed to the next level.")

def main():
    print("Welcome to Mastermind!")
    print("Choose a game mode:")
    print("1. Human vs Human")
    print("2. Human vs CPU")
    print("3. Campaign")

    while True:
        choice = input("Enter the number of your choice (1-3): ")
        if choice == '1':
            play_human_vs_human()
            break
        elif choice == '2':
            play_human_vs_cpu()
            break
        elif choice == '3':
            play_campaign()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
