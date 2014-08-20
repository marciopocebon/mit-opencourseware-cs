class Printer:
    @staticmethod
    def print_info(num_guesses, available_letters):
        print 'You have %s guesses left.' % num_guesses
        print 'Available letters:', available_letters

    @staticmethod
    def print_successfully_message(guessed_word):
        print 'Good guess:', guessed_word

    @staticmethod
    def print_failure_message(guessed_word):
        print 'Oops! That letter is not in my word:', guessed_word

    @staticmethod
    def print_game_over(word):
        print 'Game over!'
        print 'The word is', word

    @staticmethod
    def print_congrats():
        print 'Congratulations, you won!'

    @staticmethod
    def print_welcome(word):
        print 'Welcome to the game, Hangman!'
        print 'I am thinking of a word that is %s letters long.' % len(word)

    @staticmethod
    def print_divisor():
        print '-'*30