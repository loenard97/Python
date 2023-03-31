import requests
from requests import ConnectTimeout, HTTPError, Timeout, ConnectionError

MAX_WRONG_GUESSES = 15
WORD_API_URL = "https://random-word-api.herokuapp.com/word"
DICTIONARY_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def main():
    try:
        word = requests.get(WORD_API_URL).json()[0]
    except (ConnectTimeout, HTTPError, Timeout, ConnectionError):
        print(f"An Error occurred while trying to read a random word from '{WORD_API_URL}'.")
        return
    right_guesses = set()
    wrong_guesses = 0

    print("Take a guess for the following word (capitalization is ignored):")
    while True:
        # print word
        hidden_word = ''.join([letter if letter.casefold() in right_guesses else '_' for letter in word])
        print(hidden_word)

        # check win and fail condition
        if '_' not in hidden_word:
            print(f"Congrats! "
                  f"You got the word right with {wrong_guesses} wrong guess{'es' if wrong_guesses != 1 else ''}.")
            break
        if wrong_guesses > MAX_WRONG_GUESSES:
            print(f"Sorry. You took to many guesses. The word would have been '{word}'")
            break

        # check if guess is correct
        guess = input("Your guess: ")
        if guess and guess.isalpha():
            guess = guess[0].casefold()
        else:
            print("You have to guess a letter. Try again.\n")
            continue
        guesses_left = MAX_WRONG_GUESSES - wrong_guesses
        if guess in word.casefold():
            print(f"Correct. ({guesses_left} guess{'es' if guess != 1 else ''} left)\n")
            right_guesses.add(guess)
        else:
            wrong_guesses += 1
            print(f"Nope. Try again. ({guesses_left} guess{'es' if guess != 1 else ''} left)\n")

    # print dictionary definition
    print(f"Dictionary definition of {word}:")
    definition = requests.get(DICTIONARY_API_URL + word).json()
    if definition:
        if "phonetic" in definition[0]:
            print("Phonetic: " + definition[0]["phonetic"])
        if "meanings" in definition[0]:
            print("Meanings:")
            for meaning in definition[0]["meanings"][0]["definitions"]:
                print(" - " + meaning["definition"])
    else:
        print(f"Could not find definition for '{word}'")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThank you for playing!")
