# coding=utf-8

# Jeff Heinz
# October 2018
# 3.3.3. Breton Double Plurals with Pynini
#
# Based on Figure 3.8 p. 82 in Roark and Sproat 2007
#

import pynini
import functools

A = functools.partial(pynini.acceptor, token_type="utf8")
T = functools.partial(pynini.transducer, input_token_type="utf8", output_token_type="utf8")

# some natural classes

letter = A("a")
for x in ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]: letter = A(x) | letter
letter.optimize()

sg = A("[sg]")
pl = A("[pl]")
dim = A("[dim]")
noun = A("[noun]")
ou = A("[ou]") 
ed =  A("[ed]") 

num = sg | pl
feat = dim | num
category = noun | num
inflClass = ou | ed

sigma = (letter | inflClass | category | feat).optimize()

lexicon = A("bag[ou][noun]")

# lexical 'construction' rules
numRule = pynini.cdrewrite(T("",pl),"","[EOS]",sigma.star,mode="opt")
dimRule = pynini.cdrewrite(T("",dim),"","[EOS]",sigma.star,mode="opt")

# lexical realization rules

dimRealization = pynini.cdrewrite(T("","ig"+ou),inflClass,sigma.star+dim,sigma.star)
plRealization =  pynini.cdrewrite(T(ou,"ou"),"",sigma.star+noun+pl,sigma.star)

# clean up rules

cleanUp = pynini.cdrewrite(T(inflClass | category | feat,""),"","",sigma.star)

# double plurals in Breton

newLex = (lexicon @ numRule @ dimRule).optimize()
grammar = (dimRealization @ plRealization @ cleanUp).optimize()
lexForms = (newLex @ grammar).optimize()

# Checking the program

pynini.optimize(pynini.project(lexForms,True))

def realizeNoun(m):
  x = (m @ grammar).optimize() 
  y = pynini.project(x,True)
  return y.stringify(token_type="utf8")

arrow = "\t-->\t" # \t is the 'tab' character

print("bag[sg]\t" + arrow + realizeNoun(lexicon+sg))
print("bag[pl]\t" + arrow +  realizeNoun(lexicon+pl))
print("bag[sg,dim]" + arrow + realizeNoun(lexicon+sg+dim))
print("bag[pl,dim]" + arrow + realizeNoun(lexicon+pl+dim))



