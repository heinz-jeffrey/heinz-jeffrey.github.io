% Learnability (LIN 629)
65;6203;1c
# Course Information

**Course:** TThu 15:00-16:20, Frey Hall 326

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/), [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours:** M 13:00-14:00, W 11:00-13:00, SBS N237

# Materials

* [Syllabus](materials/learnability-LIN629-22F-Heinz.pdf)

# Course Log

## 17 Nov 2022

* Jeff

## 15 Nov 2022

* Logan presents on Nowak et al. 2022.
* For next Tuesday Nov 22 please read [Jardine et al
  2014](https://proceedings.mlr.press/v34/jardine14a.html) (Salam and Adil presenting)

## 10 Nov 2022

* Yola presents on Rawski and Heinz's response to Pater.
* Gillian presents on Dunbar's response to Pater.
* For Tuesday please read [Nowak et
  al. 2002](materials/NowakKomarovaNiyogi2002.pdf) (Logan presenting)

## 08 Nov 2022

* Rita [presents](materials/Pater2019presentation.pdf) on Pater 2019
* For those interested, here is [Kodner and Khalifa
  2022](https://aclanthology.org/2022.sigmorphon-1.18.pdf) which
  discusses the past tense debate in the context of the 2022
  SIGMORPHON shared task on modeling inflection.

## 03 Nov 2022

* Jeff on [different approaches to evaluating ML systems](materials/studyinglearning.pdf)

## 01 Nov 2022

* Jack [presented](materials/LIN629_Presentation_Jack.pdf) on on
    extracting automata from recurrent neural networks (Weiss et
    al. 2018).
* For next Tuesday, please read the following (Rita, Yola, and Gillian presenting next Tue and Thu)
    - Generative linguistics and neural networks at 60 [Pater 2019](https://doi.org/10.1353/lan.2019.0009)
    - Response by Dunbar [The implementational mapping problem](https://doi.org/10.1353/lan.2019.0013)
    - Response by Rawski and Heinz [No free lunch](https://doi.org/10.1353/lan.2019.0021)
* In case you are interested, here is the [whole issue](https://muse.jhu.edu/issue/40022)

## 27 Oct 2022

* Han presented on string extension learning (Heinz 2010). Slides are
  here.
  - For those interested, [this 2012
    paper](materials/Heinz-KasprzikEtAl-2012-LLHS.pdf) presents a
    deeper analysis of the lattice structure of string-extension
    learnable hypothesis spaces, and shows that many other classes of
    languages languages that are identifiable in the limit (including
    the zero reversible languages) have this lattice structure. It
    also characterizes which of these classes are also PAC learnable.
* For Tuesday, please read Weiss et al. 2018 on extracting automata
    from recurrent neural networks [Weiss et
    al. 2018](https://arxiv.org/pdf/1711.09576.pdf) (Jack presenting).

## 25 Oct 2022

* Nick presented on distributional learning (Clark and Eyraud
  2007). The [slides are here](materials/Nick-presentation.pdf).
* For Thu Oct 27 read string extension learning [Heinz
    2010](https://aclanthology.org/P10-1092.pdf) (Han presenting)
* For those interested:
  - Here is [(Clark
    2013)](https://jmlr.csail.mit.edu/papers/volume14/clark13a/clark13a.pdf)
    which builds on the prior work of the subsitutable language
    learning algorithm to remove much (all?)  of the ambiguity in the
    derivations. Consequently, syntactic structures are learned. For
    example, he basically recovers the syntactic structure underlying
    propositional logic. And here is Clark and Yoshinaka's [2016
    review](materials/ClarkYoshinaka2016.pdf) of several extensions to
    the distributional learning framework since 2007.
  - Here are [slides](materials/Heinz-MLRegTest-2022.pdf) from my talk
    on investigating the generalization powers of NNs on regular
    languages at the "All Things Language and Computation" series last
    Friday.

## 20 Oct 2022

* We concluded the handout on [identification in the
  limit](materials/idlimit.pdf).
* We discussed RPNI from [de la Higuera's
  slides](materials/de-la-higuera.pdf).
* ALERGIA and OSTIA adapt these ideas to learn probability
  distributions over sigma star and string-to-string functions from
  positive examples only.
* [flexfringe](https://github.com/tudelft-cda-lab/FlexFringe)
  implements RPNI and ALERGIA and many variants
  [paper](https://orbilu.uni.lu/handle/10993/32814).
* For more details read de la Higuera (2010) [Grammatical
  Inference](https://doi.org/10.1017/CBO9781139194655).

## 18 Oct 2022

* We continued our study of [identification in the limit
  paradigms](materials/idlimit.pdf).
* Reminder that project proposals are to be approved by
  November 1. Please talk to me if you need help coming up with a good
  project.
* Here is the schedule we developed over the next several weeks.
  - Tue Oct 25: Nick on distributional learning [Clark and Eyraud
    2007](https://www.jmlr.org/papers/volume8/clark07a/clark07a.pdf)
  - Thu Oct 27: Han on string extension learning [Heinz
    2010](https://aclanthology.org/P10-1092.pdf)
  - Tue Nov 01: Jack on extracting automata from recurrent neural
    networks [Weiss et al. 2018](https://arxiv.org/pdf/1711.09576.pdf)
  - Thu Nov 3 - Tue Nov 8: Rita, Gillian, Yola
    - Generative linguistics and neural networks at 60 [Pater 2019](https://doi.org/10.1353/lan.2019.0009)
    - Response by Dunbar [The implementational mapping problem](https://doi.org/10.1353/lan.2019.0013)
    - Response by Rawski and Heinz [No free lunch](https://doi.org/10.1353/lan.2019.0021)
    - The [whole issue](https://muse.jhu.edu/issue/40022)
  - Thu Nov 10: Logan on evolution and learnability [Komorova et
    al. 2002](materials/NowakKomarovaNiyogi2002.pdf)
  - Thu Nov 15: Salam on learning classes of DFTs [Jardine et al 2014](https://proceedings.mlr.press/v34/jardine14a.html)
  - Thu Nov 17: Kenneth on learning TSL [Lambert 2021](https://proceedings.mlr.press/v153/lambert21a.html)
  - Adil, TBD

## 13 Oct 2022

* Eric [presented](materials/Sclafani-LLP2.pdf) and led discussion on
  Heinz 2010 "Learning Long-distance Phonotactics".
* Jeff finished going over the last several slides from his [what does
  learning mean](materials/whatdoeslearningmean.pdf) talk, which
  emphasized how deterministic finite state machines define a
  parameterized concept class, and whether the concepts are formal
  (boolean) languages, stochastic languages, or string-to-string
  functions -- so whether the parameter values are boolean, reals, or
  strings -- the learning of these classes is conducted
  similarly. Papers exist which make these connections explicit for
  DFA more generally and k-SL and k-SP classes in particular.
* For next Tuesday, review the first 10 pages (up to 4.7) of the notes
  on identification in the limit. (We have already discussed up to 4.5
  on Oct 06).
* Also for those who are enrolled and have not yet presented yet,
  please think about which papers you would be interested in
  presenting over the next few weeks as I would like to schedule. Feel
  free to get in touch if you need pointers.

## 11 Oct 2022

* Fall break


## 06 Oct 2022

* We began our study of [identification in the
  limit](materials/idlimit.pdf).
* Read [Heinz 2010](http://jeffreyheinz.net/papers/Heinz-2010-LLP.pdf)
  for next Thursday. Eric will present.

## 04 Oct 2022

* Class canceled.

## 29 Sep 2022

* We discussed the rest of Chapter 5 of Valiant 2013.
* Jeff presented his talk [what does learning
  mean](materials/whatdoeslearningmean.pdf)

## 27 Sep 2022

* Sarah
  [presents](materials/Morphology-Language-Acquisition-Slides-Payne.pdf)
  on Lignos and Yang 2016.
* Read the rest of Valiant 2013 chapter 5 and write answers to [these
  questions](materials/04-pac-chap05-2.html) and send them to me
  [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu).

## 22 Sep 2022

* Class cancelled. Try to check out the learning talks on Friday at [this workshop](https://www.jeffreyheinz.net/events/WMTRPprogram.html)

## 20 Sep 2022

* Magda [presented](materials/NoisyExamplesMarkowska.pdf) on Angluin
  and Laird's 1988 paper "Learning from Noisy Examples."

## 15 Sep 2022

* John presents on the VC
  dimension. ([Slides](materials/VC-Dimension-Murzaku.pdf))

## 13 Sep 2022

* We went over this [handout](materials/pacproofs.pdf) that reviewed
  the proof that the tightest-fit rectangle algorithm pac-learns the
  class of axis-aligned rectangles and the proof that the elimination
  algoritm pac-learns the class of monomials.
* For Thursday, read sections 1, 2 and 3 of chapter 3 KV94 on the VC
  dimension.

## 08 Sep 2022

* We reviewed the preliminary definition of PAC learnability.
* We discussed and explained the PAC learnability of axis-aligned
  rectangles.
* We discussed the modified definition of PAC learnability which takes
  into account the size of the representation of the concepts.
* We established a plan for the next several classes
  - Tue Sep 13: Jeff on PAC learning monomials (1.3 in KV94)
  - Thu Sep 15: John on the VC dimension (3.1, 3.2, 3.3 in KV94 and theorems 3.3,3.4)
  - Tue Sep 20: Magda on [Learning from Noisy Examples](materials/AngluinLaird1988.pdf), up to 2.3
  - Thu Sep 22: Class canceled because of [this
    workshop](https://www.jeffreyheinz.net/events/WMTRPprogram.html)
    At least see the learning talks from 4:30pm on Fri Sep 23!
  - Tue Sep 27: Sarah on [Morphology and Language Acquisition](materials/LignosYang2016.pdf)

## 06 Sep 2022

* We went over HW03. 
* We discussed up to 5.7 in Valiant 2013.
* We defined PAC learning formally.

## 01 Sep 2022

* We finished the handout on enumerability and computability.
* We discussed the first part of chapter 5 of Valiant 2013 "Probably Approximately Correct".
* For next time
  - Write answers to [these
    questions](materials/03-pac-chap05-1.html) and send them to me
    [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu). Show
    and explain your work.
  - Read [up to 5.7](materials/Valiant2014-Chaps4-5.pdf)
    of Valiant 2013 "Probably Approximately Correct"

## 01 Sep 2022

* We finished the handout on enumerability and computability.
* We discussed the first part of chapter 5 of Valiant 2013 "Probably Approximately Correct".
* For next time
  - Write answers to [these
    questions](materials/03-pac-chap05-1.html) and send them to me
    [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu). Show
    and explain your work.
  - Read [up to 5.7](materials/Valiant2014-Chaps4-5.pdf)
    of Valiant 2013 "Probably Approximately Correct"

## 30 Aug 2022

* We discussed chapter 3 of Valiant 2013.
* We explained enumerability and why there are [too few
  grammars](materials/toofewgrammars.pdf).
* For next time
  - Read [chapter 4 and up to 5.5](materials/Valiant2014-Chaps4-5.pdf)
    of Valiant 2013 "Probably Approximately Correct"
  - Here are the [footnotes, glossary and
    index](materials/Valiant2014-NotesGlossaryIndex.pdf) of Valiant
    2013 "Probably Approximately Correct"

## 25 Aug 2022

* We discussed chapters 1 and 2 of Valiant 2013.
* We finished discussing [language learning on planet Verorez](materials/verorez.pdf).
* For next time
  - Read chapter 3 of [Valiant 2013 "Probably Approximately Correct"](materials/Valiant2014-Chap3.pdf)
  - Write answers to [these questions](materials/02-pac-chap-03.html)
    and send them to me
    [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu). Remember,
    conciseness is a virtue.

## 23 Aug 2022

* We went over the syllabus.
* We studied [language learning on planet Verorez](materials/verorez.pdf).
* For next time
  - Read chapters 1 and 2 of [Valiant 2013 "Probably Approximately Correct"](materials/Valiant2014-Chaps1-2.pdf)
  - Write answers to [these
    questions](materials/01-pac-chaps-01-02.html) and send them to me
    [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu). Remember,
    conciseness is a virtue.


-------------------------------------------------------------------------------
