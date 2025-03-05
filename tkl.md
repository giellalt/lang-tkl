# Tokelauan language model documentation

All doc-comment documentation in one large file.

---

# src-cg3-dependency.cg3.md 

# Tokelau dependency grammar 

## strict-tags
Alphabet below must be all multichar symbols used in all rules
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

## Delimiters #

### Sets

... to be documented

*# Rules

First som e adjustment rules

### NP rules

### PPs

### ellipse

### S

Rules for subj and obj (to be revised)

### preposition to verb

### VPs

### CS

### CC

### subjunction and coordination

### Root

* * *

<small>This (part of) documentation was generated from [src/cg3/dependency.cg3](https://github.com/giellalt/lang-tkl/blob/main/src/cg3/dependency.cg3)</small>

---

# src-cg3-disambiguator.cg3.md 

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

- lava

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

---

# src-cg3-functions.cg3.md 

# Tokelau functions grammar

Tag declaration via STRICT-tAGS
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 
- *@NO CODE@ 

- *@NO CODE@ 

# Tags and sets #

- *@NO CODE@  
- *@NO CODE@ 

## Parts of speech

* Sets for POS sub-categories

* Sets for Semantic tags

* Sets for Morphosyntactic properties

* Sets for verbs

* Miscellaneous sets

* Border sets and their complements

* Syntactic sets

These were the set types.

## Rules

Map Interj, CC, CS, ..

PP complement rules

NP complemnt rules

## Map clause structure tags

## PP rules

## FMV

## The X rule

Map any leftover as @X

* * *

<small>This (part of) documentation was generated from [src/cg3/functions.cg3](https://github.com/giellalt/lang-tkl/blob/main/src/cg3/functions.cg3)</small>

---

# src-fst-morphology-affixes-adjectives.lexc.md 

Adjective inflection
The Tokelauan language adjectives compare.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adjectives.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/adjectives.lexc)</small>

---

# src-fst-morphology-affixes-nouns.lexc.md 

Noun inflection
The Tokelauan language nouns inflect in number and cases.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/nouns.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/nouns.lexc)</small>

---

# src-fst-morphology-affixes-numerals.lexc.md 

Numeral affix file

* **LEXICON ARABICCASES**  adds +Arab

* **LEXICON ARABICCASE**  adds +Arab

* **LEXICON ARABICCASE0**  adds +Arab

!! __LEXICON NUM-PREFIXES__

* __LEXICON REALARABICfirst__ to avoid 0 as first arabic, except from only 0, or in front of comma

* __LEXICON REALARABICpunct__ to get number after

* __LEXICON REALARABIC__ 1-4 arabics

* __LEXICON REALARABICfirstpart__ numbers like 199 878, 199.878, 199,878, 12000-13000

* __LEXICON REALDECARABICsecond__ 19912,878 and 12000-13000

* __LEXICON REALDECARABICdec__ hyph and comma

* __LEXICON REALARABICsecondpart__ numbers like 199 878 and 199.878
allow 199,878 as special typo

* __LEXICON REALARABICsecondpart_cont__ loop, to case suffix, to , or -,

* __LEXICON REALARABICDECIM__ loop and to % and case suffix

* __LEXICON ARABIC__ +Sem/ID, +Ord

* __LEXICON ARABICLOOPS__

* __LEXICON ARABICSabcdef__

* __LEXICON ARABICDATE__

* __LEXICON ARABICDATEHYPH__

* __LEXICON ARABICDATENUM__

* __LEXICON ARABICDATENUM2__

* __LEXICON datetag_w_dot_cont__

* __LEXICON ARABICCLOCK__ is a regex for clock time.

* __LEXICON CLOCK-sep__ different separators for intervals, or one clock time only

* __LEXICON ARABICCLOCK2__ is the second component of intervals, idntical to ARABICCLOCK

* __LEXICON ARABICCLOCK2x__ is the second component of intervals,

* __LEXICON ARABICCLOCKDECIMALS__ is fractional seconds

* __LEXICON ARABICYEAR__

* __LEXICON numyear__

* __LEXICON moreyear__

* __LEXICON moreyearx__

* __LEXICON yeartagplx__

* __LEXICON ARABICORD__

* __LEXICON REALARABICDELIMITER__

* __LEXICON ARABICLOOP__

* __LEXICON MARKDOT__

