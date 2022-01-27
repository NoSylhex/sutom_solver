def case_func(text):
    return text.lower()

class Verifier:
    def __init__(self, words):
        self.words = words

    def apply_size(self, size):
        self.words = [case_func(w) for w in self.words if len(w)==size]

    def apply_letter_at(self, letter, index):
        letter = case_func(letter)
        self.words = [w for w in self.words if w[index]==letter]

    def apply_no_letter_at(self, letter, index):
        letter = case_func(letter)
        self.words = [w for w in self.words if w[index]!=letter]

    def apply_letter_in(self, letter):
        letter = case_func(letter)
        self.words = [w for w in self.words if letter in w]

    def apply_no_letter_in(self, letter):
        letter = case_func(letter)
        self.words = [w for w in self.words if not letter in w]
    


# if __name__ == '__main__':
#     words = ['abc', 'a', 'klu', 'inu', 'ljskdff']
#     words = ['abdoman', 'abdomen', 'adkjsa', 'ajshdki', 'asjdk', 'aksjdh']
#     verifier = Verifier(words)
#     wordsize = int(input('size: '))
#     verifier.apply_size(wordsize)
#     # print(len(solver.words))
#     verifier.apply_letter_at('a', 0)
#     print(verifier.words)

#     verifier.apply_letter_in('e')
#     print(verifier.words)