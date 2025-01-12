#guess the number game
import random

print('Hello! What is your name?')

playerName = input()

print('Well, ' + playerName + ', I am thinking of a number between 1 and 10.')
print('Take a guess, you have 6 tries.')

guesses = 0

number = random.randint(1,10)

while guesses < 6:
    playerGuess = input()
    playerGuess = int(playerGuess)

    guesses = guesses + 1

    if playerGuess > number:

        print('Your guess is too HIGH.')
        print('Take another guess.')

    if playerGuess < number:

        print('Your guess is too LOW.')
        print('Take another guess.')

    if playerGuess == number:

        print('Good job, ' + playerName + '! You guessed my number in ' + str(guesses) + ' guesses!')

        break

if guesses >= 6:
    print('Womp womp, the number was ' + str(number))