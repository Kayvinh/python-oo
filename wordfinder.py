from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file):
        self.file = open(file)
        self.words = []
        self.getWords()
        print (f"{len(self.words)} words read")

    def getWords(self):
        for line in self.file:
            #remove "/n" from end of line
            line = line[:len(line)-1:] #maybe use strip from lecture python-ds
            self.words.append(line)
        self.file.close()
    def random (self):
        return choice(self.words)




class SpecialWordFinder(WordFinder):
    def __init__ (self, file):
        super().__init__(file)

    def getWords(self):







# TRIED AND DID NOT WORK
# def getWords(self):
#         super().getWords()
#         for word in self.words:
#             if len(word) != 0 and not (word.startswith("#", 0)):
#                 self.not_special_words.append(word)


#         print(self.not_special_words)

