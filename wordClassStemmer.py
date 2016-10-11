"""Word Class Stemmer: returns the stem of a given word

From https://github.com/daalft/PaliNLP
License: GPLv2
"""


import os
import sys

#! instead of reading as the .py in there, read the plain text files and load as objects
# endings_dir = os.path.expanduser('~/cltk_data/pali/stem/endings')
# sys.path.insert(0, endings)

import wordClassGuesser
# import endings
from data import endings
from data.endings.endings import retainEndings

wcg = wordClassGuesser.guessWordClassFromLemma
retainEndings = retainEndings
exceptions = list('-_(){}[]?!–')


def stemRecursive(word, ends):
    """Recursive function to keep stemming a word."""
    for end in ends:
        if word.endswith(end):
            index = word.rindex(end)
            return stemRecursive(word[0:index],ends)
    return word


def stemOne(word, out=[]):
    """Final algorithm to stem a given word.
    Returns the stemmed word.
    """
    out = []
    wordClasses = (wcg(word))
    if len(wordClasses) == 0:
        out.append(stemRecursive(word, 'all'))
        return out

    for pos in wordClasses:
        endings = retainEndings(pos)
        if len(endings) == 0:
            endings = retainEndings("all")
        out1 = set()
        out1.add(stemRecursive(word,endings))
    out = list(out1)
    return out


def stem(sentence):
    """Final algorithm to stem a sentence.
    Returns the stemmed sentence
    """
    inp = sentence.split()
    out = ''
    for i in range(len(inp)):
        if inp[i] in exceptions:
            out += inp[i]
        else:
            out += stemOne(inp[i])[0] + ' '
    return out.strip()

