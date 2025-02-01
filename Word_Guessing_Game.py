import random

words = ['home','physics','airport','weather','python','january','truck','football','castle']
word = random.choice(words)

print("Welcome to Word Guessing Game")
print("You will have 10 attempts to guess the correct word")
print("Guess the characters")

guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win ")
        print("The word is ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("You are wrong")
        print("You have", +turns, "more guesses")

        if turns == 0:
            print("You Loose")
    