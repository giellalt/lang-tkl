#!/usr/bin/env python3

import sys
from functools import cmp_to_key

# aeioufgklmnphtv
# aāeēiīoōuūfgklmnphtv
# āēīōū

chars = {ch: i for i, ch in enumerate("aāeēiīoōuūfgklmnphtv")}
nchars = len(chars)


def cmp_fn(s1, s2):
    for a, b in zip(s1, s2):
        ka = chars.get(a, nchars)
        kb = chars.get(b, nchars)
        if ka > kb:
            return 1
        elif ka < kb:
            return -1
    return 0


strings = [line.strip() for line in sys.stdin]
strings.sort(key=cmp_to_key(cmp_fn))

for s in strings:
    print(s)
