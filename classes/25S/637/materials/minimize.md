% How to classify a transducer in ATT format

# Overview

This shows step by step how to algebraically classify a finite-state
transducer provided in the ATT format.

As a running example, it will use the [fig6right.att](fig6right.att)
file, which is the nonminimal DFT found on the right in Figure 6 of
[Burness et
al. 2021](https://www.glossa-journal.org/article/id/5780/).

This ATT file is accompanied by the [syms-fig6.txt](syms-fig6.txt)
file which provides a numerical encoding of the symbols.  Note there
can be two such files, one for input symbols and one for output
symbols. In this example, the input and output symbols are the same
and so only one file is present.

# What you will need to have installed

1. The [pynini python
   package](https://www.openfst.org/twiki/bin/view/GRM/Pynini). Use
   `pip install pynini`. 
2. The program `classify` from the
   [Language-Toolkit-2](https://github.com/vvulpes0/Language-Toolkit-2). Follow
   the directions there.
3. The [openfst command line tools](https://www.openfst.org/). This is
   easiest to install with
   [conda](https://docs.conda.io/en/latest/). Use the command `conda
   install -c conda-forge openfst` on Linux, MacOS, or (hopefully)
   WSL.

# Step 1 - Conversion

Convert the ATT file to a binary FST file. This is done generally with
the command line as follows.

```
> fstcompile --isymbols=isyms_file --osymbols=osyms_file --keep_isymbols --keep_osymbols filename.att filename.fst
```

where `isyms_file`, `osyms_file`, `filename.att` are the names of the
text files you provide as input for the numerical encoding of the
input symbols, the numerical encoding of the output symbols, and the
ATT format description of the transducer itself, respectively; and
where `filename.fst` is the binary file output by this command
encoding the transducer.

Thus for the transducer in our example, one can run the following.

```
$ fstcompile --isymbols=syms-fig6.txt --osymbols=syms-fig6.txt --keep_isymbols --keep_osymbols fig6right.att fig6right.fst
```

# Step 2 - Minimization

Start up python, import pynini, read the fst file, and minimize the transducer.

```
$ python3
Python 3.8.18 (default, Sep 11 2023, 13:40:15)
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pynini
>>> f = pynini.Fst.read("fig6right.fst")
>>> f.minimize()
```

That's it!

Note that `minimize()` assumes that the trnsducer is deterministic. If
it is not, use `optimize()` instead since this first aims to
determinize the transducer before minimizing. See the pynini
documentation for details.

# Step 3 - Printing and file writing

To check it on the screen, just use `print`.

```
>>> print(f)
0	0	x	x
0	0	s	s
0	1	S	S
0
1	1	x	x
1	1	S	S
1	1	s	S
1

>>> quit()
```

To put it into a file, you can do something like this.

```
>>> output = open("minimized.att",'w')
>>> print(f,file=output)
>>> quit()
```

# Step 4 - Classify

Now we have a minimized transducer in ATT format and so we can check
its algebraic structure. From the command line, run the `classify`
command. You must use the `-N` flag. There are 12 classes we want to
check. These are the finite, definite, reverse definite, and
generalized definite classes, as well as their tier-based, and
multi-tier based counterparts. However, classify won't check the
tier-based finite (I think it's just an oversight). So just check the
following: `FIN Def RDef GD TDef TRDef TGD MTF MTDef MTRDef MTGD`.

```
$ cat minimized.att | classify -N Fin Def RDef GD TDef TRDef TGD MTF MTDef MTRDef MTGD 
[ ("Fin",False)
, ("Def",False)
, ("RDef",False)
, ("GD",False)
, ("MTF",True)
, ("TDef",True)
, ("TRDef",True)
, ("MTDef",True)
, ("MTRDef",True)
, ("TGD",True)
, ("MTGD",True)
]
```

# Step 5 - Record your results!

Put your results in the [spreadsheet](https://docs.google.com/spreadsheets/d/1IWFIMThG5AIkmrA2c6gmbTTBxIZinQmGT5WUhJI-47I/edit?usp=sharing)!
