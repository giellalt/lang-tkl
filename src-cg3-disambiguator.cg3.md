# Tokelau disambiguator 

## Strict-tags
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 

## Delimiters 

- @NO CODE@  sentence delimiters

## Tags and sets 

- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 

- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 

- @NO CODE@ 

- @NO CODE@ 
- @NO CODE@ 
- @NO CODE@ 

- @NO CODE@ 
- @NO CODE@ 

- @NO CODE@ 

## rule SECTION  

### No context rules

### Local context rules (+/- 1)

- ō

- ke / kē

- ko

- mā

-  mai

-  na

-  nā

### NP

**PNP** removes V if N to the right of safe Pr

### VP

**V** selects V if Prs or Prf particle to the left

**VV** selects V if next word is a safe V

### Propernoun

**prop** selects Prop if not sentence-initially (relying on capital first letter)

Verbs

Preposition

**PrDemN** selects Pr in front of Dem N string (hmm, should it be Det N)

**PrN** selects Pr if in front of safe N

**NoPr** removes Pr when homoym with V and np NP or Pcle to the right

**Ve** selects V for "e" if followed by verb

**NoVe** removed V reading for all other "e"

**Det** selects Det when next word is N (hmm, careful mode?)

Nouns 

**NP** selects N when left word is safe Det or Poss

**maN** selects N for clause-initial *maa*

Late lexical rules

**ePrs** selects Prs for "e" if V to the right

**ePr** selects Pr for "e" if N to the right

**oi** removes N reading from "oi" for CC oi

Late verb rules

**dirverb** selects V for item in directioal verb set when next word is directional particle

**dirpcle** selects Pcle if verb to the left

* * *

<small>This (part of) documentation was generated from [src/cg3/disambiguator.cg3](https://github.com/giellalt/lang-tkl/blob/main/src/cg3/disambiguator.cg3)</small>