* __LEXICON ROMAN__  roman numerals

* __LEXICON ROM-SINGEL__

* __LEXICON ROM-THOUSAND__

* __LEXICON ROM-THOUSAND-TAG__

* __LEXICON ROM-HUNDRED__

* __LEXICON ROM-HUNDRED-TAG__

* __LEXICON ROM-TEN__

* __LEXICON ROM-TEN-TAG__

* __LEXICON ROM-ONE__

* __LEXICON ROM-ONE-TAG__

* __LEXICON ROM-SPLIT__

* __LEXICON 2ROMAN__

* __LEXICON 2ROM-THOUSAND__

* __LEXICON 2ROM-THOUSAND-TAG__

* __LEXICON 2ROM-HUNDRED__

* __LEXICON 2ROM-HUNDRED-TAG__

* __LEXICON 2ROM-TEN__

* __LEXICON 2ROM-TEN-TAG__

* __LEXICON 2ROM-ONE__

* __LEXICON 2ROM-ONE-TAG__

* __LEXICON ISOLATED-NUMEXP__ some isolated numeral expressions

* __LEXICON ARABICLOOPORD__ ordinals

* __LEXICON ACASETAG__  is for 1e+Num+Sg+Num:1e

* __LEXICON ARABICDELIMITER__  blank + 3 delim, what does the lg counc prefer?

* __LEXICON ARABICDELIMITERORD__ ordinals

* __LEXICON PROSENT__ % and case suffix

* __LEXICON POSTPROSENT__ % and case suffix

* __LEXICON ROMNUMTAG__

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/numerals.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/numerals.lexc)</small>

---

# src-fst-morphology-affixes-propernouns.lexc.md 

Proper noun inflection
The Tokelauan language proper nouns inflect in the same cases as regular
nouns, but perhaps with a colon (':') as separator.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/propernouns.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/propernouns.lexc)</small>

---

# src-fst-morphology-affixes-symbols.lexc.md 


# Symbol affixes

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/symbols.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/symbols.lexc)</small>

---

# src-fst-morphology-affixes-verbs.lexc.md 

Verb inflection
The Tokelauan language verbs inflect for number.

# Prefixes

LEXICON Verbs  splits to subgrups according to pl form

* S = syll; R, E = C V in redup pattern

* LEXICON 2v_pref  = 2-syllabic verbs with CV reduplication

* LEXICON 3v_pref  = 3-syllabic verbs with CV reduplication

* LEXICON tav_pref  = 3-syllabic verbs with CV to ta

* LEXICON ta_pref  = 2-syllabic verbs with ta prefix

* LEXICON 3redup_pref  = 2-syllabic verbs with full reduplication

* LEXICON 4redup_pref  = 2-syllabic verbs with full reduplication

# Suffixes

* LEXICON vsg  

* LEXICON vpl  

* LEXICON vtags  = adds POS and Sg, Pl tags as governed by the U flags

* LEXICON tvtags  = adds POS and Sg, Pl tags as governed by the U flags

* LEXICON tv  

* LEXICON redup_suff  = adds POS and Sg, Pl tags as governed by the U flags

* LEXICON redup_suff_sgflags  
* LEXICON redup_suff_plflags  

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/verbs.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/affixes/verbs.lexc)</small>

---

# src-fst-morphology-phonology.twolc.md 

=================================== !
The Tokelauan morphophonological/twolc rules file !
=================================== !

# Alphabet 
-  a b c d e f g h i j k l m n o p q r s t u v w x y z    = lower case
-  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z    = upper case
-  %^R:f %^R:g %^R:k %^R:l %^R:m %^R:n %^R:p %^R:h %^R:t %^R:v   = redup Cns
-  %^R1:f %^R1:g %^R1:k %^R1:l %^R1:m %^R1:n %^R1:p %^R1:h %^R1:t %^R1:v   = tja
-  %^R2:f %^R2:g %^R2:k %^R2:l %^R2:m %^R2:n %^R2:p %^R2:h %^R2:t %^R2:v   = tja
-  %^E:a %^E:e %^E:i %^E:o %^E:u    = redup Vow
-  %^E1:a %^E1:e %^E1:i %^E1:o %^E1:u    = tja
-  %^E2:a %^E2:e %^E2:i %^E2:o %^E2:u    = tja
-  %^3S:0   
 %^T:t %^A:a  = ta prefix
