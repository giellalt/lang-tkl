Test diary
==========


## Lexical coverage 

(testing on different conversion versions of the nt)

Number of words (standing in `lang-tkl`):

```
cat misc/nt_tkl.txt |hfst-tokenise -m tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |wc -l
cat misc/nt.tkl.txt |tr -d "[0-9]"|hfst-tokenise -m tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |wc -l
```

Number of unknown words:


```
cat misc/nt_tkl.txt |hfst-tokenise -mgW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |grep ' ?'|wc -l
cat misc/nt.tkl.txt |tr -d "[0-9]"|hfst-tokenise -mgW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |grep " ?"|wc -l
```

### Lexical coverage nt


Coverage, NT:

```
241115: 1-(34193/351080) = 0.9026
241115: 1-(30018/350323) = 0.9143
241117: 1-(17098/350323) = 0.9512
241201: 1-(14505/320561) = 0.9548
241209: 1-(11008/320540) = 0.9656
```

Coverage, book collection:

```
        All words                      Not words with initial capital
241210: 1-(6868/62281) = 0.8897        1-(4549/44442) = 0.8976
```


## Disambiguation

Assuming the disambiguation is correct:

Number of words in the test corpus:

```
cat misc/nt2.txt |hfst-tokenise tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |wc -l
```


Number of readings in the test corpus:

```
cat misc/nt2.txt |hfst-tokenise -gmW tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |vislcg3 -g src/cg3/disambiguator.cg3|grep -v '^[":]'|wc -l
```

Number of readings per word:

Without disambiguation, the number of readings is 1.835 per word (601788/327949)

With disambiguation:

```
241202: 408241/327949 = 1.24483
241202: 391579/327949 = 1.19402
241209: 383837/327928 = 1.17049
```
  
  




