"""
Codigo para jogo da forca.
Refatorado por Amanda Muniz.
"""
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"

class Word():
    """
    Essa classe lida com o arquivo de palavras e escolhe a palavra.
    """
    def __init__(self):
        self.wordlist = ""
        self.infile = ""
        self.line = ""

    def loadwords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        try:
            self.infile = open(WORDLIST_FILENAME, 'r', 0)
        except FileNotFoundError:
            print'Sorry, the file cant be found'
            sys.exit()
        # line: string
        self.line = self.infile.readline()
        # wordlist: list of strings
        self.wordlist = string.split(self.line)
        print "  ", len(self.wordlist), "words loaded."
        return random.choice(self.wordlist).lower()

class Guess():
    """
    Essa classe lida com o jogo em si. Nela estao presentes todas as
    funcoes que manipulam a palavra escolhida.
    """
    def __init__(self, secretword):
        self.word = Word()
        self.secretword = secretword
        self.lettersguessed = []
        self.guessed = ''
        self.available = string.ascii_lowercase
        self.guesses = 8
        self.letters = 0

    def iswordguessed(self):
        """
        Essa funcao verifica se a letra ja foi escolhida e se
        esta presente na palavra secreta.
        """
        for letter in self.secretword:
            if letter in self.lettersguessed:
                pass
            else:
                return False

        return True

    def getguessedword(self):
        """
        Funcao get para pegar a palavra adivinhada.
        """
        return self.guessed

    def getavailableletters(self):
        """
        Funcao get para as letras disponiveis no jogo.
        """
        return self.available

    def getlettersofword(self):
        """
        Funcao para pegar o numero de letras diferentes
        na palavra secreta.
        """
        for letter in self.available:
            if letter in self.secretword:
                self.letters += 1
        return self.letters

    def changeword(self):
        """
        Essa funcao muda a palavra se o numero de letras diferentes
        presentes nela e maior que o numero de jogadas.
        """
        while self.getlettersofword() > 8:
            print 'This word is too big for this game'
            self.secretword = self.word.loadwords()
            if self.letters <= self.guesses:
                break
            break
        return self.secretword

    def initialmenu(self):
        """
        Menu inicial do jogo.
        """
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretword), ' letters long.'
        print '-------------'
        print 'The word has ', self.getlettersofword(), 'differents letters.'

    def hangman(self):
        """
        Funcao main do jogo.
        """
        self.initialmenu()

        if self.getlettersofword() > 8:
            self.changeword()

        while self.iswordguessed() == False and self.guesses > 0:
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
                        print '\n'


                print 'Oops! That letter is not in my word: ', self.guessed
            print '------------'
            print '\n'

        else:
            if self.iswordguessed() == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', self.secretword, '.'

word = Word()
secretword = word.loadwords().lower()
guess = Guess(secretword)
guess.hangman()
