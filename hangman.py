# Problem Set 2, hangman.py
# Name: Vrublevskyi Oleksandr
# Collaborators: --
# Time spent: 12 hours

# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    t_word = []
    for i in secret_word:
        if i in letters_guessed:
            t_word.append(i)
        else:
            t_word.append("_ ")
    return ''.join(t_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = []
    for i in range(len(all_letters)):
        if all_letters[i] not in letters_guessed:
            available_letters.append(all_letters[i])
    return ''.join(available_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = "aeiou"

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings_remaining} warnings left')
    while (guesses_remaining > 0) and not (is_word_guessed(secret_word, letters_guessed)):
        print('-------------')
        print(f'You have {guesses_remaining} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        let=input("Please guess a letter:").lower()

        #Cheking for symbols quantity
        if len(let) > 1:
            print("Your input has more then one symbol")
            continue

        #Add hints, output all the aceptable words
        if let == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue


        #Checking for unwanted symbols
        if not let.isalpha():
            if warnings_remaining == 0:
                guesses_remaining -= 1
            else:
                warnings_remaining -= 1
            print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", end="")
            continue

        letters_guessed.append(let)

        #Cheking for repeating symbols
        if letters_guessed[-1] in letters_guessed[0:-1]:
            if warnings_remaining == 0:
                guesses_remaining -= 1
            else:
                warnings_remaining -= 1
            print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", end="")

        #Cheking for usuall mistake
        elif not (letters_guessed[-1] in secret_word):
            if letters_guessed[-1] in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", end="")

        #Cheking for right answer
        elif letters_guessed[-1] in secret_word:
            print("Good guess:", end="")

        print(get_guessed_word(secret_word, letters_guessed))

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", guesses_remaining * len(secret_word))
    else:
        print("Sorry, you ran out of guesses.")
        print("The word was else\nIt's", secret_word)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    emph = "_"

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] != emph:
            if my_word[i] != other_word[i]:
                return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    possible_matches = []
    my_word = my_word.replace(' ', '')
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    print(*possible_matches)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)