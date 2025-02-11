% Computational Linguistics 2 (LIN 637, Spring 2025)

# Course Information

**Course:** TThu 14:00-15:20, SBS N250 (or compling lab)

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/),
[jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours: Tuesday 11:30-1pm, Wednesday 2pm-3:30pm and by appointment**

# Materials

* [Syllabus](materials/LIN637_Syllabus_Spring2025.pdf)

# Course Log

## 11 Feb

* We sketched how to obtain a RE from a NFA.
* We showed why NFA are closed under complement, intersection, and
  difference.
* Using those facts, and the notion of reachable states, we showed we
  can decide whether one regular language is a subset of another.  And
  then we can decide whether two regular languages are equal.
* We played with plebby.

  ```
  :display <a a>
  :display ~<a a>
  :display <a,b>
  :display ~<a,b>
  :display \/{<a a>, <b b>}
  :display /\{<a a>, <b b>}
  :display /\{<a a>, <b b>}
  :display [b,c]<b b>
  :display ~[b,c]<b b>
  :display [b,c]<b b>
  :display [a]*<a a>
  :display [a]*|%%|<a a>
  =bcstar *\/{%||%<b>, %||%<c>}
  :display \/{bcstar, *@{bcstar, %||%<a>, bcstar, %||%<a>, bcstar}}
  :equal \/{bcstar, *@{bcstar, %||%<a>, bcstar, %||%<a>, bcstar}} *@{bcstar, *@{%||%<a>, bcstar, %||%<a>}, bcstar}
  ```

## 06 Feb

* We looked at this [supplement](materials/nfadfa-supplement.pdf),
  which defines NFA and DFA and how they process strings from a
  non-recursive perspective. (This will change.)
* We discussed how to visualize NFA and DFA as graphs.
* We explored connections between NFA and REs.
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
