import re

class BookBot:
    def __init__(self):
        self.pattern = r'[a-zA-Z]'
        self.alphabet = {}

    def open_book(self, filename):
        with open(filename) as f:
            file_contents = f.read()
            words = file_contents.split()
            return file_contents, words

    def split_words(self, words):
        letters = []
        for word in words:
            for char in word:
                letters.append(char)
        return letters

    def count_letters(self, letters):
        for letter in letters:
            letter = letter.lower()
            if not re.match(self.pattern, letter):
                continue
            if letter in self.alphabet:
                self.alphabet[letter] += 1
            else:
                self.alphabet[letter] = 1

    def generate_report(self):
        sorted_alpha = sorted(self.alphabet)
        for char in sorted_alpha:
            print(f"The letter {char} was found {self.alphabet[char]} times")

# script
counter = BookBot()
file_contents, words = counter.open_book("books/frankenstein.txt")
letters = counter.split_words(words)
counter.count_letters(letters)
counter.generate_report()
