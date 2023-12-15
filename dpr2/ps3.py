"""
6.0001 Problem Set 3.

The 6.0001 Word Game
Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>

Name          : Latko Artem
Collaborators :
Time spent    :
"""
import os
import math
import random
import string
import logging
import json
import sys

WORDLIST_FILENAME = "words.txt"

# the current path to the script
script_path = os.path.dirname(os.path.abspath(__file__))
# change the current working directory to the one where the script is located
os.chdir(script_path)

text_path = os.path.join(script_path, WORDLIST_FILENAME)
config_path = os.path.join(script_path, 'config.json')

with open(config_path, 'r', encoding='utf-8') as config_file:
    config_data = json.load(config_file)

log_level_str = config_data.get('log_level')
log_level = getattr(logging, log_level_str, logging.DEBUG)

# Set up logging based on the configuration
logging.basicConfig(filename=config_data.get('log_file', 'hangman.log'),
                    level=log_level,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

logger = logging.getLogger(__name__)

if not os.path.exists(text_path):
    logging.fatal("words.txt file not found!!!")
    sys.exit("words.txt file not found!!!")
logging.info("The program is running!")

#######################################

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def load_words():
    """
    Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Get frequency dictionary.

    Return a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Return the score for a word. Assumes the word is a valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

    The score for a word is the product of two components:
    The first component is the sum of the points for letters in the word.
    The second component is the larger of:
        1, or
        7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
        and n is the hand length when the word was played.
    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on
    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()

    # Calculate the sum of points for letters in the word
    letter_sum = sum(SCRABBLE_LETTER_VALUES.get(letter, 0) for letter in word)

    second_component = max(1, 7 * len(word) - 3 * (n - len(word)))

    # Calculate the total word score
    word_score = letter_sum * second_component

    return word_score


def display_hand(hand):
    """
    Display the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):
    """
    Return a random hand containing n lowercase letters.

    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = int(math.ceil(n / 3))
    hand["*"] = 1

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """
    Return new hand.

    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()

    for letter in word.lower():
        if letter in new_hand:
            new_hand[letter] = new_hand.get(letter, 0) - 1

    return new_hand


def is_valid_word(word, hand, word_list):
    """
    Сheck for correct input.

    Return True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    if "*" in word:
        wildcard_index = word.find("*")
        if wildcard_index != -1:
            for vowel in VOWELS:
                new_word = word[:wildcard_index] + vowel + word[wildcard_index + 1:]
                if new_word in word_list:
                    return True
            return False

    if word not in word_list:
        return False
    # Check if each letter in the word is in the hand
    for letter in word:
        if letter not in hand or word.count(letter) > hand[letter]:
            return False

    return True


def calculate_handlen(hand):
    """
    Return the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    number_of_letters = sum(hand.values())
    return number_of_letters


def play_hand(hand, word_list):
    """
    Return total score.

    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
    """
    total_score = 0

    while calculate_handlen(hand) > 0:
        print("Current Hand: ", end='')
        display_hand(hand)
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        logging.debug(f"Guess: {word}")

        if word == '!!':
            logging.info("Guessing for the hand is complete!")
            break
        else:
            if is_valid_word(word, hand, word_list):
                logging.info("Correct guess!")
                word_score = get_word_score(word, calculate_handlen(hand))
                total_score += word_score
                print(f'"{word}" earned {word_score} points. Total: {total_score} points')
                print()
            else:
                print("This is not a valid word. Please choose another word.")
                logging.info("Incorrect guess!")
                print()
            hand = update_hand(hand, word)
            if calculate_handlen(hand) == 0:
                print(f'Ran out of letters.')

    return total_score


def substitute_hand(hand, letter):
    """
    Return hand.

    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter not in hand:
        return hand

    else:
        count = hand[letter]
        # Remove the letter from the hand
        del hand[letter]

        # Generate a new letter different from the user's choice and not in the hand
        available_letters = [letter for letter in ALPHABET if letter not in hand]
        new_letter = random.choice(available_letters)
        # Add the new letter to the hand with the same count
        hand[new_letter] = count

    return hand


def play_game(word_list):
    """
    Allow the user to play a series of hands.

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand. This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score_all_hands = 0
    while True:
        try:
            total_hands = int(input("Enter total number of hands: "))
            if total_hands > 0:
                logging.debug(f"Total number of hands: {total_hands}")
                break
            else:
                logging.error("Incorrect input!")
        except ValueError:
            logging.error("Incorrect input!")
            pass
    for h in range(total_hands):
        hand = deal_hand(HAND_SIZE)
        print(f"Current Hand: ", end='')
        display_hand(hand)
        while True:
            try:
                substitute = input("Would you like to substitute a letter?: ").lower()
                if substitute == 'yes' or substitute == 'no':
                    break
                else:
                    logging.error("Incorrect input!")
            except ValueError:
                logging.error("Incorrect input!")
                pass
        if substitute == "yes":
            logging.debug(f"To substitute a letter: {substitute}")
            while True:
                try:
                    substitute_letter = input("Which letter would you like to replace: ").lower()
                    if substitute_letter in hand and substitute_letter != "*":
                        logging.debug(f"Replacing the letter '{substitute_letter}'")
                        break
                    else:
                        logging.error("Incorrect input!")
                except ValueError:
                    logging.error("Incorrect input!")
                    pass
            hand = substitute_hand(hand, substitute_letter)

        elif substitute == "no":
            logging.debug(f"To substitute a letter: {substitute}")
        print()
        hand_score = play_hand(hand, word_list)
        print(f'Total score for this hand: {hand_score} points')
        print("--------------")
        while True:
            try:
                replay = input("Would you like to replay the hand?: ").lower()
                if replay == 'yes' or replay == 'no':
                    break
                else:
                    logging.error("Incorrect input!")
            except ValueError:
                logging.error("Incorrect input!")
                pass
        if replay == 'yes':
            logging.debug(f"To replay the hand: {replay}")
            replay_hand_score = play_hand(hand, word_list)
            hand_score = max(hand_score, replay_hand_score)
            print(f"Total score for this hand: {hand_score} points")
            print("--------------")
        elif replay == 'no':
            logging.debug(f"To replay the hand: {replay}")
        total_score_all_hands += hand_score
    print(f"Total score over all hands: {total_score_all_hands}")
    logging.info(f"Total score over all hands: {total_score_all_hands}")


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    logging.info("The program is complete!")
