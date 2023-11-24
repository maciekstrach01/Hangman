import sys
import requests
import json

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game(user_word, no_of_tries, used_letters):
    print()
    print(user_word)
    print("Trials remaining:", no_of_tries)
    print("Letters used:", used_letters)
    print()

def show_guessed_words(guessed_words):
    print("\nGuessed words:")
    for word, definition in guessed_words.items():
        print(f"{word}: {definition}")


def show_unguessed_words(used_words, guessed_words):
    print("\nUnguessed words:")
    for word in used_words - set(guessed_words.keys()):
        definition = get_word_definition(word)
        print(f"{word}: {definition}")


def get_random_word(used_words):
    api_url = "https://random-word-api.herokuapp.com/word?number=1"
    
    while True:
        response = requests.get(api_url)
        word_data = response.json()
        new_word = word_data[0] if word_data else "default"

        if new_word not in used_words:
            used_words.add(new_word)
            return new_word

def get_word_definition(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return data[0]["meanings"][0]["definitions"][0]["definition"]
    except (requests.RequestException, KeyError, IndexError):
        return "No definition."

def select_difficulty():
    print("\nDifficulty levels:")
    print("1. Easy (10 attempts)")
    print("2. Medium (6 trials)")
    print("3. Difficult (3 attempts)")

    while True:
        difficulty_choice = input("Choose a difficulty level (1-3): ")
        if difficulty_choice in ["1", "2", "3"]:
            return int(difficulty_choice)
        else:
            print("Incorrect choice. Select 1 to 3.")

def play_hangman(difficulty, used_words, guessed_words, word):
    no_of_tries = 10 if difficulty == 1 else 6 if difficulty == 2 else 3
    used_letters = []
    user_word = ["_" for _ in word]

    while True:
        try:
            letter = input("Enter the letter: ")

            if not letter.isalpha() or len(letter) != 1:
                raise ValueError("Provide a single letter.")

            if letter in used_letters:
                raise ValueError("This letter has already been used.")

            used_letters.append(letter)

            found_indexes = find_indexes(word, letter)

            if len(found_indexes) == 0:
                print("There is no such letter.")
                no_of_tries -= 1

                if no_of_tries == 0:
                    print("Game over :( The correct word is:", word)
                    break
            else:
                for index in found_indexes:
                    user_word[index] = letter

                if "".join(user_word) == word:
                    print(word + "\nBravo, that's the word!")

                    definition = get_word_definition(word)
                    guessed_words[word] = definition
                    save_state(used_words, guessed_words)
                    break

            show_state_of_game(user_word, no_of_tries, used_letters)

        except ValueError as e:
            print(f"Error : {e}")
            show_state_of_game(user_word, no_of_tries, used_letters)

    definition = get_word_definition(word)
    print("Definition:", definition)

def main_menu(used_words, guessed_words):
    while True:
        print("\nMenu:")
        print("1. Play the game")
        print("2. Exit the game")
        print("3. Show guessed words")
        print("4. Show unguessed words")

        choice = input("Select an option: ")

        if choice == "1":
            difficulty = select_difficulty()
            word = get_random_word(used_words)
            play_hangman(difficulty, used_words, guessed_words, word)
        elif choice == "2":
            save_state(used_words, guessed_words)
            print("Thank you for playing. Goodbye!")
            sys.exit(0)
        elif choice == "3":
            show_guessed_words(guessed_words)
        elif choice == "4":
            show_unguessed_words(used_words, guessed_words)
        else:
            print("Incorrect selection. Select option 1 to 4.")

def save_state(used_words, guessed_words):
    with open("guessed_words.txt", "w") as guessed_file:
        for word, definition in guessed_words.items():
            guessed_file.write(f"{word}: {definition}\n")

    with open("used_words.txt", "w") as used_file:
        for word in used_words:
            used_file.write(word + "\n")

def load_state():
    try:
        with open("guessed_words.txt", "r") as guessed_file:
            guessed_words = {}
            for line in guessed_file:
                parts = line.strip().split(": ", 1)
                if len(parts) == 2:
                    word, definition = parts
                    guessed_words[word] = definition

        with open("used_words.txt", "r") as used_file:
            used_words = {line.strip() for line in used_file}

        return used_words, guessed_words
    except FileNotFoundError:
        return set(), {}

guessed_words = {}
used_words, guessed_words = load_state()

while True:
    main_menu(used_words, guessed_words)
