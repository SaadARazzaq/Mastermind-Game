# MasterMind Game

## Overview
MasterMind is a classic code-breaking game where players try to guess a secret code consisting of a sequence of colors. This Python-based version of MasterMind is a Command-Line Interface (CLI) game that supports different game modes, including Human vs Human, Human vs CPU, and a Campaign mode.

## Features
- CLI-based gameplay
- Multiple game modes: Human vs Human, Human vs CPU, and Campaign
- Random code generation for CPU
- Predefined codes for Campaign mode
- Feedback on guesses, indicating correct positions and incorrect positions

## Requirements
- Python 3.x

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Download or clone the game script to your local machine.

## How to Play
1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:
    ```sh
    python mastermind.py
    ```

## Game Modes
### 1. Human vs Human
- Player 1 creates a secret code.
- Player 2 tries to guess the code within a limited number of attempts (10 tries).

### 2. Human vs CPU
- The CPU generates a random secret code.
- The human player tries to guess the code within 10 attempts.

### 3. Campaign
- The player goes through multiple levels with predefined secret codes.
- Each level presents a new code to guess within 10 attempts.

## Scoring
- After each guess, feedback is provided indicating the number of correct positions and incorrect positions.
- A correct position means the guessed color is in the correct place.
- An incorrect position means the guessed color is correct but in the wrong place.

## Game Instructions
### Starting the Game
- When the game starts, you will be prompted to choose a game mode.
- Enter the number corresponding to your desired game mode (1-3).

### Making a Guess
- For each attempt, enter your guess as space-separated color codes (e.g., `R G B Y`).
- Valid color codes are:
  - R: Red
  - G: Green
  - B: Blue
  - Y: Yellow
  - W: White
  - O: Orange

### Ending the Game
- The game ends when the code is correctly guessed or the number of attempts is exhausted.
- In Campaign mode, the game progresses to the next level upon correctly guessing the code.

## Game Outputs

![image](https://github.com/SaadARazzaq/Mastermind-Game/assets/123338307/87d0f22c-3ddf-491f-8c96-92887a0f36ba)
![image](https://github.com/SaadARazzaq/Mastermind-Game/assets/123338307/f7896817-7a08-4953-b206-3135e529d34f)
![image](https://github.com/SaadARazzaq/Mastermind-Game/assets/123338307/d6cc1116-4808-488e-80e4-982919daab49)

# Test Cases:

![image](https://github.com/SaadARazzaq/Mastermind-Game/assets/123338307/fb1c4f9d-f4c7-4483-a10c-d9c844786bb2)

## Developer Notes
- The game uses the `random` library for generating random codes.
- The `COLORS` list defines the possible colors in the code.
- The `TRIES` constant sets the maximum number of attempts (default is 10).
- The `CODE_LENGTH` constant sets the length of the secret code (default is 4).

## Future Enhancements
- Add more levels to the Campaign mode.
- Implement additional difficulty settings.
- Improve user feedback and error handling.

---

Enjoy playing MasterMind! If you encounter any issues or have suggestions for improvements, feel free to contribute or open an issue.
