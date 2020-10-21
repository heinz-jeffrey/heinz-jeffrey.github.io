from pomegranate import *
import numpy as np
import random as r

d1 = DiscreteDistribution({'A' : 0.35, 'C' : 0.20, 'G' : 0.05, 'T' : 0.40})
d2 = DiscreteDistribution({'A' : 0.25, 'C' : 0.25, 'G' : 0.25, 'T' : 0.25})
d3 = DiscreteDistribution({'A' : 0.10, 'C' : 0.40, 'G' : 0.40, 'T' : 0.10})

# what do each of these lines add?  - add states
s1 = State(d1, name="s1")
s2 = State(d2, name="s2")
s3 = State(d3, name="s3")

# makes a HMM object and adds  - each state (1,2,3)
model = HiddenMarkovModel('example')
model.add_states([s1, s2, s3])

# what do these transitions represent? - initial state probs
model.add_transition(model.start, s1, 0.90)
model.add_transition(model.start, s2, 0.10)

# what would this trans prob matrix look like?
model.add_transition(s1, s1, 0.80)
model.add_transition(s1, s2, 0.20)
model.add_transition(s2, s2, 0.90)
model.add_transition(s2, s3, 0.10)
model.add_transition(s3, s3, 0.70)
model.add_transition(s3, model.end, 0.30)
model.bake()

# what does this line print out for us?  - _________________________
print(model.log_probability(list('ACGACTATTCGAT')))


"""
I added some stuff down here to make this a little more general
and show more examples.

This gives us a log probability. How can we change this?
This exponentiates the log probability, giving us a result in the interval [0,1].

"""
t = model.log_probability(list('ACGACTATTCGAT'))
tprob = np.exp(t)
print(tprob)

"""
This bit of code at the bottom generates 50 sequences (each of length 13),
and then calculates their respective probabilities.
(It's very sloppy but hey it does what I want...)

"""
types = ['A','C','T','G']
seqs, seq_probs = [], []


for i in range(50):
     seq = ""
     while len(seq) < 13:
          seq = seq + r.choice(types)
     seqs.append(seq)
     seq_probs.append(np.exp(model.log_probability(list(seq))))

print("\n")
print("Sequence \t\t\t Probability")
print("------------------------------------------------------------------------")
for i in range(len(seqs)):
     print(str(seqs[i]) +"\t\t" + str(seq_probs[i]))

