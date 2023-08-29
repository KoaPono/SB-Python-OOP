"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class to read in and find random words from dictionary
    
    >>> wf = WordFinder("words.txt")
    235888 words read

    >>> wf.getRandomWord() in wf.words
    True
    
    """
    def __init__(self, path):
        """Reads in words and ouputs number of words read"""
        file = open(path)
        self.words = self.parseWords(file)
        print(f"{len(self.words)} words read")

    def parseWords(self, file):
        return [word.strip() for word in file]

    def getRandomWord(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that removes comments
    
    >>> swf = SpecialWordFinder("./words.txt")
    235886 words read

    >>> swf.getRandomWord() in swf.words
    True
    """

    def parseWords(self, file):
        """Parse file -> list of words, skipping blanks/comments."""

        return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]