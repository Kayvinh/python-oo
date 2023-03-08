from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """ Opens files and fills list with words and prints word count """
        file = open(path)
        self.words = self.get_words(file)
        file.close()
        print (f"{len(self.words)} words read")

    def get_words(self, file):
        """ Returns list of words without whitespace including \n """
        return [line.strip() for line in file]

    def random (self):
        """ Returns random word from words list """
        return choice(self.words)

    def __repr__(self):
        return f"<{self.__class__.__name__}> words={self.words}"


class SpecialWordFinder(WordFinder):
    """ SpecialWordFinder: filters invalid words from a list """



    def get_words(self, file):
        """ Returns list of words without comments or whitespace words """
        return [word for word in super().get_words(file)
            if word != "" and not word.startswith("#", 0)]

