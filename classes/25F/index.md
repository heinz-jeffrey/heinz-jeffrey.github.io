% Learnability (LIN 629)

# Course Information

**Course:** TuTh 09:30-10:50

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/),
  [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours:** WF 3:30pm-5:00pm

# Materials

* [Syllabus](materials/learnability-LIN629-25F-Heinz.pdf)

# Course Log

## Upcoming

(subject to change)

* Thu 10/23 - Guest Lectures by Logan and Han on their recent papers
* Tue 10/28 - [Yang and Piantadosi
  2022](https://www.pnas.org/doi/full/10.1073/pnas.2021865119) by
  Robin
* Thu 10/30 - [OSTIA (see chapter
  18)](materials/delaHiguera2010.pdf) by Dorothy
* Tue 11/04 - [UR
  learning](https://proceedings.mlr.press/v153/hua21a.html) by Ben
* Thu 11/06 - Guest lecture by Magda on her recent paper +
  dissertation research
* Tue 11/11 - [review
  paper](http://jeffreyheinz.net/papers/Heinz-2016-CTLDP.pdf) by
  Geonhee
* Thu 11/13 - something related to syntactic learning (precise paper
  TBD) by Alina



## 28 Oct 2025
* Robin presents the Yang and Piantadosi paper.
* We had a follow-up discussion on bufia.
* We discussed the [Vapnik-Chervonenkis dimension](materials/07vcd.pdf).

## 23 Oct 2025

* Logan presented on his work applying bufia to Quechua.
* Han presented her work on developing a version of bufia over
  autosegmental representations for learning tonotactics.

## 21 Oct 2025

* Ola presented the [BUFIA](https://aclanthology.org/W19-5708/) paper.
* We discussed abductive principles as they relate to bufia (see chapters 3 and 4 of [Rawski 2021](http://jeffreyheinz.net/advisees/2021_JonRawski_dissertation.pdf)).
* We discussed [empirical and theoretical approaches to
  learning](materials/06empirical.pdf).


## 16 Oct 2025

* We went over the proofs that the strategies we discussed for
  learning (1) axis-aligned rectangles and (2) monomials both satisfy
  the PAC-criteria. See [Kearns and Vazirani](materials/KV94.pdf) (up
  to 1.4), and Jeff's [notes on it](materials/05pacintro.pdf)

## 14 Oct 2025

* FALL BREAK - NO CLASS

## 09 Oct 2025

* We made plans for papers and topics to study in upcoming weeks.
* We discussed in broad terms ideas for final projects.
  - theoretical work -- identify linguistically motivated classes of
    concepts learnable under some criterion
  - theoretical/empirical work -- identify weakness in some current
    learning algorithm and improve it
  - empirical work -- compare a new variant of a learning algorithm
    (that you are introducing) to the existing version on one or more
    datasets
  - empirical work -- compare an existing learning algorithm on one or
    more datasets to others (such as NNs or maxent)
* We began the formal [introduction to PAC](materials/05pacintro.pdf)

## 07 Oct 2025

* Jacob presented Angluin's proof, reading [Angluin
  1980](materials/Angluin1980-iiflpd.pdf), section 3q, condition 1
  and/or 2 (TBD)
* We introduced the axis-aligned rectangle learning problem and
  identified the strategy of selecting the smallest axis-aligned
  rectangle which fits the positive data will as one that will succeed
  if all positive data points are eventually observed.

## 02 Oct 2025
  - M presented [Clark and Eyraud
    2007](https://www.jmlr.org/papers/volume8/clark07a/clark07a.pdf),
  - We continued with PAC, getting through section 5.6 of [Valiant
    2013](materials/Valiant2013.pdf).

## 30 Sep 2025

*  Matthew presented [Heinz
   2009](https://www.jeffreyheinz.net/papers/Heinz-2009-RLLSP.pdf), on
   learning stress patterns with neighborhood distinctness.
* We began our introduction to PAC. We got through sections 5.2 and
  5.3 of [Valiant 2013](materials/Valiant2013.pdf).
* PAC readings in the near term which we will be going over in class.
  - Sections 5.2 - 5.6 (inclusive) of [Valiant
    2013](materials/Valiant2013.pdf).
  - And then up to 1.4 of [Kearns and Vazirani
    1994](materials/KV94.pdf)

## 25 Sep 2025

* Hannah presented on [Wu and Heinz
  2023](https://proceedings.mlr.press/v217/wu23a/wu23a.pdf). We also
  discussed the limitations of using relative frequencies as a way to
  distinguish between well-formed and ill-formed expressions.
* We discussed an efficient, state-merging method "RPNI", which
  identifies the class of regular languages in the limit from positive
  and negative data. See [de la Higuera
  2010](materials/delaHiguera2010.pdf) for more details (Chapter 12).

## 23 Sep 2025

* We discussed some items in the string extension learning paper.
  - the characteristic sample
  - the example relating to the Parikh map
  - the example relating to the generalized subsequence languages
* We discussed Angluin's theorem, but did not prove it.  **Claimed by
  Jacob to show proof on 10/07!**
* We reviewed three ways to learn k-SL languages
  1. collect permissible k-factors
  2. build prefix tree and merge states with a k-1 prefix
  3. "filling in" the transitions and states of a k-definite machine
* We observed that each method is an instantiation of a more general strategy
  1. string extension learning
  2. state-merging
  3. activating parts of a fixed, deterministic grammar
* We observed that string extension learning has been generalized to
  lattice learning [(Heinz, Kasprzik, and Kötzing
  2013)](https://www.jeffreyheinz.net/papers/Heinz-KasprzikEtAl-2012-LLHS.pdf)
* We observed that the "filling in" method
  - can be generalized to multiple finite DFA (for handling the k-SP
  language) [(Heinz and Rogers
  2013)](http://jeffreyheinz.net/papers/Heinz-Rogers-2013-LSCLFDA.pdf)
  - has a probabilistic variant, which is the classical n-gram model,
    which finds the MLE of the data with respect to this type of model.
  - (and the probabilistic variant can also be extended to multiple
    DFA [(Shibata and Heinz
    2018)](http://jeffreyheinz.net/papers/Shibata-Heinz-2019-MLEFRDSL.pdf)
    )
* Resources for learning more on state merging
  - [de la Higuera 2010](materials/delaHiguera2010.pdf) is a
    comprehensive, technical treatment
  - [Heinz, de la Higuera, and van Zaanen
    2015](materials/HdlHvZ2015.pdf) is less technical, and covers main
    ideas
* For Thursday:

## 18 Sep 2025

* We reviewed the zero-reversible languages and the state-merging
  algorithm for learning them.
* We discussed state-merging strategies more broadly for learning
  regular languages.
* Abed presented on string extension learning.
* Future topics for possible presentation
  - a state-merging strategy for learning stress patterns [Heinz
    2009](https://www.jeffreyheinz.net/papers/Heinz-2009-RLLSP.pdf)
    **Claimed by Matthew for 9/30!**
  - RPNI - efficient learning of the class of regular languages from
    positive and negative data [de la Higuera 2010, Chapter 12 section
    4](materials/delaHiguera2010.pdf)
  - Substitutable languages (a subclass of CF languages) [Clark and
    Eyraud
    2007](https://www.jmlr.org/papers/volume8/clark07a/clark07a.pdf)
    **Claimed by M for 10/02!**
  - Sting extension learning with noise [Wu and Heinz
    2023](https://proceedings.mlr.press/v217/wu23a/wu23a.pdf)
    **Claimed by Hannah for 9/25!**  <!-- - Distributional learning
    more generally []() --> <!-- - Efficiency Concerns [Eyraud et
    al. 2014]() -->


## 16 Sep 2025

* We discussed some of your ideas on how to modify identification in the limit.
* We discussed language learning on [planet
  Verorez](materials/04verorez.pdf).
* Read [Heinz 2010](https://aclanthology.org/P10-1092/) for Thursday
  (Abed will present it within 40 minutes).

## 11 Sep 2025

* We went over the proof that the one can identify the class of
  TM-computable languages from texts that generated by primitive
  recursive functions (using the generator naming relation as opposed
  to the tester).
* The basic idea behind the proof is that the text itself in a
  generator/enumerator of the language and so there is a p.r. program
  for it. The learner simply guesses the first program in the
  enumeration of all programs that correctly predicts the text it has
  seen so far. After finitely many guesses, it is guaranteed to find
  the first program generating the text, and thus have found a program
  generating the target language.
* We then began discussing your reflections on Gold. Here is a list of
  the issues the class identified.
  1. The paradigm targets formal languages, which is about weak
     generative capacity and not strong generative capacity.
  2. The paradigm considers data presentations without noise. But real
     world data is noisy with false positives, false negatives, or
     missing data.
  3. The paradigm does not consider time/resource complexity. While it
     may be useful to say "no algorithm exists no matter how many
     resources are consumed" we also want to be interested in learners
     that make efficient use of the data.
  4. The paradigm requires exact identification, which is too strict a
     requirement because may learn something close enough to the
     target language, even if it is not exactly the same. (this can
     also help explain why languages change)
  5. The learner does not know when convergence happens.
  6. As a model of acquisition, the paradigm fails to take into
     account the critical period. Humans succeed before this window
     closes.
  7. As a model of acquisition, the paradigm takes into account
     adversarial data presentations; that is, ones that potentially
     delay key data points for as long as possible. Human children are
     probably not exposed to adversarial data presentations.
  8. As a model of acquisition, how would the model take into account
     U-shaped learning, where children, correctly generalize,
     overgeneralize, and then correctly generalize again.
  9. The paradigm does not appear to make distinctions between
     learning grammars, searching for grammars in a space of grammars,
     and memorizing strings.
* Your HW for Tuesday, is the following: Pick one of the above issues,
  and provide 1-2 ideas about how the id in the limit paradigm could
  be modified to address the issue. Again, please limit your response
  to 1-2 paragraphs (max one page). You do not have to provide a
  formal definition of learning, but you are welcome to. You are also
  welcome to reflect whether your proposed solution allows edge cases
  that makes instances of the learning problem "unreasonably"
  difficult (for instance if you are trying to learn in the presence
  of noise, how do you ensure the noise doesn't drown out the signal?)

## 09 Sep 2025

* We reviewed the proofs of theorems 4 and 6 and discussed them.
* We proved the following statement: Any finite class of languages is
  identifiable in the limit (hypothesizing testers) from positive
  (arbitrary) data.
* The idea behind this proof is that any finite class of languages can
  be ordered in such a way such that, for any pair of languages (L,
  L') in a proper subset relationship (so L is a subset of L'), (a
  grammar for) language L is ordered before (a grammar for) language
  L'. Then a learning strategy is to find the first grammar in the
  list consistent with the data so far.
* Homework for Thursday: Write 1-2 paragraphs (no more than one page),
  reflecting on the identification in the limit paradigm. What are
  some choices in its definition of learning that you would reconsider
  and why? Please email the assignment to me.

<!-- * Time permitting, we considered the learnability of languages spoken -->
<!--   on the planet [Verorez](materials/04verorez.pdf). -->
<!-- * For Thursday, begin reading [chapter 3](materials/HdlHvZ2015.pdf) on -->
<!--   state-merging. -->


## 04 Sep 2025

* We went through the notes on [id in the
  limit](materials/03idlimit.pdf). In particular:
* We reviewed identification in the limit of testers from arbitrary
  text (commonly known as identification in the limit from positive
  data).
* We examined some two classes of formal languages (Strictly
  k-Piecewise and Strictly k-Local) and algorithms which can learn
  these classes under this definition of learning. Both exemplify
  "string extension learning" which is a particular kind of learning
  strategy. It has other properties as well which we will return to later.
* At the end of class we considered another strategy based on
  enumeration, and presented an algorithm which learns the class BAR-X
  under this definition.
* For next Tuesday please study Theorems 4 and 6 and their
  proofs. (You can skip Theorems 5 and 7 for now.)

## 02 Sep 2025

* We discussed the twelve identification in the limit paradigms that
  Gold introduced, the main results, and Gold's discussion of the
  implications of these results vis a vis child acquisition.
* We took a brief aside on [recursive function
  theory](materials/recursive-function-theory.pdf) to get an idea of
  some of the finer points of arbitrary functions/sets/text versus
  recursive functions/sets/text versus primitive recursive
  functions/sets/text.
*  Here are some notes on [id in the
  limit](materials/03idlimit.pdf). Please read up to, but not
  including, section 2.4 for Thursday. Document the mistakes!

## 28 Aug 2025

* We discussed finished talking about likelihood.
* We continued talking about learning as a computational problem.
* We discussed the first few sections of Gold 1967.
* We are prepared to discuss [enumeration](materials/02enumeration.pdf),
  which plays an important role in computability.
* For next Tuesday, read section 4 of Gold 1967.

## 26 Aug 2025

* We went over the syllabus.
* We introduced the idea of studying learning as a computational problem.
* We studied the meanings of consistent estimators.
* [01intro.pdf](materials/01intro.pdf)
* For Thursday: please read sections 1-3 of [Gold
  1967](materials/Gold--1967--LanguageIdentificationInTheLimit.pdf).

-------------------------------------------------------------------------------