-  %>:0    = suffix border
-  a2 e2 i2 o2 u2 ;   for Petele2ema - Peteleema *Petelēma
The digit 2 to be removed in longvowel-cleanup.regex 
# Sets  

-  Vow = a e i o u      
- ā ē ō ī ū Ā Ē Ō Ī Ū ; long vowels  
-  Cns = b c d f g h j k l m n p q r s t v w x y z ;   

# Rules  

**RULE: ^R realisation as consonant** = duplicates C for reduplication

**RULE: ^E realisation as vowel** = duplicates V for reduplication

**RULE: ^R1 realisation as consonant** = duplicates C1 for full reduplication

**RULE: ^E1 realisation as vowel** = duplicates V1 for full reduplication

**RULE: ^R2 realisation as consonant** = duplicates C3 for full reduplication

**RULE: ^E2 realisation as vowel** = duplicates V2 for full reduplication

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.twolc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/phonology.twolc)</small>

---

# src-fst-morphology-root.lexc.md 


INTRODUCTION TO THE MORPHOLOGICAL ANALYSER FOR Tokelauan .

# Definitions for Multichar_Symbols

## Composed letters

- a2 e2 i2 o2 u2 these are for first part of lexical aa, ee, ii, oo, uu

## Analysis symbols
The morphological analyses of wordforms for the Tokelauan
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).

The parts-of-speech are:
- +N +A +Adv +V
- +Pron +CS +CC +Adp +Po +Pr +Interj +Pcle +Num
- +Incl +Excl
- +Rom

The parts of speech are further split up into:
- +Prop +Pers +Dem +Interr +Refl +Recipr +Rel +Indef +Poss
- +Def +Det
- +Prox +Med +Dist = proximal, medial, distal (near speaker, hearer, neiter)

- +Post +Pre = postmodifiers, premodifiers

The Usage extents are marked using following tags:
- +Err/Orth
- +Use/-Spell
* **+Use/TTS** – **only** retained in the HFST Text-To-Speech disambiguation tokeniser
* **+Use/-TTS** – **never** retained in the HFST Text-To-Speech disambiguation tokeniser

The nominals are inflected in the following  Number
- +Sg +Du +Pl
- +Nom +Gen +Acc
- +Loc for locative nouns

The possession is marked as such:
Numerals are classified under:
Verb moods are:
Other verb forms are

* +Symbol = independent symbols in the text stream, like £, €, ©
Special symbols are classified with:
The verbs are syntactically split according to transitivity:
Special multiword units are analysed with:
Non-dictionary words can be recognised with:

For reduplication
 ^R ^E ^R1 ^R2 ^E1 ^E2 ^3S ^T ^A ^[ ^]  cons, vow, for 2- and 3-syll

+Dir   directional

Question and Focus particles:
 +Qst +Foc  

+Prf +Ipf +Fut   Aspect, perhaps

- +Emph 
- +Dem-Dist 
- +Du1 
- +Du2 
- +Du3 
- +Pl1 
- +Pl2 
- +Pl3 
- +Sg1 
- +Sg2 
- +Sg3 
- +Use/GC 

Semantics are classified with
- +Sem/Date 
- +Sem/Measr 
- +Sem/Time-clock 

- +Sem/Ani 
- +Sem/Build 
- +Sem/Clth 
- +Sem/Edu 
- +Sem/Fem 
- +Sem/Group 
- +Sem/Hum 
- +Sem/Mal 
- +Sem/Measr 
- +Sem/Obj 
- +Sem/Org 
- +Sem/Plant 
- +Sem/Plc 
- +Sem/Route 
- +Sem/Sur 
- +Sem/Time 
- +Sem/Txt 
- +Sem/Veh 
- +Sem/Wthr 

These tags are used somewhere:

Derivations are classified under the morphophonetic form of the suffix, the
source and target part-of-speech.

Morphophonology
To represent phonologic variations in word forms we use the following
symbols in the lexicon files:

And following triggers to control variation

## Flag diacritics
We have manually optimised the structure of our lexicon using following
flag diacritics to restrict morhpological combinatorics - only allow compounds
with verbs if the verb is further derived into a noun again:
|  @P.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @D.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @C.NeedNoun@ | (Dis)allow compounds with verbs unless nominalised

