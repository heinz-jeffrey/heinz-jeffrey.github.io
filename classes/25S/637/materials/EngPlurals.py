# coding=utf-8

# Jeff Heinz
# April 2025
# English Plural with Pynini

# Pynini 2.1.3
# Python 3.8.5


import pynini
import functools
from pynini.lib import rewrite

A = functools.partial(pynini.accep, token_type="utf8")

# VIEWING PATHS IN FINITE TRANSDUCERS

def printPaths(f):
  paths = f.paths(input_token_type="utf8",output_token_type="utf8")
  while not paths.done():
    print(f"{paths.istring()}:{paths.ostring()}")
    paths.next()

# some natural classes

vowel = (
  A("a") | A("i") | A("ɪ") |
  A("e") | A("ɛ") | A("æ") |
  A("u") | A("ʊ") | A("o") |
  A("ɔ") | A("ɑ") | A("ə") |
  A("ʌ")
).optimize()

consonant = (
  A("p") | A("b") | A("t") |
  A("d") | A("k") | A("g") |
  A("m") | A("n") | A("ŋ") |
  A("f") | A("v") | A("θ") |
  A("ð") | A("s") | A("z") |
  A("ʃ") | A("ʒ") | A("h") |
  A("ʤ") | A("ʧ") | A("j") |
  A("w") | A("ɹ") | A("l")
).optimize()

strident = (
  A("s") | A("z") | A("ʃ") |
  A("ʒ") | A("ʤ") | A("ʧ")
).optimize()

voiceless = (
  A("p") | A("t") | A("k") |
  A("f") | A("θ") | A("s") |
  A("ʃ") | A("ʧ")
).optimize()


# all possible strings from all segments
sigmaStar = (pynini.closure(vowel | consonant)).optimize()

# PHONOLOGY

# From Gorman and Sproat 2021, p.59, section 5.2.3:
#
# The Pynini `cdrewrite` function is used to compile context-dependent
# rewrite rules into WFSTs. The first four arguments, all mandatory,
# include a transducer defining τ, unweighted acceptors defining the
# left and right environments L and R -- an empty string is used for
# null environments -- and a cyclic, unweighted acceptor representing
# Σ*, the closure over the rule’s alphabet. The reserved symbol [BOS]
# (“beginning of string”) can be used to symbolize the left boundary
# symbol ^ when constructing L ; similarly, [EOS] (“end of string”)
# can be used to symbolize the right boundary symbol $ when
# constructing R. The optional keyword argument `mode` allows one to
# specify directionality of application; left-to-right application is
# the default.

# Epenthesis

epenPair = pynini.string_map(
  [("","ɪ")],
  input_token_type="utf8",
  output_token_type="utf8").optimize()

epenthesis = pynini.cdrewrite(epenPair, strident, strident, sigmaStar)

# Devoicing

devoicePairs = pynini.string_map(
  [ ("b","p"),
    ("d","t"),
    ("g","k"),
    ("v","f"),
    ("ð","θ"),
    ("z","s"),
    ("ʒ","ʃ"),
    ("ʤ","ʧ") ],
  input_token_type="utf8",
  output_token_type="utf8").optimize()

devoicing = pynini.cdrewrite(devoicePairs, voiceless, "", sigmaStar)

phonology = (epenthesis @ devoicing).optimize()


# MORPHOLOGY

z_suff = pynini.string_map(
  [("","z")],
  input_token_type="utf8",
  output_token_type="utf8")

regPlural = (sigmaStar + z_suff).optimize() # plural morphology  suffixes a 'z'

# LEXICON

wish  = A("wɪʃ")
cat   = A("kæt")
cable = A("keɪbl")
dog   = A("dɔg")

wishesT = ((wish @ regPlural) @ phonology).optimize()

# A general funtion to produce plural form

def printRegPl(stem):
  x = (((A(stem)) @ regPlural) @ phonology).optimize()
  for string in rewrite.lattice_to_strings(x,token_type="utf8"):
    print(string)


# LEXICAL EXCEPTIONS

pluralExceptions = pynini.string_map(
  [ ("fʊt", "fit"),      # foot/feet
    ("gus", "gis"),      # goose/geese
    ("fɪʃ", "fɪʃ"),      # fish/fish
    ("gutza", "gutza"),  # hypothetical (to see how phonology devoices any voiceless-voiced sequences)
    ("guzza", "guzza")   # hypothetical (to see how phonology epenthesize any pair of stridents)
   ],
  input_token_type="utf8",
  output_token_type="utf8").optimize()


# Plural Morphology with exceptions

lexicalExceptions = pynini.project(pluralExceptions,"input")

otherWords = (sigmaStar - lexicalExceptions).optimize()

plural = (pluralExceptions | (otherWords + z_suff)).optimize()

# New general function to produce plural forms

def makePl(stem):
  x = (((A(stem)) @ plural) @ phonology).optimize()
  for string in rewrite.lattice_to_strings(x,token_type="utf8"):
    print(string)

# the "full" lexicon

lexicon = (wish | cat | cable | dog | lexicalExceptions).optimize()

lexiconPlural = lexicon @ plural @ phonology

# just playing around with unicode
dogLEX = pynini.string_map(
  [("🐕","dɔg")],
  input_token_type="utf8",
  output_token_type="utf8").optimize()
