from pyfoma import FST, State

myfst = FST()            # Init object

s0 = myfst.initialstate  # FST() always has one state, make that s0
s2 = State()             # Add a state
s1 = State()             # Add a state


s0.add_transition(s0, ("x","x"), 0.0)  # Add transitions...
s0.add_transition(s1, ("s","s"), 0.0)
s0.add_transition(s2, ("S","s"), 0.0)

s1.add_transition(s1, ("x","x"), 0.0)
s1.add_transition(s1, ("s","s"), 0.0)
s1.add_transition(s1, ("S","S"), 0.0)

s2.add_transition(s2, ("x","x"), 0.0)
s2.add_transition(s2, ("s","S"), 0.0)
s2.add_transition(s2, ("S","S"), 0.0)

s0.finalweight = 0.0                   # Set the final weight
s1.finalweight = 0.0                   # Set the final weight
s2.finalweight = 0.0                   # Set the final weight

myfst.states = {s0,s1,s2}              # Set of states
myfst.finalstates = {s0,s1,s2}         # Set of final states
myfst.alphabet = {"x","s","S"}         # Optional alphabet