For languages that allow compounding, the following flag diacritics are needed
to control position-based compounding restrictions for nominals. Their use is
handled automatically if combined with +CmpN/xxx tags. If not used, they will
do no harm.
|  @P.CmpFrst.FALSE@ | Require that words tagged as such only appear first
|  @D.CmpPref.TRUE@ | Block such words from entering ENDLEX
|  @P.CmpPref.FALSE@ | Block these words from making further compounds
|  @D.CmpLast.TRUE@ | Block such words from entering R
|  @D.CmpNone.TRUE@ | Combines with the next tag to prohibit compounding
|  @U.CmpNone.FALSE@ | Combines with the prev tag to prohibit compounding
|  @P.CmpOnly.TRUE@ | Sets a flag to indicate that the word has passed R
|  @D.CmpOnly.FALSE@ | Disallow words coming directly from root.

Use the following flag diacritics to control downcasing of derived proper
nouns (e.g. Finnish Pariisi -> pariisilainen). See e.g. North Sámi for how to use
these flags. There exists a ready-made regex that will do the actual down-casing
given the proper use of these flags.
|  @U.Cap.Obl@ | Allowing downcasing of derived names: deatnulasj.
|  @U.Cap.Opt@ | Allowing downcasing of derived names: deatnulasj.

Use the following flag diacritics to control tag placement for prefixing
|  @U.verb.sg@ | Tag moving from prefixing to +Sg
|  @U.verb.pl@ | Tag moving from prefixing to +Pl
|  @U.noun.sg@ | Tag moving from prefixing to +Sg
|  @U.noun.pl@ | Tag moving from prefixing to +Pl
|  @C.ErrOrth@ | a pematch tag to remove

|               Flag diacritic | Explanation
|               :------------- |:-----------
|  @P.Pmatch.Loc@ | Used on multi-token analyses; tell hfst-tokenise/pmatch where in the form/analysis the token should be split. Used e.g. in `bijladagi` to split `bijla` from `dagi`, or after abbreviations with full stops before the full stop, to allow an alternate `+CLB` analysis of it in case of a sentence final abbreviation. __NB!__ This will give a faulty lemma for the abbreviation, as it will not include the full stop. This can lead to other issues, but presently we have no other solution if we want to keep the full stopp as a separate token. We could leave a full stop at the end of the abbreviation lemma as well (but not on the input side - we only have one full stop in the input). That must be tested, it could work, but then requires special attention when generating suggestions in e.g. grammar checkers - it should not generate two full stops. 
|  @P.Pmatch.Backtrack@ | Used on single-token analyses; tell hfst-tokenise/pmatch to backtrack by reanalysing the substrings before and after this point in the form (to find combinations of shorter analyses that would otherwise be missed)

|               Flag diacritic | Explanation
|               :------------- |:-----------
| @D.ErrOrth.ON@ | To be written
| @R.ErrOrth.ON@ | To be written
| @C.ErrOrth@ | To be written
| @P.ErrOrth.ON@ | To be written

|              Flag diacritic | Explanation
|              :------------- |:-----------
|  @U.number.one@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.two@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.three@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.four@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.five@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.six@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.seven@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.eight@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.nine@ | Flag used to give arabic numerals in smj different cases ;
|  @U.number.zero@ | Flag used to give arabic numerals in smj different cases ;

| @P.number.one@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.two@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.three@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.four@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.five@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.six@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.seven@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.eight@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.nine@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.ten@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.one@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.two@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.three@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.four@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.five@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.six@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.seven@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.eight@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.nine@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.ten@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.one@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.two@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.three@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.four@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.five@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.six@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.seven@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.eight@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.nine@ | Flag used to give arabic numerals in smj different cases ;
| @P.number.ten@ | Flag used to give arabic numerals in smj different cases ;

- **@@ODE@**
The word forms in Tokelauan language start from the lexeme roots of basic
word classes, or optionally from prefixes:

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/root.lexc)</small>

---

# src-fst-morphology-stems-conjunctions.lexc.md 

# Tokelau conjunctions

- +CC: # ;  

- oi cc "and" ;  
- kae cc "and, when, while, but" ;  
- ma cc "and" ;  
- ona cc "fordi" ;  
- ka cc "but" ;  
- kana cc "if" ;  
- ona cc ;  

- +CS: # ;  

