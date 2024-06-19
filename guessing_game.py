





import random

# Dictionary of words categorized
words_dict = {
    "animals":["cat", "dog", "elephant", "lion", "tiger"],
    "fruits": ["apple", "banana", "orange", "grape", "melon"],
    "programming": ["python", "javascript", "java", "ruby", "php"]
}


# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Function to choose a word from a specific category
def choose_word(category):
    return random.choice(words_dict[category])


# Function to reveal a random letter as a hint
def provide_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    if remaining_letters:
        return random.choice(remaining_letters)
    return None


# Function to run the game
def guess_game():
    print("\nWelcome to the Guessing Game!")
    print("------------------------------")

    # Choose category
    print("Choose a category:")
    for category in words_dict.keys():
        print(category)

    category = input("\nEnter category: ").lower()
    while category not in words_dict:
        print("Invalid category. Please choose from the available categories.")
        category = input("Enter category: ").lower()

    # Randomly choose a word from the selected category
    word = choose_word(category)
    guessed_letters = set()

    # Difficulty levels
    difficulty_levels = {
        "easy": 8,
        "medium": 6,
        "hard": 4
    }

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    while difficulty not in difficulty_levels:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    attempts_left = difficulty_levels[difficulty]

    print("\nLet's begin!")
    print("Try to guess the word.")

    while attempts_left > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter or type 'hint' for a hint(Using a hint costs one attempt): ").lower().strip()

        # Input validation
        if guess == 'hint':
            if attempts_left == 1:
                print("Sorry, you cannot use a hint on your last attempt.")
            else:
                hint_letter = provide_hint(word, guessed_letters)
                print(f"Hint: One of the letters is '{hint_letter}'.")
                guessed_letters.add(hint_letter)
                attempts_left -= 1

            # Check if the word is fully guessed after the hint
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You guessed the word: '{word}'")
                return
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("* Invalid input. Please enter only one alphabetic letter. *")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Check if the word is fully guessed
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You guessed the word: '{word}'")
                return
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if attempts_left == 0:
        print(f"Game over! The word was: '{word}'")


# Start the game
guess_game()