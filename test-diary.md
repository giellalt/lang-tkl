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

```