- kāfai cs "if" ;  
- kafai cs "if" ;  
- ke cs "so" ;    introducing subordinate clauses.
- auā cs "because" ;  
- heiloga cs "unless" ;  
- vāganā cs "unless" ;  

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/conjunctions.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/conjunctions.lexc)</small>

---

# src-fst-morphology-stems-determiners.lexc.md 

# Tokelau determiners

Documentation: NP overview:
1. (preposition) -> in prepositions.lexc
2. determiner -> Determiners
3. (possessive pronoun)
4. (premodifier)
5. nucleus
6. (postmodifier)
7. (demonstrative)

-Dem may occur both pre-N and post-N:
before N they function as Det, after N they
must have another Det as support. (taimi = time)
tēnei taimi, te taimi tēnei

## pre-nominal
sg

unspecified for number

pl

## Possessors

### Singular reference

du1

pl1

### Plural reference

du1

pl1
pl3
TODO

# System should be:
- particles before / after N
- particles before / after V

- proximal or first person (objects near to the speaker),
- medial or second person (objects near to the addressee),
- distal or third person

post-nominal
sg

unspecified for number

pl

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/determiners.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/determiners.lexc)</small>

---

# src-fst-morphology-stems-interjections.lexc.md 

# Interjections

- +Interj: # ;  

- fakamolemole ij "sorry" ;  
- fakafetai ij "thank you" ;  
- aho ij "good afternoon" ;  
- afiafi ij "good evening" ;  
- mâlô ij "greeting" ;  
- tâlofa ij "greeting" ;  
- hāloa ij "what a pity" ;  
That was all interjections

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/interjections.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/interjections.lexc)</small>

---

# src-fst-morphology-stems-nouns.lexc.md 

# Tokelau Nouns
Nouns in the Tokelauan language refer to objects or sets of objects, qualities, states or ideas.

- tamāloa:tamaalo^R^Ea nredupsuf "man" ;   (one redupnoun)

## Locative noun s

- uta locnoun " The islets on the far" ;  
- fafo locnoun " Outside, out of" ;  
- falē locnoun "Communal settlement," ;  
- gāuta locnoun " 1. Shore, land, (from" ;  

- Todo: Check these:
- Iaugātogi n "Prize giving. Nae" ;  
- Taumuliava n "rad itio" ;  
- Iaupāma n "Palm leaf. (n.b." ;  
- Lafalafa n "Traditional name given" ;  

## Ordinary nouns

- a n "Letter A." ;  
- āeto n "(Bb.). Eagle. He" ;  
- āeto:aaeto n "eagle" ;  
- āiā n "Right, claim" ;  
- aiha:aiha n "ice" ;  
- aihiga n "Sam. ‘aisiga A" ;  
- aitu n "ghost, spirit. E" ;  
- ao n "daylight" ;  
- aoao n "Supremacy. Ko" ;  
etc

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/nouns.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/nouns.lexc)</small>

---

# src-fst-morphology-stems-numerals.lexc.md 

# Tokelau Numerals

* CODE@
* CODE@

* CODE@ for the arabic numerals        !
* CODE@ for the roman numerals         !
* CODE@ for §34 etc.                   !
* CODE@ for ½ etc.                     !

* CODE@ except when counting, which is tahi
* CODE@
* CODE@
* CODE@
* CODE@
etc. up to 30, thereafter tens and hundreds and thousands up to 9000

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/numerals.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/numerals.lexc)</small>

---

# src-fst-morphology-stems-particles.lexc.md 

# Tokelau particles

* CODE@
* CODE@

* CODE@
* CODE@

* CODE@
* CODE@ Post-verbal directional
* CODE@ Post-verbal directional
* CODE@ anaphoric particle, after Pr, referring to antecedent
* CODE@ In front of Prop, Pron, locnoun
* CODE@Post-nominal emphatic
* CODE@Post-verbal directional
* CODE@preverbal qualifying particle (oioti oi kaumai te tuhi)
* CODE@follows the word it emph
* CODE@Pre-nominal, introducing S or NP
* CODE@in phrase "i lō"
* CODE@Pre-verbal particle
* CODE@interrogative particle !
* CODE@Pre-pronominal particle, o-class
* CODE@Pre-pronominal particle, a-class
* CODE@Pre-verbal particle
* CODE@in front of numerals

That was all particles

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/particles.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/particles.lexc)</small>

