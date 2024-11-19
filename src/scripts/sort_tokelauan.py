#!/usr/bin/env python3

import sys
from itertools import zip_longest
from functools import cmp_to_key

sentinel = object()
# TOKELAU_ALPHABET = "aāeēiīoōuūfgklmnphtvbcdjqrswxyz0123456789"
ALPHABET_VOWELS_NE = {
    "a": 0,
    "ā": 1,
    "e": 2,
    "ē": 3,
    "i": 4,
    "ī": 5,
    "o": 6,
    "ō": 7,
    "u": 8,
    "ū": 9,
    "f": 10,
    "g": 11,
    "k": 12,
    "l": 13,
    "m": 14,
    "n": 15,
    "p": 16,
    "h": 17,
    "t": 18,
    "v": 19,
    " ": -1,
    "\t": -1,
    "\n": -1,
    sentinel: 20,
}
ALPHABET_VOWELS_EQ = {
    "a": 0,
    "ā": 0,
    "e": 1,
    "ē": 1,
    "i": 2,
    "ī": 2,
    "o": 3,
    "ō": 3,
    "u": 4,
    "ū": 4,
    "f": 5,
    "g": 6,
    "k": 7,
    "l": 8,
    "m": 9,
    "n": 10,
    "p": 11,
    "h": 12,
    "t": 13,
    "v": 14,
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
