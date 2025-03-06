# Number Guessing Game 

This is a simple **Number Guessing Game** built in Python. The game generates a random number between 50 and 100, and you have 5 chances to guess the correct number. The game provides feedback on whether your guess is too high or too low.

---

## Features

- **Random Number Generation**: A random number between 50 and 100 is generated for each game.
- **Limited Chances**: You have 5 chances to guess the correct number.
- **Colorful Feedback**: The game uses colored text to provide feedback on your guesses.
- **Fun and Interactive**: A colorful banner and messages make the game engaging.

---

## How to Run

1. **Save the Script**: Save the script as `num_guess_game.py`.
2. **Run the Script**: Open a terminal and navigate to the directory where the script is saved. Run the script using Python:
   ```bash
   python num_guess_game.py
   ```

---

## Gameplay

1. **Start the Game**: The game displays a colorful banner and instructions.
2. **Guess the Number**: Enter your guess when prompted.
3. **Feedback**:
   - If your guess is correct, you win! 🎉
   - If your guess is too high or too low, the game will tell you.
   - You have 5 chances to guess the correct number.
4. **End of Game**: If you guess the number within 5 tries, you win. Otherwise, the game ends, and the correct number is revealed.

---

## Example Output

```
I'm thinking of a number between 50 and 100 🤔
You have 5 chances to guess the number. Good Luck! 🍀

Enter your guess: 75
You have 4 chances left.
Your guess is too high, Try again 😕

Enter your guess: 60
You have 3 chances left.
Your guess is too low, Try again 😕

Enter your guess: 65
You have 2 chances left.
Your guess is too low, Try again 😕

Enter your guess: 70
You have 1 chances left.
Your guess is too high, Try again 😕

Enter your guess: 68
Congratulations! You guessed the number 68 in 5 tries. 🎉
```

---

## Customization

- **Range**: You can change the range of the random number by modifying the `random.randrange(50, 100)` line in the script.
- **Chances**: You can adjust the number of chances by changing the `chances` variable.