---

# src-fst-morphology-stems-prefixes.lexc.md 

Prefixes
Prefixes in the Tokelauan language are attatched to the left of other words.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/prefixes.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/prefixes.lexc)</small>

---

# src-fst-morphology-stems-prepositions.lexc.md 

# Tokelau Prepositions
============

* CODE@
* CODE@

* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@

That was all prepositions

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/prepositions.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/prepositions.lexc)</small>

---

# src-fst-morphology-stems-pronouns.lexc.md 

# Tokelau Pronouns
Pronouns in the Tokelauan language are words that may replace nouns or refer to participants in the conversation.

* **CODE@**
* CODE@
* CODE@
* CODE@
* CODE@

* **CODE@**
* CODE@
* CODE@
* CODE@
* ...

* CODE@
* CODE@
* CODE@
* CODE@
* ...

* CODE@
* CODE@
* CODE@
* ... cf. also the adverbs.lexc file

* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* ...

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/pronouns.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/pronouns.lexc)</small>

---

# src-fst-morphology-stems-propernouns.lexc.md 

# nTokelau proer nouns

* **LEXICON Propernouns**
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* CODE@
* ...

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/propernouns.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/propernouns.lexc)</small>

---

# src-fst-morphology-stems-verbs.lexc.md 

# Verbs
Verbs in the Tokelauan language inflect for tense.

* **LEXICON v_particles**

* **LEXICON aux**

* **LEXICON auxtag**

* LEXICON 2v_stems  = 2-syllabic verbs with CV reduplication

* LEXICON 3v_stems = 3-syllabic verbs with CV reduplication

* LEXICON tav_stems   = 3-syllabic verbs with CV to ta prefix

* LEXICON ta_stems = 2-syllabic verbs with ta prefix

* LEXICON 4redup_stems = 2-syllabic verbs with full reduplication

* LEXICON 3redup_stems = 2-syllabic verbs with full reduplication

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbs.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/morphology/stems/verbs.lexc)</small>

---

# src-fst-transcriptions-transcriptor-abbrevs2text.lexc.md 



We describe here how abbreviations are in Tokelauan are read out, e.g.
for text-to-speech systems.

For example:

* s.:syntynyt # ;  
* os.:omaa% sukua # ;  
* v.:vuosi # ;  
* v.:vuonna # ;  
* esim.:esimerkki # ; 
* esim.:esimerkiksi # ; 

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-abbrevs2text.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/transcriptions/transcriptor-abbrevs2text.lexc)</small>

---

# src-fst-transcriptions-transcriptor-numbers-digit2text.lexc.md 



