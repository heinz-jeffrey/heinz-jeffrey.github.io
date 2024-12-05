% Computational Phonology (LIN 655)

# Course Information

**Course:** TThu 09:30-10:50, Compling lab

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/), [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours: Mondays 2-5pm and by appointment**

# Materials

* [Syllabus](materials/LIN655_Syllabus_Fall2024.pdf)

# Course Log

## 05 Dec 2024

* We reviewed the class and discussed open questions.
* [board left](materials/boardleft.jpeg)
* [board right](materials/boardright.jpeg)


## 03 Dec 2024

* Today we discussed the quality of the characteristic sample for
  [SOSFIA](https://www.jeffreyheinz.net/papers/Jardine-ChandleeEtAl-2014-VELSCSFPD.pdf), as well as the [OSL learning algorithm](https://www.jeffreyheinz.net/papers/Chandlee-EyraudEtAl-2015-OSLF.pdf).

* We briefly mentioned the [Burness and McMullin](materials/burnessmcmullin2019.pdf) method for inducing
  tiers to to tier-based OSL functions. 

## 28 Nov 2024

* Thanksgiving Holiday. No Class.

## 26 Nov 2024

* Today we discussed the SOSFIA paper using the [presentation from ICGI 2014](http://jeffreyheinz.net/talks/Jardine-ChandleeEtAl-2014-VELSCSFPD-slides.pdf).

## 21 Nov 2024

* Today we discussed learning tradeoffs in the context of transducer
  learning.

  | Algortithm |   | Class it learns              |   | Time Complexity |
  |:-----------|---|------------------------------|---|-----------------|
  | OSTIA      |   | subsequential (DFTs)         |   | O(n^3^)         |
  | ISLFLA     |   | ISL (definite DFTs)          |   | O(n^2^)         |
  | OSLFIA     |   | OSL                          |   | O(n^2^)         |
  | SOSFIA     |   | any class given by fixed DFT |   | O(n^1^)         |

  Smaller, more well-structured learning classes can make learning
  easier. The subregular program aims to find classes of patterns
  which are both sufficiently expressive to describe natural language
  patterns and which are sufficiently structured to enable learning
  from small data.

* [OSTIA](materials/Oncina-et-al-1993-OSTIA.pdf) and
  [ISLFLA](http://jeffreyheinz.net/papers/Chandlee-EyraudEtAl-2014-LSLSF.pdf)
  are start merging algorithms (builds a prefix tree of the sample and
  then collapses
  states). [OSLFLA](https://www.jeffreyheinz.net/papers/Chandlee-EyraudEtAl-2015-OSLF.pdf)
  draws the transitions into the DFT from the start state
  outwards. [SOSFIA](https://www.jeffreyheinz.net/papers/Jardine-ChandleeEtAl-2014-VELSCSFPD.pdf)
  recognizes that the state space and transitions are fixed and aims
  to fill in what is unknown, which is just the outputs on the
  transitions.

* SOSFIA cannot be used to learn the OSL class since OSL is not fixed
  by a DFT, unlike ISL-k. Many OSL functions are also (tier-based)
  reverse definite functions which can be represented by a fixed DFT
  [Lambert and Heinz
  2024](https://openpublishing.library.umass.edu/scil/article/id/2137/). Anton
  points out these cannot handle blocking. Perhaps the blocking
  patterns are generalized definite?

* We also discussed [Gildea and Jurafsky's
  1996](materials/GildeaJurafsky1996.pdf) application of OSTIA to
  English flapping.

* On Tuesday we will study how SOSFIA works.

## 19 Nov 2024

* Today we discussed [Burness et al. 2019 "Long-distance phonological
  processes as tier-based strictly local
  functions"](https://www.glossa-journal.org/article/id/5780/).
  - We reviewed SL formal languages and defined TSL formal
    languages. We observed that neutral letters (non-tier letters) can
    be added or subtracted anywhere to any word without impacting its
    membership status in the language. In finite-state terms, that
    means neutral letters never change state. They are self-loops. Any
    class of stringsets can be "tierified" ([Lambert
    2023](https://doi.org/10.1007/s10849-023-09398-x)).
  - We reviewed ISL and defined OSL functions. We saw why iterative
    nasal spreading is not ISL but is OSL.
  - We examined why sequential functions admit functions sensitive to
    parity.
  - We saw how Burness et al. tierify the ISL and OSL classes, and why
    they argued that Tier ISL cannot express long-distance sibilant
    harmony but Tier OSL can.
  - We quickly acknowledged their treatment of more complex cases of
    long-distance functions that they showed to be T-OSL, and also
    quickly acknowledged the limitations they observed.
  - On Thursday, more learning!
  
## 14 Nov 2024

* Today we decided to discuss order preservation in string maps. We
  learned:
  - with precedence (<) and FO it is straightforward:
    - <(c,d)(x,y) := x<y  (when c <= d)
    - <(c,d)(x,y) := x<=y (when d < c)
  - with successor (S) and FO it is not possible because unbounded
    spans in an input may delete.
    - Consider one copy: S(x,y) := xSy OR (Ex z1)[ x S z1 S y AND NOT
      lic(z1) ] OR (Ex z1,z2)[ x S z1 S z2 S y AND NOT lic(z1) AND NOT
      lic(z2)] OR .. (Ex z1,z2, .. zn)[ x S z1 S z2 S .. zn S y AND
      NOT lic(z1) AND NOT lic(z1) AND .. NOT lic(zn)]. The number of
      variables is bounded by some n but the input string can be
      longer than this n. Recall Chandlee and Lindell relate this idea
      to finite-to-one maps.
  - In summary, order-preserving maps with FO(S) entail finite-to-one
    maps. Those entail partial functions since total functions may
    delete spans of unbounded length. (Consider C+V mapping to CV
    given by the OT grammar *ComplexOnset>>Max.)
  - Are there spans of unbounded deletion in phonology? Truncation
    comes close, but some truncation is clearly Reverse Definite. Ola
    mentioned truncation in Yoruba in the middle of words. We should
    look at that.
* For Tuesday, read [Burness et al. 2019 "Long-distance phonological
  processes as tier-based strictly local
  functions"](https://www.glossa-journal.org/article/id/5780/). We
  will discuss then.
  - Note there is an error in Figure 6 in Burness et al. the
    transition from > state [s] to [ʃ] with the transition labeled ʃ:ʃ
    should instead be from > state [s] to [s] with label ʃ:s.
* Tier-based OSL functions are deterministic, but do not have a fixed
  structure. This paper shows that the long-distance processes belong
  to classes which have a fixed, deterministic structure: [Lambert and
  Heinz (2024) "Algebraic Reanalysis of Phonological Processes
  Described as
  Output-Oriented"](https://openpublishing.library.umass.edu/scil/article/id/2137/)
  The classes are the (left and right) reverse definite.
  - The algebraic analysis in this paper is technical. The heart of it
  though comes from the notion of Myhill equivalence. Lambert (under
  review) describes it this way: "In phonology, we often use minimal
  pairs to determine whether two phones represent distinct
  phonemes. For instance, Finnish has contrastive length on both
  vowels and consonants as demonstrated by the words [tːuli] ‘fire’,
  [t̪uːli] ‘wind’ and [t̪ulːi] ‘customs’, differing only in length. The
  t̪\_li environment distinguishes [u] from [uː], and the t̪u\_i
  environment distinguishes [l] from [lː]. In algebra, we do the same
  thing, except that rather than looking for differences in meaning,
  we seek differences in acceptability.  Given arbitrary strings 𝑥 and
  𝑦, we seek an environment 𝑢\_𝑣 where 𝑢𝑥𝑣 is accepted and 𝑢𝑦𝑣 is
  rejected, or vice versa. If such an environment can be found, then 𝑥
  and 𝑦 are distinct (Rabin & Scott, 1959). Otherwise, they are
  Myhill-equivalent with respect to the language." This is for sets of
  strings; for string maps, it's the same idea but takes into account
  output behavior as well.
  - We do not need to read this one for Tuesday, but I will mention it.
* On Thursday, we will discuss the importance of determinism for
  learning.

## 12 Nov 2024

* Anton presents on BMRS.
* [Ideas for final projects](materials/ideas.pdf) if you are still looking.

## 07 Nov 2024

* Jack presents on reduplication with 2 way transducers.

## 05 Nov 2024

* Class Canceled. Office Hour by
  [Zoom](https://stonybrook.zoom.us/my/jeffreyheinz) to catch up and
  ask questions if needed.

## 31 Oct 2024

* We discussed ISL functions, ISL transductions, and QF(succ,pred) functions.
* Here is the draft chapter of ["Logical Perspectives on Strictly Local
  Transformations"](materials/dcpChap22.pdf) by Chandlee and Lindell.

## 29 Oct 2024

* Using this [handout](materials/learning2.pdf), we formally
  introduced two learning criteria: identification in the limit from
  positive data and PAC.
* We discussed compared the two frameworks and thought about what
  choices in a learning criterion make it easier or harder.
* Supporting reading material: ["Computational Theories of Learning
  and Developmental Psycholinguistics" (Heinz
  2016)](http://jeffreyheinz.net/papers/Heinz-2016-CTLDP.pdf)
* Please read ["Strict Locality and Phonological Maps" (Chandlee and
  Heinz
  2018)](http://jeffreyheinz.net/papers/Chandlee-Heinz-2018-SLPM.pdf)
  for Thursday.
* Also, we had some discussion about computable and noncomputable real
 numbers. This [recent summary from the
 ACM](https://mathvoices.ams.org/featurecolumn/2021/12/01/alan-turing-computable-numbers/)
 reviews some of the issues. This paper ["How real are real
 numbers"](https://arxiv.org/pdf/math/0411418) is a bit more in depth.


## 24 Oct 2024

* We continued our discussion of learning problems, and developed one
  related to learning strictly k-local languages. Those techniques
  have been generalized and developed in the papers [String Extension
  Learning](http://www.aclweb.org/anthology/P10-1092) and [Learning
  with Lattice-Structured Hypothesis
  Spaces](https://www.sciencedirect.com/science/article/pii/S0304397512007128). See
  also [Typology emerges from simplicity in representations and
  learning](https://jlm.ipipan.waw.pl/index.php/JLM/article/view/262).

* On November 7, Jack will present [Computing and classifying
  reduplication with 2-way finite-state
  transducers](https://jlm.ipipan.waw.pl/index.php/JLM/article/view/245). Then
  Anton will present [Computational universals in linguistic theory:
  Using recursive programs for phonological
  analysis](materials/ChandleeJardine2021.pdf).


## 22 Oct 2024

* We discussed [related work
  (references)](materials/relatedwork.pdf). Students were asked to
  review those papers and think about which ones they would be
  interested in for class.
* We began discussing how to formulate learning problems. [Learning
  handout 1](materials/learning1.pdf)

## 17 Oct 2024

* Jake finished his presentation.
* Alina presented on  Chapter 19 Representations
  of Gradual Oppositions.

## 15 Oct 2024

**FALL BREAK -- NO CLASS**

## 10 Oct 2024

* M presented Chapter 17 on Correspondence Theory.
* Jake began presenting on Chapter 16 on Primitive Constraints for
  Nonlexical Stress Patterns.
* Jake will finish presenting next Thursday before Alina's
  presentation.

## 08 Oct 2024

* Sarah presented Chapter 15 on Syllable Struture and the SSP.
* Logan presented Chapter 18 on Phonetically-based Phonology.
* Next Thursday Oct 15, Alina will present Chapter 19 Representations
  of Gradual Oppositions.

## 03 Oct 2024

* Shigeto's presented Chapter on Zigula and Shambaa.
* Elizabeth presented Chapter on Tibetan.


## 01 Oct 2024

* **Short Paper Assignment** (for students enrolled in 3 credits):
  Please turn in no later than Tuesday October 22, 2024 (in
  class). Please print your assignment and hand it in to me.

  For this assignment, choose a morpho-phonological data set and
  provide an analysis of it. Your analysis should formalize the
  analysis using the logical transductions we have studied in
  class. Chapters 7 through 14 in Part 2 of DCP/DPC are samples of the
  kind of short paper expected. It is not necessary to compare your
  formalization to some other framework. It is necessary to be clear
  about the representations you are positing in the underlying and
  surface forms.

  You **may not choose** one of the datasets in chapters 7 through 14
  (unless you are proposing a radically different analysis.) You **may
  choose** a dataset you have previously analyzed using a different
  set of formal tools (such as with rules or OT). For example,
  datasets from Phonology 1 or 2 can be used, or even a dataset from
  an undergraduate phonology class or introductory textbook. You may
  choose a dataset you have collected, but such original research is
  not the purpose of this assignment, and may be more appropriate for
  a final project.

  A [collection of tex files](materials/texsupport.tar.gz) providing
  macros and examples for your convenience. I commpiled the pdf in
  there with the command `latexmk dolatian-russian.tex`.

* Ola presented Chapter 9 on Lamba.
* Geonhee presented Chapter 10 on Turkish.

* We developed a plan for next week. [Updated DCP/DPC text here](materials/dcpChaps1-20.pdf)
  - Oct 8: Presentation on chapter 15 Syllabls by Sarah
  - Oct 8: Presentation on chapter 16 Stress by Jacob
  - Oct 10: Presentation on chapter 18 Phonetically-grounded representations by Logan
  - Oct 10: Presentation on chapter 17 Correspondence Theory by M

## 26 Sep 2024

* A few more words were said about suffix substitution closure,
  subsequence closure, and tier-based successor signatures.
* We then discussed BUFIA, using [slides from a
  minicourse](https://www.jeffreyheinz.net/talks/Heinz-2021-minicourse-LCORYOC-slides.pdf)
  a few years back.
* Next week, please read chapters 9-12 in DCP/DPC and support your
  classmates as they present!

## 24 Sep 2024

* We finished discussing chapter 5.
* On Thursday we will review the BUFIA learning algorithm in [this
  paper](https://aclanthology.org/W19-5708/).

## 19 Sep 2024

* We discussed section 5.1 and 5.2.
* We made a plan for the next few weeks.
  - Oct 1: Presentation on chapter 9 Lamba by Ola
  - Oct 1: Presentation on chapter 10 Turkish by Geonhee
  - Oct 3: Presentation on chapter 11 Tibetan by Elizabeth
  - Oct 3: Presentation on chapter 12 Zigula and Shambaa by Shigeto
* For Tuesday, please finish reading chapter 5.

## 17 Sep 2024

* We finished discussing Chapter 3.
* Upated DCP/DPC [Parts 1 and 2](materials/dcpParts1-2.pdf)

## 12 Sep 2024

* We discussed logical transductions as they can be applied to phonological processes.
* We got through the deletion example in Chapter 3.

## 07 Sep 2024

* We finished discussing Chapter 2.
* If you are interested in attending the [Rutgers workshop on
  subregular
  phoonology](https://rucll.github.io/workshop2024/index.html), please
  let me know this week.
* For Thursday, please finish read up to Chapter 3.3 in [Part
  1](materials/dcpPart1.pdf) of DCP/DPC.

## 05 Sep 2024

* We discussed the Chapter up to 2.6. In particular, how the successor
  model of strings, with and without features, can be combined with FO
  logic to provides a way to define well-formedness constraints. The
  representational primitives can be thought of as claims regarding
  the psychologically real primitives. They are the aspects of the
  representation that can be "looked up" for free.
* For Tuesday, please finish reading chapter 2 in [Part
  1](materials/dcpPart1.pdf) of DCP/DPC. (Note it has been updated
  **again** to fix more errors).

## 03 Sep 2024

* We discussed Chapter 1 and began discussion of models of strings and
  FO logic in Chapter 2.
* For Thursday, please read up to section 2.6 (p.43) in [Part
  1](materials/dcpPart1.pdf) of DCP/DPC. (Note it has been updated to
  fix some errors).

## 29 Aug 2024

* We finished the Phonology Forum talk. Next Tuesday we discuss
  Chapter 1.

## 27 Aug 2024

* We went over the [syllabus](materials/LIN655_Syllabus_Fall2024.pdf).
* As an overview of the class, I presented [a
  talk](materials/forum24-Heinz.pdf) I gave last week at the Phonology
  Forum sponsored by the Phonological Society of Japan.
* Here is [Part 1](materials/dcpPart1.pdf) of "Doing Computational
  Phonology"/"Doing Phonology, Computationally".
* For Thursday, please read Chapter 1 of Part 1.

-------------------------------------------------------------------------------
