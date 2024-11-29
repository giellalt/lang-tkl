#!/usr/bin/env python3

import sys
from itertools import zip_longest
from functools import cmp_to_key

sentinel = object()
# TOKELAU_ALPHABET = "AaĀāEeĒēIiĪīOoŌōUuŪūFfGgKkLlMmNnPpHhTtVvBbCcDdJjQqRrSsWwXxYyZz0123456789"
ALPHABET_VOWELS_NE = {
#    "A": 0,
#    "a": 1,
#    "Ā": 2,
#    "ā": 3,
#    "E": 4,
#    "e": 5,
#    "Ē": 6,
#    "ē": 7,
#    "I": 8,
#    "Ī": 9,
#    "ī": 10,
#    "O": 11,
#    "o": 12,
#    "ō": 13,
#    "Ō": 14,
#    "u": 15,
#    "Ū": 16,
#    "ū": 17,
#    "F": 18,
#    "f": 19,
#    "G": 20,
#    "g": 21,
#    "K": 22,
#    "k": 23,
#    "L": 24,
#    "l": 25,
#    "M": 26,
#    "m": 27,
#    "N": 28,
#    "n": 29,
#    "P": 30,
#    "p": 31,
#    "H": 32,
#    "h": 33,
#    "T": 34,
#    "t": 35,
#    "V": 36,
#    "v": 37,
    "A": 0,
    "Ā": 1,
    "E": 2,
    "Ē": 3,
    "I": 4,
    "Ī": 5,
    "O": 6,
    "Ō": 7,
    "Ū": 8,
    "F": 9,
    "G": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "P": 15,
    "H": 16,
    "T": 17,
    "V": 18,
    "a": 19,
    "ā": 20,
    "e": 21,
    "ē": 22,
    "ī": 23,
    "o": 24,
    "ō": 25,
    "u": 26,
    "ū": 27,
    "f": 28,
    "g": 29,
    "k": 30,
    "l": 31,
    "m": 32,
    "n": 33,
    "p": 34,
    "h": 35,
    "t": 36,
    "v": 37,
   " ": -1,
    "\t": -1,
    "\n": -1,
    sentinel: 20,
}
ALPHABET_VOWELS_EQ = {
    "A": 0,
    "Ā": 0,
    "a": 1,
    "ā": 1,
    "E": 2,
    "Ē": 2,
    "e": 3,
    "ē": 3,
    "I": 4,
    "Ī": 4,
    "i": 5,
    "ī": 5,
    "O": 6,
    "Ō": 6,
    "o": 7,
    "ō": 7,
    "U": 8,
    "Ū": 8,
    "u": 9,
    "ū": 9,
    "F": 10,
    "f": 11,
    "G": 12,
    "g": 13,
    "K": 14,
    "k": 15,
    "L": 16,
    "l": 17,
    "M": 18,
    "m": 19,
    "N": 20,
    "n": 21,
    "P": 22,
    "p": 23,
    "H": 24,
    "h": 25,
    "T": 26,
    "t": 27,
    "V": 28,
    "v": 29,
    " ": -1,
    "\t": -1,
    "\n": -1,
    sentinel: 15,
}
LONG_VOWELS_AS_SHORT = str.maketrans({
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ō": "o",
    "ū": "u",
    "Ā": "A",
    "Ē": "E",
    "Ī": "I",
    "Ō": "O",
    "Ū": "U",
})


def cmp(s1, s2):
    if s1 == s2.translate(LONG_VOWELS_AS_SHORT):
        chars = ALPHABET_VOWELS_NE
    else:
        chars = ALPHABET_VOWELS_EQ

    for a, b in zip_longest(s1, s2, fillvalue=sentinel):
        ka = chars.get(a, chars[sentinel])
        kb = chars.get(b, chars[sentinel])
        if ka < kb:
            return -1
        if ka > kb:
            return 1
    return 0


for s in sorted((line.strip() for line in sys.stdin), key=cmp_to_key(cmp)):
    print(s)
