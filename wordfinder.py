"""Word Finder: finds random words from a dictionary."""
#working with file.open/read

from random import choice

num_words = 0
word_list = []

class WordFinder:
    """Docstrings + Doctests
    
    >>>

    """

    def __init__(self, words_file):
        """Read dictionary of words and reports # of items read"""

        dict_file = open(words_file)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file to a list of words"""
        return [w.strip() for w in dict_file]

    
    # def __repr__(self):
    #     """representation of class"""

    def random(self):
        """returns random word from word list"""
        return choice(self.words)
    
class SpecialWordFinder (WordFinder):
    """Specialized WordFinder that excludes blank lines/comments"""

    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]