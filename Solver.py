import random
from FileHandler import FileHandler
from Verifier import Verifier


class Solver:
    def __init__(self, filename):
        self.fileHandler = FileHandler(filename)
        self.verifier = Verifier(self.fileHandler.get_words())

    def show_words(self, number=10):
        answer = 'y'
        while answer.lower()=='y':
            print(f'There are {len(self.verifier.words)} words possible.\nHere are 10 randoms words:')
            print('\n'.join([random.choice(self.verifier.words) for _ in range(number)]))
            answer = input('\nWould you like to see more words ?(y/n)')

    def first_round(self):
        wordSize = int(input('Select the size of the word: '))
        self.verifier.apply_size(wordSize)
        
        firstLetter = input('Select the first letter of the word: ')
        self.verifier.apply_letter_at(firstLetter, 0)        

    def round(self):
        last_word = input('Enter the last word you tried: ')
        good_letters = input('Precise the letters positioned correctly separated with space (ex: a e o): ').split(' ')
        position_letters = input('Precise the letters that are not in their right position separated with space (ex: a e o): ').split(' ')

        for letter in good_letters:
            self.verifier.apply_letter_at(letter, last_word.find(letter))
        for letter in position_letters:
            self.verifier.apply_no_letter_at(letter, last_word.find(letter))
            self.verifier.apply_letter_in(letter)
        for letter in last_word:
            if not letter in good_letters and not letter in position_letters:
                self.verifier.apply_no_letter_in(letter)

    def end_game(self):
        if len(self.verifier.words) == 1:
            print(f'The answer should be: {self.verifier.words[0]}.\nOtherwise this app is doomed.')
        elif len(self.verifier.words) == 0:
            print('No more word available... This app is doomed.')
        else:
            print('You win !')

    def run(self):
        self.first_round()
        self.show_words()

        stop_run = 'n'
        while stop_run.lower() == 'n' and len(self.verifier.words) > 1:
            self.round()
            self.show_words(min(10, len(self.verifier.words)))
            stop_run = input('Have you win already ?(y/n)')
        
        self.end_game()
