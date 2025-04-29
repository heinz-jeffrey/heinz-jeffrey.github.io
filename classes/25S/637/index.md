% Computational Linguistics 2 (LIN 637, Spring 2025)

# Course Information

**Course:** TThu 14:00-15:20, SBS N250 (or compling lab)

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/),
[jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours: Tuesday 11:30-1pm, Wednesday 2pm-3:30pm and by appointment**

# Materials

* [Syllabus](materials/LIN637_Syllabus_Spring2025.pdf)

# Course Log

## 28 Apr

* We discussed the problem of learning finite-state machines.
  - State merging. See chapter 3 of [this
    book](materials/GIFCL2015.pdf)
  - Learning Tree Languages. See chapter 7 of [this
    book](materials/TGI2016.pdf).
  - Learning deterministic, structured classes.
    - Path following in acceptors [Heinz and Rogers
      2013](http://jeffreyheinz.net/papers/Heinz-Rogers-2013-LSCLFDA.pdf)
    - Path following + lcp for transducers [Jardine et
      al. 2014](http://jeffreyheinz.net/papers/Jardine-ChandleeEtAl-2014-VELSCSFPD.pdf)
* Course review.

## 24 Apr

* We noted one more item about composition.
  - Application as composition.
  - For rational relations, this gives us a way to represent
    infinitely many outputs with a single input.
  - [Roark and Sproat 2007](materials/Roark-Sproat2008Comp.pdf)
    highlight the importance of composition in grammar construction
    and analysis.
  - Example in pynini: [English Plurals](materials/EngPlurals.py)
* Another way to factor complex functions is with the *direct
  product*. Direct products hold for algebraic varieties (like
  k-definiteness). We discussed this in the context of phonological
  features and Magda's dissertation research.
* An additional paper with potentially challenging long-distance
  transformations: [Gleim and Schneider
  2023](materials/GleimSchneider2023.pdf)

## 22 Apr

* We talked a bit about the classification exercise.
* We discussed topics related to non-determinism.
  - Inversion
  - Semirings (see Mohri's 2009 chapter on [Weighted Automata
    Algorithms](https://cs.nyu.edu/~mohri/transducer-algorithms.html)).
* We discussed the last two weeks of classes.

## 17 Apr

* main lesson: Life is precious. Don't sweat the small stuff.
* We talked about the role of composition in the construction of morpho-phonological finite-systems.
* We talked about the rol of composition in the construction of
  compilers of rewrite rules into finite-state transducers. (See
  [Mohri and Sproat 1996](materials/MohriSproat1996.pdf) for details.)
* Here are [instructions](materials/minimize.html) on how to take a
  transducer in ATT format, prepare it for classification, and then
  classify it with plebby.

## 15 Apr

* We studied function composition with transducers.
* We studied other closure operations of regular relations and
  functions.

## 10 Apr

* We realized that the right FST in Figure 6 in Burness et al. 2021 is
  not the minimum FST. The minimum one is here:
  [att](fig6rightmin.att).

  ```$ classify -N TDef TRDef < fig6rightmin.att
     [ ("TDef",True)
     , ("TRDef",True)
     ]
  ```
* We discussed that unless we are sure that the DFT we have is
  minimal, we should do our best to minimize it.
  - In pynini of pyfoma, we would want to read in an ATT file,
    minimize it, and then output a new ATT file which can be sent to
    `classify`.

* We discussed some of the differences between the FST libraries.

## 08 Apr

* We reviewed the Myhill relation and construction of the syntactic
  monoid from minimal DFTs.
* We saw how to use the classify program in
  [LTK](https://github.com/vvulpes0/Language-Toolkit-2) to classify
  transducers
  - [classify man page](materials/classify-man.txt)
  - Example. Figure 6 in [Burness et al. 2021](https://www.glossa-journal.org/article/id/5780/)
  - [att](fig6right.att)  [syms](materials/syms-fig6.txt)


## 03 Apr

* We reviewed deterministic top-down tree transducers.
* We discussed their expressivity re bottom-up ones.
* We discussed Lambert and Heinz 2023, in particular:
  - What the Nerode and Myhill relations mean for string-to-string functions
  - What the minimal, deterministic, onward transducer is
  - How to obtain the syntactic monoid from that
  - And then algebraic analysis is the same as before!
* Don't forget proposals are supposed to be approved by next Friday.
* For next Tuesday, choose one process discussed in [Burness et
  al. 2019, sections 5 and
  6](https://www.glossa-journal.org/article/id/5780/), or for a
  challenge, choose a FST used in NLP such as a
  [tokenizer](https://github.com/cslu-nlp/DetectorMorse/blob/master/detectormorse/ptbtokenizer.py),
  [stemmer](https://snowballstem.org/), or [G2P,
  P2G](https://dmort27.github.io/subwordmodeling/assignments/project3.html),
  something with [epitran](https://github.com/dmort27/epitran), etc.

## 01 Apr

* We reviewed 1-way, string-to-M transducers for an arbitrary monoid M.
* We defined 1-way non-deterministic letter-to-letter transducers.
* We defined 2-way transducers (see [Dolatian and Heinz
  2020](Dolatian-Heinz-2020-CCR2FT.pdf) for application to
  reduplication).
* We identified five classes of interest: 1DFT  ⊂ 1fNFT  ⊂ 1NFT, 2DFT ⊂ 2NFT
  - 1 means "1 way" and 2 mean "2 way"
  - D means "deterministic" and N means "non-deterministic"
  - f means "functional"
  - FT means "finite-state transducer"
* Compare with finite-state acceptors: 1DFA = 1NFA = 2DFA = 2NFA.
* Note also 1DFTs come in two varieties (left and right).
* We discussed (but little to no details provided) minimization and composition of FTs.
* For Thursday, read [Lambert and Heinz 2023](materials/Lambert-Heinz-2023-ACISLF.pdf).

## 27 Mar

* We reviewed deterministic bottom-up tree transducers.
* We generalized deterministic string-to-string transducers to
  string-to-M transducers for an arbitrary monoid M.
* We discussed the landscape of classes of finite-state string
  transducers.
  - Additional Reading: [Filiot and Reynier
    2016](materials/FiliotReynier2016.pdf)
* Some libraries for finite-state transducers
  - [openfst](https://www.openfst.org/) and
    [pynini](https://www.openfst.org/twiki/bin/view/GRM/Pynini)
  - [foma](https://fomafst.github.io/) and
    [pyfoma](https://github.com/mhulden/pyfoma)
  - [Helsinki Finite-State Technology](https://github.com/HFST/HFST)
  - Nick Behrje's [tree transducer
    library](https://github.com/nbehrje/tree_transducer)
  - The [Lethal tree transducer
    toolkit](https://lethal.sourceforge.net/)

## 25 Mar

* Today we began discussing finite-state transducers for both strings
  and trees. We went over the first parts of both chapter 6 and 7 in
  [these notes](materials/TCL-FSA.pdf).

## 18-20 Mar

* SPRING BREAK

## 13 Mar

* We showed that culminativity is neither definite nor reverse definite.
* We defined generalized definite and nilpotent (co/finite) languages
  and the equations that characterize them.
* We were interrupted by a fire alarm.
* We studied tier-based and multi-tier based extensions of classes of
  formal languages and algebraic characterizations of them.
* We see multiple characterizations of culminativity (for instance
  both SP and TN).
* During break:
  - Please read all of [Lambert,
  forthcoming](materials/Lambert-2025-Multier-Phonotactics.pdf).
  - Examine the associated [plebby
    files](materials/Lambert-2025-Multier-Phonotactics-extras.zip).

## 11 Mar

* We reviewed the algebraic analysis of "stress penult without
  culminativity."
* We explained how the semigroup can also be represented with a Myhill
  Graph (which is a DFA whose states represent blocks in a partition
  which refines than the partition given by the Nerode relation.)
* We reviewed the analysis from the HW "stress peninitial without
    culminativity."
* We reviewed reverse definite languages and the equations that
  characterize them.

## 06 Mar

* We began discussing the algebraic approach to analysis of formal languages.
  - We explained how to obtain the elements of finite semigroup from a
    DFA by identifying the 'actions' each symbol, or sequence of
    symbols, induces on the DFA.
  - We explained how that semigroup can be represented with a
    concatentation table (Cayley table).
  - We defined k-definite languages using grammars, and showed how the
    elements of a semigroup for k-definite languages, and definite
    languages more generally satisfy particular equations.
  - Homework for Tuesday: determine the DFA, semigroup elements
    (actions), and the Cayley table for stress-peninitial without
    culminativity.

## 04 Mar

* We reviewed a definition of Strictly k-Local tree languages in terms
  of "tiling" trees of depth k. We saw how the derivation tree
  language of any CFG is a SL-2 tree language.
* We discussed Theorem 18 on page 56 of the course notes.
* Switching gears, we began talking about the Myhill Equivalence
  relations, using section 6 of [Lambert,
  forthcoming](materials/Lambert-2025-Multier-Phonotactics.pdf) as our
  guide.
* For Thursday, please read section 6 up to section 6.2.1, but not
  including 6.2.1. (so bottom of page 24 to top of page 29)

## 27 Feb

* We reviewed deterministic, bottom-up and top-down finite state
  recognizers for tree languages.
* We talked about the gorn addresses in a tree and definitions of
  trees as prefix-closed sets.
* We defined rewrite grammars, and examined right-linear, left-linear
  and context-free grammars.
* We examined the derivation trees of CFGs in light of recognizable
  tree languages.

## 25 Feb

* We defined deterministic, bottom-up tree acceptors and looked at
  some examples of how they work.
* We defined deterministic, top-down tree acceptors and looked at some
  examples of how they work.
* We discussed the expressivity of non-deterministic BU and TD
  acceptors with respect to the deterministic ones.
* We discussed how they are recognizable tree languages are closed
  under intersection and union. They are not closed under complement
  with respect to Σᵀ, but they are closed under complement with
  respect to Σᵀⁿ, where n is the maximum branching factor.

## 20 Feb

* We defined strings and trees as recursive data structures.
* We showed how computations over trees such as length, size, and
  yield, have the same structure as their inputs.
* We began defining bottom-up tree acceptors.

## 18 Feb

* We discussed how to minimize DFA (identifying
  distinguishable states).
* We introduced the Nerode equivalence relation.
* We related the minimal DFA to this equivalence relation.

## 13 Feb

* We reviewed some more of plebby's features [pleb.txt](materials/pleb.txt).
* We explained how to determinize NFA (powerset construction). For a
  proof, see pages 54-56 in [Chapter
  1](materials/Sipser2013Chaps0-1.pdf) of Sipser's 2012 text.  See
  [Kozen1997](materials/Kozen1997.pdf) Chapter 6 for a more
  technically complete proof.
* On Tuesday we will discuss how to minimize DFA (identifying
  distinguishable states) and we will relate this minimal DFA to the
  Nerode equivalence relation.

## 11 Feb

* We sketched how to obtain a RE from a NFA. See pages 66-76 in
  [Chapter 1](materials/Sipser2013Chaps0-1.pdf) of Sipser's 2012 text.
* We showed why NFA are closed under complement, intersection, and
  difference.
* Using those facts, and the notion of reachable states, we showed we
  can decide whether one regular language is a subset of another.  And
  then we can decide whether two regular languages are equal.
* We played with plebby. [pleb.txt](materials/pleb.txt)
* For Thursday, see if you can get the visualization (graphviz)
  installed. Also see if you can write PLEs for #12 and #13 in Example
  1 in the course notes.

## 06 Feb

* We looked at this [supplement](materials/nfadfa-supplement.pdf),
  which defines NFA and DFA and how they process strings from a
  non-recursive perspective. (This will change.)
* We discussed how to visualize NFA and DFA as graphs.
* We sketched how any RE can be expressed as a NFA because the base
  cases correspond to NFA and the inductive cases correspond to
  particular constructions.
* We demonstrated plebby and its PLEs.
* For Tuesday, please install plebby, and examine its tutorial,
  especially the section titled "Building a Linguistic Pattern".

## 04 Feb

* We defined and discussed CUEs, GREs, and SFEs and stated the facts
  (without proof) that
  - [[GREs]] = [[REs]] ⊃ [[SFEs]] ⊃ [[CUEs]] = FIN
  - even-a is a formal language expressible with REs but not SFEs
  - Regular languages and SFEs have other characterizations in terms
    of logic and algebra
  - This material is the subject of [McNaughton and Papert
    1971](https://archive.org/details/CounterFre_00_McNa/)
* We also defined Dakotah's Lambert's Piecewise Local Expressions,
  which we will study further on Thursday.
  - The LTK software:
    [Git](https://github.com/vvulpes0/Language-Toolkit-2)
    [Hackage](https://hackage.haskell.org/package/language-toolkit)
  - [Lambert 2024 paper about the software](materials/Lambert2024.pdf)
- Theorem 6 in [this
  paper](https://www.jeffreyheinz.net/papers/Heinz-RawalEtAl-2011-TSLCP.pdf)
  establishes that Tier-based Strictly Local languages are a subset of
  the Star-Free Languages. That they are a proper subset follows from
  Theorems 4 and 5.

## 30 Jan 2025

* We discussed concatenation, how to define formal grammars, and REs in Chapter 2.
* For Tuesday, write a RE for the set containing all strings which do
  not contain the sequence aa (assume the alphabet is {a, b, c}).

## 28 Jan 2025

* We went over the [syllabus](materials/LIN637_Syllabus_Spring2025.pdf).
* We discussed Chapter 1 and began Chapter 2 of the [course's lecture
  notes](materials/TCL-FSA.pdf).

-------------------------------------------------------------------------------
