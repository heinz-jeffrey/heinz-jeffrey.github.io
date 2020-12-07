First create your grammar in a text file using vim or nano or txt or whatever your preference. Save it as <name>.cfg    
    
If you don't have NLTK you can download it online.

In the console you’ll import nltk and load your grammar like this: 
    gram = nltk.data.load("file:<name>.cfg")
where <name> is your cfg file.  You can also do this from a string like this:



```python
import nltk
gram = nltk.CFG.fromstring("""
    TP -> DP T1
    TP -> T1
    T1 -> T VP
    VP -> V1
    VP -> V1 PP
    NP -> N1
    N1 -> AdjP N1
    N1 -> N
    N1 -> N PP
    V1 -> V DP
    DP -> D1
    D1 -> D NP
    D1 -> NP
    PP -> P DP
    AdjP -> Adj1
    Adj1 -> Adj
    Adj1 -> Adj AdjP
    T -> 
    V -> 'ate'
    V -> 'saw'
    V -> 'walked'
    V -> 
    N -> 'Kelsey'
    N -> 'Victoria'
    N -> 'dog'
    N -> 'cat'
    N -> 'pizza'
    N -> 'park'
    N -> 'rain'
    D -> 'the'
    D -> 'a'
    D -> 'an'
    Adj -> 'big'
    Adj -> 'yellow'
    Adj -> 'round'
    Adj -> 'red'
    P -> 'of'
    P -> 'in'
    P -> 'at'
    P -> 'around'
    """)

print (gram)  # print to make sure it’s correct

```

    Grammar with 40 productions (start state = TP)
        TP -> DP T1
        TP -> T1
        T1 -> T VP
        VP -> V1
        VP -> V1 PP
        NP -> N1
        N1 -> AdjP N1
        N1 -> N
        N1 -> N PP
        V1 -> V DP
        DP -> D1
        D1 -> D NP
        D1 -> NP
        PP -> P DP
        AdjP -> Adj1
        Adj1 -> Adj
        Adj1 -> Adj AdjP
        T -> 
        V -> 'ate'
        V -> 'saw'
        V -> 'walked'
        V -> 
        N -> 'Kelsey'
        N -> 'Victoria'
        N -> 'dog'
        N -> 'cat'
        N -> 'pizza'
        N -> 'park'
        N -> 'rain'
        D -> 'the'
        D -> 'a'
        D -> 'an'
        Adj -> 'big'
        Adj -> 'yellow'
        Adj -> 'round'
        Adj -> 'red'
        P -> 'of'
        P -> 'in'
        P -> 'at'
        P -> 'around'



```python
# name the parser you’re going to use : Recursive descent / chart
rd = nltk.RecursiveDescentParser(gram)

# make a sentence given your grammar’s lexicon
sent = "Kelsey walked the big dog".split()#parse tree and print it
for tree in rd.parse(sent):
    print(tree)

# draw the visual tree
tree.draw()
```

    (TP
      (DP (D1 (NP (N1 (N Kelsey)))))
      (T1
        (T )
        (VP
          (V1
            (V walked)
            (DP
              (D1 (D the) (NP (N1 (AdjP (Adj1 (Adj big))) (N1 (N dog))))))))))


If you want to use the Recursive Descent parser app, just type
nltk.app.rdparser() into the console and press enter. In the app you can edit the existing grammar and lexicon, or paste in your existing grammar. This is a top-down parser.
Choose sentences from your grammar to parse. This app shows exactly what the parser does step by step. Starting with your root node S (or whatever you made it), the parser will go through your entire grammar productions 1 by 1 until it finds the matching word. Once it finds the matching word it will move on to the search for the correct productions for the next word, until the entire sentence as been matched or fails.

# Ambiguity example


```python
ch = nltk.ChartParser(gram)
sent2 = "Victoria saw a cat in the rain".split()

for tree2 in ch.parse(sent2):
    print(tree2)

```

    (TP
      (DP (D1 (NP (N1 (N Victoria)))))
      (T1
        (T )
        (VP
          (V1 (V saw) (DP (D1 (D a) (NP (N1 (N cat))))))
          (PP (P in) (DP (D1 (D the) (NP (N1 (N rain)))))))))
    (TP
      (DP (D1 (NP (N1 (N Victoria)))))
      (T1
        (T )
        (VP
          (V1
            (V saw)
            (DP
              (D1
                (D a)
                (NP
                  (N1
                    (N cat)
                    (PP (P in) (DP (D1 (D the) (NP (N1 (N rain))))))))))))))


You can see there are two possible ways this tree can be parsed: 

One where the PP attaches to the VP, and one where the PP attaches to the NP(cat)
So Victoria either saw a cat while she was in the rain, or she saw a cat while the cat was in the rain.

To get a visual representation of each tree, you need to create a generator object for the sentence, then re-render the object as a list. Check the length of the list so you know it's correct, then you can print each tree using the indexes of the list.


