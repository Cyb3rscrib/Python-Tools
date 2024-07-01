**Cup Game
**

A simple cup game where you guess which cup hides the ball. This game is implemented in Python and is a fun way to practice basic programming concepts like list manipulation, user input, and randomization.

**How to Play
**
The game will shuffle a list of cups, one of which contains a ball ("O").
You will be prompted to guess which cup (0, 1, or 2) contains the ball.
The game will tell you if your guess was correct or not.
You can choose to play again or exit the game.

**Code Overview
**
Functions
shuffle_list(mylist): Takes a list and shuffles it.
player_guess(): Accepts a player guess until it's 0, 1, or 2.
check_guess(mylist, guess): Checks if the guess is correct.

**Main Game Loop
**
The game runs in a while loop, repeatedly shuffling the cups, accepting guesses, and checking if the guess is correct until the player decides to stop playing.

**Requirements
**
Python 3.x
