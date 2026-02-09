import random

class Game:
    def __init__(self):
        self.words = ['rollercoaster', 'ferriswheel', 'bumbercar', 'waterpark']  # Example words
        self.maximum_mistakes = 4
        self.remaining_mistakes = self.maximum_mistakes
        self.guess_history = [] 

    def make_guess(self, guess):
        if guess in self.words and guess not in self.guess_history:
            self.guess_history.append(guess)
            print(f'Correct guess: {guess}!')
        else:
            self.remaining_mistakes -= 1
            print(f'Incorrect guess: {guess}. Remaining mistakes: {self.remaining_mistakes}')

    def check_game_over(self):
        if self.remaining_mistakes <= 0:
            print('Game over! Maximum mistakes reached.')
            return True
        return False

    def play(self):
        print('Welcome to Coaster Connections Game!')
        while not self.check_game_over():
            guess = input('Make a guess (4 word options): ')
            self.make_guess(guess)
            print(f'Guesses so far: {self.guess_history}')
            if len(self.guess_history) == len(set(self.words)):
                print('Congratulations! You guessed all the words correctly!')
                break

if __name__ == '__main__':
    game = Game()
    game.play()