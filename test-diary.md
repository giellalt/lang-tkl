Test diary
==========


## Lexical coverage 

Number of words (standing in `lang-tkl`):

```
cat misc/nt_tkl.txt |hfst-tokenise -mgW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |grep ' ?'|wc -l
```

Number of unknown words:


```
cat misc/nt_tkl.txt |hfst-tokenise -m tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |wc -l
```

### Lexical coverage nt


Coverage:

```
241115: 1-(34193/351080) = 0.9026
241115: 1-(30018/350323) = 0.9143
241117: 1-(17098/350323) = 0.9512
```


## Disambiguation

Assuming the disambiguation is correct:

Number of words in the test corpus:

`cat misc/nt2.txt|hfst-tokenise -gmW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |vislcg3 -g src/cg3/disambiguator.cg3 |grep -v "^:"|grep -v "^$"|wc -l`


Number of readings and words in the test corpus:

`cat misc/nt2.txt|hfst-tokenise -gmW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |vislcg3 -g src/cg3/disambiguator.cg3 |grep -v "^:"|grep -v "^$"|grep '^"'|wc -l`

Number of readings per word:

241130: (721729-317150)/317150 = 1.27567





