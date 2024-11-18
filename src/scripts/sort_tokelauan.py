#!/usr/bin/env python3

import sys
from itertools import zip_longest
from functools import cmp_to_key

TOKELAU_ALPHABET = "aāeēiīoōuūfgklmnphtv"
ALPHABET = TOKELAU_ALPHABET if len(sys.argv) == 1 else sys.argv[1]

trans = str.maketrans({
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ō": "o",
    "ū": "u",
})


sentinel = object()
def mk_cmpfn(alphabet):
    chars = {ch: i for i, ch in enumerate(alphabet)}
    nchars = len(chars)

    alphabet_vowels_eq = {
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
        sentinel: -1,
    }

    def cmp_fn(s1, s2):
        translated = s2.translate(trans)
        if s1 == translated:
            # strings are equal if you consider short == long vowel
            for a, b in zip_longest(s1, s2, fillvalue=sentinel):
                ka = chars.get(a, nchars)
                kb = chars.get(b, nchars)
                if ka > kb:
                    return 1
                elif ka < kb:
                    return -1
            return 0
        else:
            for a, b in zip_longest(s1, s2, fillvalue=sentinel):
                ka = alphabet_vowels_eq.get(a, nchars)
                kb = alphabet_vowels_eq.get(b, nchars)
                if ka > kb:
                    return 1
                elif ka < kb:
                    return -1
            return 0

    return cmp_fn


key = cmp_to_key(mk_cmpfn(ALPHABET))
for s in sorted((line.strip() for line in sys.stdin), key=key):
    print(s)
