import random

def choose_word():
    words = ["python", "hangman", "computer", "keyboard", "science"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {max_wrong} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong:
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("Word: " + display_progress(word, guessed_letters))
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        # This runs if the while loop exits because wrong_guesses reached max_wrong
        print(f"\nGame over! You've used all {max_wrong} incorrect guesses.")
        print(f"The word was: {word}")

    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again == "y":
        print()
        play_hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_hangman()