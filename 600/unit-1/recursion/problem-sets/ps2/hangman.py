from printer import Printer

class Hangman:
    
    def __init__(self, word):
        self.word = word.lower()
        self.num_guesses = len(self.word)
        self.available_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.letters = []
        self.guessed_word = '_'*len(self.word)
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
        Printer.print_successfully_message(self.guessed_word)

    def run_negative_feedback(self):
        self.num_guesses-=1
        Printer.print_failure_message(self.guessed_word)

    def give_feedback(self):
        self.update_available_letters()

        if self.selected_letter in self.word:
            self.run_positive_feedback()
        else:
            self.run_negative_feedback()

    def ask_for_a_letter(self):
        self.selected_letter = raw_input('Please, guess a letter:')

    def new_round(self):
        Printer.print_info(self.num_guesses, self.available_letters)

        if self.num_guesses > 0:
            self.ask_for_a_letter()
            self.give_feedback()
            Printer.print_divisor()
            if self.word == self.guessed_word:
                return Printer.print_congrats()
            self.new_round()
        else:
            Printer.print_game_over(self.word)

    def start(self):
        Printer.print_welcome(self.word)
        self.new_round()