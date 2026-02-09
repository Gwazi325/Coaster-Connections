from coaster_connections import ConnectionsGame

def main():
    game = ConnectionsGame()
    max_mistakes = 4
    mistakes = 0

    print("Welcome to the Connections Game!")
    print("Guess the connections by entering 4 words at a time.")
    print(f"You can make up to {max_mistakes} mistakes.")

    while mistakes < max_mistakes:
        guess = input("Enter your guess (4 words separated by spaces): ")
        words = guess.split()

        if len(words) != 4:
            print("Please enter exactly 4 words.")
            continue

        if game.check_guess(words):
            print("Correct guess!")
            game.record_correct_guess(words)
        else:
            mistakes += 1
            print(f"Wrong guess! You have {max_mistakes - mistakes} mistakes left.")

        if game.is_completed():
            print("Congratulations! You've completed the game.")
            break

    if mistakes >= max_mistakes:
        print("Game over! You've made too many mistakes.")

if __name__ == "__main__":
    main()