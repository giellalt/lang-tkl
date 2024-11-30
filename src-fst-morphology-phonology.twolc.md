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
