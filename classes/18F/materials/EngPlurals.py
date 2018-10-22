# coding=utf-8

# Jeff Heinz
# October 2018
# English Plural with Pynini

import pynini
import functools

A = functools.partial(pynini.acceptor, token_type="utf8")
T = functools.partial(pynini.transducer, input_token_type="utf8", output_token_type="utf8")


# some natural classes

vowel = (A("i") | A("ɪ") | A("e") | A("ɛ") | A("æ") | A("u") | A("ʊ") | A("o") | A("ɔ") | A("ɑ") | A("ə") | A("ʌ")).optimize()

consonant = (A("p") | A("b") | A("t") | A("d") | A("k") | A("g") | A("m") | A("n") | A("ŋ") | A("f") | A("v") | A("θ") | A("ð") | A("s") | A("z") | A("ʃ") | A("ʒ") | A("h") | A("ʤ") | A("ʧ") | A("j") | A("w") | A("ɹ") | A("l")).optimize()

strident = (A("s") | A("z") | A("ʃ") | A("ʒ") | A("ʤ") | A("ʧ")).optimize()

voiceless = (A("p") | A("t") | A("k") | A("f") | A("θ") | A("s") | A("ʃ") | A("ʧ")).optimize()

# all segments
sigmaStar = (pynini.closure(vowel | consonant)).optimize()


# phonological changes
epenthesis = pynini.cdrewrite(T("","ɪ"), strident, strident, sigmaStar)

devoicePairs = (T("b","p") | T("d","t") | T("g","k") | T("v","f") | T("ð","θ") | T("z","s") | T("ʒ","ʃ") | T("ʤ","ʧ")).optimize()
devoicing = pynini.cdrewrite(devoicePairs, voiceless, "", sigmaStar)

phonology = (epenthesis @ devoicing).optimize()

regPlural = (sigmaStar + T("", "z")).optimize() # plural morphology suffixes a 'z'
 
wish = A("wɪʃ")
cat = A("kæt")
cable = A("keɪbl")
dog = A("dɔg")

wishesT = ((wish @ regPlural) @ phonology).optimize()
wishes = wishesT.stringify(token_type="utf8")


# THIS DOES NOT WORK
# def makeRegPl(stem):
#   x = ((A(stem) @ regPlural) @ phonology).optimize() 
#   return (x.stringify(token_type="utf8"))

# a lexicon of memorized exceptions

pluralExceptions = ( T("fʊt","fit")   # foot/feet 
                   | T("gus","gis")   # goose/geese
                   | T("fɪʃ","fɪʃ") ).optimize()   # fish/fish

lexicalExceptions = pynini.project(pluralExceptions)

wrongPlural = (lexicalExceptions @ regPlural).optimize()

regPluralLessExceptions = (regPlural - wrongPlural).optimize()

plural = (pluralLessExceptions | pluralExceptions).optimize()

# a lexicon of nouns for which plural morphology applies productively and normally.

lexicon = (wish | cat | dog | cable | foot | goose | fish).optimize()
 
dog_LEX = T("🐕","dɔg") # just playing around with unicode
