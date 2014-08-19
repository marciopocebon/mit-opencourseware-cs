# 6.00 Problem Set 3
# 
# Hangman
#

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

class Hangman:
    
    def __init__(self, word):
        self.word = word.lower()
        self.num_guesses = len(self.word)
        self.available_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.letters = []
        self.guessed_word = ''
        self.selected_letter = ''

    def update_guessed_word(self):
        self.guessed_word = ''
        
        for word_letter in self.word:
            if word_letter in self.letters:
                self.guessed_word += word_letter
            else:
                self.guessed_word += '_'

    def update_available_letters(self):
        self.available_letters = self.available_letters.replace(self.selected_letter, '')

    def is_letter_in_word(self, letter):
        return letter in self.word

    def letter_already_chosen(self, letter):
        return letter in self.letters

    def run_positive_feedback(self):
        self.letters.append(self.selected_letter)
        self.update_guessed_word()
        self.print_successfully_message()

    def run_negative_feedback(self):
        self.num_guesses-=1
        self.print_failure_message()

    def give_feedback(self):
        self.update_available_letters()

        if self.selected_letter in self.word:
            self.run_positive_feedback()
        else:
            self.run_negative_feedback()

    def ask_for_a_letter(self):
        self.selected_letter = raw_input('Please, guess a letter:')

    def print_info(self):
        print 'You have %s guesses left.' % self.num_guesses
        print 'Available letters:', self.available_letters

    def print_successfully_message(self):
        print 'Good guess:', self.guessed_word

    def print_failure_message(self):
        print 'Oops! That letter is not in my word:', self.guessed_word

    def print_game_over(self):
        print 'Game over!'
        print 'The word is', self.word

    def print_congrats(self):
        print 'Congratulations, you won!'

    def welcome(self):
        print 'Welcome to the game, Hangman!'
        print 'I am thinking of a word that is %s letters long.' % len(self.word)

    def print_divisor(self):
        print '-'*10

    def new_round(self):
        self.print_info()

        if self.num_guesses > 0:
            self.ask_for_a_letter()
            self.give_feedback()
            self.print_divisor()
            if self.word == self.guessed_word:
                return self.print_congrats()
            self.new_round()
        else:
            self.print_game_over()

    def start(self):
        self.welcome()
        self.new_round()


words = load_words()
word = choose_word(words)
hangman = Hangman(word)
hangman.start()