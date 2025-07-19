from train import train


def play(ai):
    total = 20  # Starting number of sticks
    print("Welcome to Nim! There are 20 sticks. On your turn, take 1, 2, or 3 sticks.")
    player_turn = True
    while total > 0:
        print(f"\nSticks remaining: {total}")
        if player_turn:
            while True:
                try:
                    move = int(input("Your move (1-3): "))
                    if 1 <= move <= 3 and move <= total:
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number.")
        else:
            move = ai(total)
            print(f"AI takes {move} stick(s).")
        total -= move
        if total == 0:
            if player_turn:
                print("You took the last stick. You lose!")
            else:
                print("AI took the last stick. AI loses! You win!")
            break
        player_turn = not player_turn


ai = train()  # Train the AI with a fixed seed for reproducibility
# The AI is trained using Q-learning with a fixed seed for reproducibility.
# The `train` function initializes the AI with a random seed, trains it over many
# simulated games, and returns a function that can be used to make AI moves.
print("AI is trained. Let's play Nim!")
play(ai)
# The AI is trained using a basic strategy, and the game is played interactively.
# The `train` function initializes the AI with a random seed, and the `play`
# function starts the game where the AI plays against a human player.
# The AI learns from the game, improving its strategy over time.
