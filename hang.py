import random
import string

WORDLIST_FILENAME = "words.txt"

class Word():
    def __init__(self):
        self.infile = ""
        self.line = ""
        self.wordlist = ""

    def loadwords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        self.infile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.line = self.infile.readline()
        # wordlist: list of strings
        self.wordlist = string.split(self.line)
        print "  ", len(self.wordlist), "words loaded."
        return random.choice(self.wordlist)

class Guess():
    def __init__(self, secretword):
        self.secretword = secretword
        self.lettersguessed = []
        self.guessed = ''
        self.available = string.ascii_lowercase
        self.guesses = 8


    def iswordguessed(self):

        for letter in self.secretword:
            if letter in self.lettersguessed:
                pass
            else:
                return False

        return True

    def getguessedword(self):

        return self.guessed

    def getavailableletters(self):

        return self.available

    def hangman(self):

        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretword), ' letters long.'
        print '-------------'

        while self.iswordguessed() == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.getavailableletters()
            for letter in self.available:
                if letter in self.lettersguessed:
                    self.available = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ')
            if letter in self.lettersguessed:

                self.guessed = self.getguessedword()
                for letter in self.secretword:
                    if letter in self.lettersguessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Oops! You have already guessed that letter: ', self.guessed
            elif letter in self.secretword:
                self.lettersguessed.append(letter)

                self.guessed = self.getguessedword()
                for letter in self.secretword:
                    if letter in self.lettersguessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Good Guess: ', self.guessed
            else:
                self.guesses -= 1
                self.lettersguessed.append(letter)

                self.guessed = self.getguessedword()
                for letter in self.secretword:
                    if letter in self.lettersguessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Oops! That letter is not in my word: ', self.guessed
            print '------------'

        else:
            if self.iswordguessed() == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', self.secretword, '.'



word = Word()
secretword = word.loadwords().lower()
guess = Guess(secretword)
guess.hangman()
