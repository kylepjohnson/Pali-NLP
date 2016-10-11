# Stemmer

The stemmer outputs the stemme version of an input pali sentence. The API is Pali-NLP/Stemmer/wordClassStemmer.stem()  

```python
In [1]: import wordClassStemmer

In [2]: sentence = 'Eva.m me suta.m - eka.m samaya.m bhagavaa antaraa ca raajagaha
   ...: .m antaraa ca naa.landa.m addhaanamaggappa.tipanno hoti mahataa bhikkhus
   ...: a"nghena saddhi.m pa~ncamattehi bhikkhusatehi. Suppiyopi kho paribbaajak
   ...: o antaraa ca raajagaha.m antaraa ca naa.landa.m addhaanamaggappa.tipanno
   ...:  hoti saddhi.m antevaasinaa brahmadattena maa.navena.'

In [3]: wordClassStemmer.stem(sentence)
Out[3]: 'Ev  sut - samay bhagav antar c raajagah antar c naa.land addhaanamaggappa.tipann hot mahat bhikkhusa"ngh saddhi.m pa~ncamatt bhikkhusatehi. Suppiyop kh paribbaajak antar c raajagah antar c naa.land addhaanamaggappa.tipann hot saddhi.m antevaasin brahmadatt maa.navena.'```


The process involves a few steps. 

The word class (noun, verb, adj....) of the input word is checked first.
The same word may belong to multiple word classes.
Hence a list of possibilities is returned. 

If no possibilities are identified, the ending of given word is compared with all 
available word endings and if matched, it is removed. This process is carried 
out recursively. 

If word class is identified, we consider each word class separately. 
Lists of endings for each word class are generated separately, and those endings
are compared with the word. If matching, the word is stemmed.
A list of possible stems is returned. Mostly, each separate case returns the same
stem. This method improves accuracy of stemming.  