% komma% :,      Root ;
% tjuohkkis% :%. Root ;
% kolon% :%:     Root ;
% sárggis% :%-   Root ; 
% násti% :%*     Root ; 

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-numbers-digit2text.lexc](https://github.com/giellalt/lang-tkl/blob/main/src/fst/transcriptions/transcriptor-numbers-digit2text.lexc)</small>

---

# tools-grammarcheckers-grammarchecker.cg3.md 


#  Tokelauan  G R A M M A R   C H E C K E R

# DELIMITERS

# TAGS AND SETS

## Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

### Beginning and end of sentence
BOS
EOS

### Parts of speech tags

N
A
Adv
V
Pron
CS
CC
CC-CS
Po
Pr
Pcle
Num
Interj
ABBR
ACR
CLB
LEFT
RIGHT
WEB
PPUNCT
PUNCT

COMMA
¶

### Tags for POS sub-categories

Pers
Dem
Interr
Indef
Recipr
Refl
Rel
Coll
NomAg
Prop
Allegro
Arab
Romertall

### Tags for morphosyntactic properties

Nom
Acc
Gen
Ill
Loc
Com
Ess
Ess
Sg
Du
Pl
Cmp/SplitR
Cmp/SgNom Cmp/SgGen
Cmp/SgGen
PxSg1
PxSg2
PxSg3
PxDu1
PxDu2
PxDu3
PxPl1
PxPl2
PxPl3
Px

Comp
Superl
Attr
Ord
Qst
IV
TV
Prt
Prs
Ind
Pot
Cond
Imprt
ImprtII
Sg1
Sg2
Sg3
Du1
Du2
Du3
Pl1
Pl2
Pl3
Inf
ConNeg
Neg
PrfPrc
VGen
PrsPrc
Ger
Sup
Actio
VAbess

Err/Orth

### Semantic tags

Sem/Act
Sem/Ani
Sem/Atr
Sem/Body
Sem/Clth
Sem/Domain
Sem/Feat-phys
Sem/Fem
Sem/Group
Sem/Lang
Sem/Mal
Sem/Measr
Sem/Money
Sem/Obj
Sem/Obj-el
Sem/Org
Sem/Perc-emo
Sem/Plc
Sem/Sign
Sem/State-sick
Sem/Sur
Sem/Time
Sem/Txt

HUMAN

PROP-ATTR
PROP-SUR

TIME-N-SET

###  Syntactic tags

@+FAUXV
@+FMAINV
@-FAUXV
@-FMAINV
@-FSUBJ>
@-F<OBJ
@-FOBJ>
@-FSPRED<OBJ
@-F<ADVL
@-FADVL>
@-F<SPRED
@-F<OPRED
@-FSPRED>
@-FOPRED>
@>ADVL
@ADVL<
@<ADVL
@ADVL>
@ADVL
@HAB>
@<HAB
@>N
@Interj
@N<
@>A
@P<
@>P
@HNOUN
@INTERJ
@>Num
@Pron<
@>Pron
@Num<
@OBJ
@<OBJ
@OBJ>
@OPRED
@<OPRED
@OPRED>
@PCLE
@COMP-CS<
@SPRED
@<SPRED
@SPRED>
@SUBJ
@<SUBJ
@SUBJ>
SUBJ
SPRED
OPRED
@PPRED
@APP
@APP-N<
@APP-Pron<
@APP>Pron
@APP-Num<
@APP-ADVL<
@VOC
@CVP
@CNP
OBJ
<OBJ
OBJ>
<OBJ-OTHERS
OBJ>-OTHERS
SYN-V
@X

## Sets containing sets of lists and tags

This part of the file lists a large number of sets based partly upon the tags defined above, and
partly upon lexemes drawn from the lexicon.
See the sourcefile itself to inspect the sets, what follows here is an overview of the set types.

### Sets for Single-word sets

INITIAL

### Sets for word or not

WORD
NOT-COMMA

### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

### Verb sets

NOT-V

### Sets for finiteness and mood

REAL-NEG

MOOD-V

NOT-PRFPRC

### Sets for person

SG1-V
SG2-V
SG3-V
DU1-V
DU2-V
DU3-V
PL1-V
PL2-V
PL3-V

### Pronoun sets

### Adjectival sets and their complements

### Adverbial sets and their complements

### Sets of elements with common syntactic behaviour

### NP sets defined according to their morphosyntactic features

### The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.

### Border sets and their complements

### Grammarchecker sets

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-tkl/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>

---

# tools-tokenisers-tokeniser-disamb-gt-desc.pmscript.md 

# Tokeniser for tkl

Usage:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1. unknown word-like forms, and
2. unmatched strings
We want to give 1) a match, but let 2) be treated specially by
`hfst-tokenise -a`
Unknowns are made of:
* lower-case ASCII
* upper-case ASCII
* select extended latin symbols
ASCII digits
* select symbols
* Combining diacritics as individual symbols,
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

## Unknown handling
Unknowns are tagged ?? and treated specially with `hfst-tokenise`
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-disamb-gt-desc.pmscript](https://github.com/giellalt/lang-tkl/blob/main/tools/tokenisers/tokeniser-disamb-gt-desc.pmscript)</small>

---

# tools-tokenisers-tokeniser-gramcheck-gt-desc.pmscript.md 

# Grammar checker tokenisation for tkl

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript](https://github.com/giellalt/lang-tkl/blob/main/tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript)</small>

---

# tools-tokenisers-tokeniser-tts-cggt-desc.pmscript.md 

# TTS tokenisation for smj

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```sh
make
echo "ja, ja" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```sh
echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa \
boasttu olmmoš, man mielde lahtuid." \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "márffibiillagáffe" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://kitwiki.csc.fi/twiki/bin/view/KitWiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Needs hfst-tokenise to output things differently depending on the tag they get

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-tts-cggt-desc.pmscript](https://github.com/giellalt/lang-tkl/blob/main/tools/tokenisers/tokeniser-tts-cggt-desc.pmscript)</small>