```python
mytrees = ch.parse(sent2)
mytrees = list(mytrees)
len(mytrees)
mytrees[0].draw()

```


```python
mytrees[1].draw()
```

We didn't get to do this in class but here is a tangible example of PCFG in NLTK.
First you need a PCFG, or create one. I'm just making this up out of my pizzaCatgrammar. The sum of each Lefthand node needs to = 1.0.


```python
pg = nltk.PCFG.fromstring("""
    TP -> DP T1      [1.0]
    T1 -> VP       [1.0]
    VP -> V1         [0.4]
    VP -> V1 PP      [0.6]
    NP -> N1         [1.0]
    N1 -> AdjP N1    [0.3]  
    N1 -> N          [0.4]
    N1 -> N PP       [0.3]
    V1 -> V DP       [0.6]
    V1 -> V          [0.4]
    DP -> D1         [1.0]
    D1 -> D NP       [0.6]
    D1 -> NP         [0.4]
    PP -> P DP       [1.0]
    AdjP -> Adj1     [1.0]
    Adj1 -> Adj      [0.7]
    Adj1 -> Adj AdjP [0.3]
    V -> 'ate'       [0.3]
    V -> 'saw'       [0.4]
    V -> 'walked'    [0.3]
    N -> 'Kelsey'    [0.1]
    N -> 'Victoria'  [0.1]
    N -> 'dog'       [0.2]
    N -> 'cat'       [0.2]
    N -> 'pizza'     [0.2]
    N -> 'park'      [0.1]
    N -> 'rain'      [0.1]
    D -> 'the'       [0.4]
    D -> 'a'         [0.3]
    D -> 'an'        [0.3]
    Adj -> 'big'     [0.3]
    Adj -> 'yellow'  [0.2]
    Adj -> 'round'   [0.2]
    Adj -> 'red'     [0.3]
    P -> 'of'        [0.3]
    P -> 'in'        [0.2]
    P -> 'at'        [0.3]
    P -> 'around'    [0.2]     
    """)

print(pg)
```

    Grammar with 38 productions (start state = TP)
        TP -> DP T1 [1.0]
        T1 -> VP [1.0]
        VP -> V1 [0.4]
        VP -> V1 PP [0.6]
        NP -> N1 [1.0]
        N1 -> AdjP N1 [0.3]
        N1 -> N [0.4]
        N1 -> N PP [0.3]
        V1 -> V DP [0.6]
        V1 -> V [0.4]
        DP -> D1 [1.0]
        D1 -> D NP [0.6]
        D1 -> NP [0.4]
        PP -> P DP [1.0]
        AdjP -> Adj1 [1.0]
        Adj1 -> Adj [0.7]
        Adj1 -> Adj AdjP [0.3]
        V -> 'ate' [0.3]
        V -> 'saw' [0.4]
        V -> 'walked' [0.3]
        N -> 'Kelsey' [0.1]
        N -> 'Victoria' [0.1]
        N -> 'dog' [0.2]
        N -> 'cat' [0.2]
        N -> 'pizza' [0.2]
        N -> 'park' [0.1]
        N -> 'rain' [0.1]
        D -> 'the' [0.4]
        D -> 'a' [0.3]
        D -> 'an' [0.3]
        Adj -> 'big' [0.3]
        Adj -> 'yellow' [0.2]
        Adj -> 'round' [0.2]
        Adj -> 'red' [0.3]
        P -> 'of' [0.3]
        P -> 'in' [0.2]
        P -> 'at' [0.3]
        P -> 'around' [0.2]


The Viterbi Parser is a bottom-up PCFG parser that uses dynamic programming to find the most likely parse for a sentence. It parses texts by filling in a "most likely constituent table," which records the most probable tree representation. 


```python
vit = nltk.ViterbiParser(pg)
newSent = "the cat ate the dog".split() #ignore capitalization here
for tree in vit.parse(newSent):
    print(tree)
newSent2 = "Kelsey walked the big red dog in the park".split()
for tree1 in vit.parse(newSent2):
    print(tree1)
```

    (TP
      (DP (D1 (D the) (NP (N1 (N cat)))))
      (T1
        (VP (V1 (V ate) (DP (D1 (D the) (NP (N1 (N dog))))))))) (p=2.65421e-05)
    (TP
      (DP (D1 (NP (N1 (N Kelsey)))))
      (T1
        (VP
          (V1
            (V walked)
            (DP
              (D1
                (D the)
                (NP
                  (N1
                    (AdjP
                      (Adj1 (Adj big) (AdjP (Adj1 (Adj red)))))
                    (N1 (N dog)))))))
          (PP (P in) (DP (D1 (D the) (NP (N1 (N park))))))))) (p=3.61185e-10)


The probability of tree is 2.65421e-05, and the probability of tree1 is 3.61185e-10
Since newSent2 is ambiguous, the parser picked the most probable derivation.
