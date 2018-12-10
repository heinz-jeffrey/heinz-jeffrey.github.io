# coding=utf-8

# Jeff Heinz
# November 2018
# Replace Rules

# Here I try to implement the transducer construction algorithm in
# Mohri and Sproat 1996.  In particular, the left-to-right obligatory
# application of a rewrite rule.  As a running example, I use the rule
# a b --> x / a b __ a 
#
# This is not complete and probably not correct. Not all transitions
# mentioned in Mohri and Sproat appear.

import pynini
import functools

A = functools.partial(pynini.acceptor, token_type="utf8")
T = functools.partial(pynini.transducer, input_token_type="utf8", output_token_type="utf8")


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",">","[<1]","[<2]"]

mini = ["a","b","x",">","[<1]","[<2]"]
letters = ["a","b","x"]


sigma = pynini.epsilon_machine()
for x in mini:
    sigma = A(x)|sigma
sigma.optimize()

letter = pynini.epsilon_machine()
for x in letters:
    letter = A(x)|letter
letter.optimize()

S = sigma.star
L = letter.star

rb  = A(">")
lb1 = A("[<1]")
lb2 = A("[<2]")

lbs = (lb1 | lb2).optimize()

phi = A("ab") # target
psi = A("x")  # change
lam = A("ab") # left context
rho = A("a")  # right context

# RULE : ab -> x | ab __ a


############# r ######################

wordsWithRho =  pynini.closure(S + rho + S, 1,0)
wordsWithRho.optimize()

wordsWithOutRho = pynini.difference(S,wordsWithRho)
wordsWithOutRho.optimize()

r = wordsWithOutRho | pynini.closure(wordsWithOutRho + T("",rb) + rho + wordsWithOutRho,1,0)
r.optimize()

############### f ####################

phiRB = (phi + rb).optimize()

wordsWithPhiRB = pynini.closure(S + phiRB + S, 1,0)
wordsWithPhiRB.optimize()

wordsWithOutPhiRB = pynini.difference(S,wordsWithPhiRB)
wordsWithOutPhiRB.optimize()

f = wordsWithOutPhiRB | pynini.closure(wordsWithOutPhiRB + T("",lbs) + phiRB + wordsWithOutPhiRB,1,0)
f.optimize()

############### replace ####################

state0Fig2 = (L | lb2 | T(rb,"") ).star
state0Fig2.optimize()
 
replace = state0Fig2 | (state0Fig2 + lb1 + T(phi,psi) + T(rb,"")+state0Fig2).star  
replace.optimize()


############### l1 ####################

wordsWithLamLB1 = S + lam + T(lb1,"") + S 
wordsWithLamLB1.optimize()

l1 = ((L | lb2 ).star | wordsWithLamLB1.star).star
l1.optimize()


#wordsWithLam = pynini.closure(S + lam + S, 1,0)
#wordsWithLam.optimize()

#wordsWithOutLam = pynini.difference(S,wordsWithLam)
#wordsWithOutLam.optimize()

# Lb = (L | lb2 ).star
# Lb.optimize()

#l1 = Lb | (Lb + lam + T(lb1,"")+Lb).star
#l1.optimize()


############### l2 ####################

# Lb2 = (letter | lb2).star

# notLam = pynini.difference(Lb2,Lb2+lam)
# notLam = notLam @ (letter | T(lb2,"")).star
# notLam.optimize()

# notLamLB2 = notLam + T(lb2,"")

#l2 = ().star
#l2.optimize()


############### Example words ####################

w1 = A("aba")
w2 = A("ababa")
w3 = A("abababa")
