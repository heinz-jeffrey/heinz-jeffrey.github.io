
# **Hidden Markov Model** 

This note is mainly just a summarization of the textbook (Jurafsky and Martin 2019) with related python codes from jason2506 and you can see the original code [here](https://github.com/jason2506/PythonHMM/blob/master/hmm.py). Also, I read some online posts to further understand before I write this so they may affected to this short note.


## Index

1. Markov Model
2. HMM
3. The Forward Algorithms
4. The Viterbi Algorithms
5. The Forward-Backward Algorithms

---

## Markov Model

Markov Model is a model that shows **the probabilities of sequences of states**.

![width:400px](https://i.ibb.co/3MmLnDW/CixTo.png)


Markov Models are: 

* based on Markov Assumption

	> $P(q_{i} = a | q_{i-1}) = P(q_{i} = a | q_1 ... q_{i-1})$

* have transition probabilities, that the sum of arcs leaving a state must be 1


Markov chain can be specified by:
* Q: a set of n states
	$Q = q_1, q_2, ... q_n$
* A: a transition probability matrix
	$A = a_{11}, a_{12}, ... a_{nn}  \\
	(\sum_{j=1}^n aij = 1)$
* $\pi$: an initial probability distribution over states
	$\pi = \pi_1, \pi_2, ... \pi_n  \\
	(\sum_{i=1}^n \pi = 1)$


---
## The Hidden Markov Model

However, in most real world situation, events that we want to know are **hidden** because they are not observed. **HMM** tries to calculate the possibility of the sequence of this hidden states by looking at the observed data.

As the HMM can reveal the hidden sequence of some events, it is widely used in sequential labeling such as **speech recognition**, **text recognition** and **POS tagging**. 

>### HMM and POS tagging
>
>HMM was used to POS tagging before CRF(Conditional Random Field) was introduced. Although it has advantages such as unsupervised learning and faster learning speed, it has fundamental problems:
>
>* Hard to handle Unknown words
>* Label bias problem
> 
> These problems caused MFMM(Maximum Entropy Markov Model) or CRF to be introduced. 


HMM assumes that a system has two components:
* hidden states $\leftarrow$ What we want to find out
	$\downarrow$ *emission probability*
* observable states $\leftarrow$ What we can know
 ![width:700px](https://t1.daumcdn.net/cfile/tistory/9908AC405AD5FF9328)


Hidden Markov Models can be specified by:
* Q: a set of n states
	$Q = q_1, q_2, ... q_n$
* A: a transition probability matrix 
	$A = a_{11}, a_{12}, ... a_{nn}  \\
	(\sum_{j=1}^n aij = 1)$
* $\pi$: an initial probability distribution over states
	$\pi = \pi_1, \pi_2, ... \pi_n  \\
	(\sum_{i=1}^n \pi = 1)$
* O: a sequence of T observations
	$O = o_1 o_2 ... o_T$
* B: a sequence of observed likelilhoods, or emission probabilities, each expressing the probability of an ovservation $o_t$ being generated from a state $i$
	$B = b_i(o_t)$


So, let's try to understand how this work with simple example:

Jason Eisner's ice cream task
![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.2.png?raw=true)


1. $Q = \{Hot, Cold\}$
2. $A = \begin{pmatrix}
.6 & .4\\
.5 & .5
\end{pmatrix}$
3. $\pi = (.8, .2)$
4. for $b_i(o_t)$, the matrix will be:
	$b_i(o_t) = \begin{pmatrix}
.2 & .4 & .4\\
.5 & .4 & .1
\end{pmatrix}$


And when the $O$ is given, we can calculate (1) the possibility of this sequence happening and (2) the highest possible sequence of weather which caused this sequence to happen.

In order to do this, we should solve **three fundamental problems**:
> ### **Problem 1. Likelihood**: 
> 
> when HMM $\lambda = (A, B)$ and $O$ is given, determine the likelihood $P(O|\lambda)$
> 
> ### **Problem 2. Decoding**:
> 
> when HMM $\lambda = (A, B)$ and $O$ is given, discover the best hidden state sequence $Q$ 
> 
> ### **Problem 3. Learning**:
> 
> when $O$ and $Q$ are given, learn the HMM parameters $A$ and $B$

---
## Likelihood Computation: The Forward Algorithm

> ### **Problem 1. Likelihood**: 
> 
> when HMM $\lambda = (A, B)$ and $O$ is given, determine the likelihood $P(O|\lambda)$

This problem can be solved step by step.

Let's here use again the ice cream task to understand things more easily. 

This is the notes from Jason:

|          | Day 1 | Day 2 | Day 3 |
|----------|-------|-------|-------|
| Weather  | ??    | ??    | ??    |
| Icecream | 3     | 1     | 3     |


1. Here, we already know how many states we have in a sequence (T=3), thus we can calculate $P(O|Q)$
2. As this is the "sequence", we also have to calculate the possibility of the specific sequence $P(q_i|q_{i-1})$
3. But we do not know the hidden sequence, thus we have to add up the all possibility of the sequence to get the overall probability of observation $P(O)$

However, as the number exponentially rise, we need to use more efficient $O(N^2T)$; **the forward algorithms**.

![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.5.png?raw=true)

So, basically what the forward algorithm is doing is that it uses a table to store intermediate values as it moves through the observed sequence but makes it more efficient by summing them up into a single **forward trellis**. Thus, each cell express the probability of $\alpha_t(j)$ which means the probability of being in $j$ state after seeing the first $t$ observations, given automaton $\lambda$: 

$\alpha_t(j) = P(o_1, o_2, ..., q_t = j | \lambda)$

And as we sum up every possiblities we've passed through, this can be computed as:

$\alpha_t(j) = \sum_{i=1}^N \alpha_{t-1}(i)a_{ij}b_j(o_t)$

This can be coded as below:

```{p}
# Before we start, we have to define the HMM:

class hmm():
# we can define hmm with Q, A, pi, O, B:
def __init__ (self, states, observed, trans_prob = None, emit_prob = None, iniprob = None):
	self._states = set(states) # states
	self._observed = set(observed) 
	self._trans_prob = _transition(trans_prob, self._states, self._states)
	self._emit_prob = _emission(emit_prob, self._states, self._observed)
```
```
# Define the forward algorithm: 

def _forward(self, observed_sequence):
	# Before we start, we have to rule out 0 length sequence:
	sequence_length = len(observed_sequence)
	if sequence_length == 0:
		return []
	
	# Make a forward trellis to store each alpha:
	alpha = [{}]
	# Initialization:
	for state in self._states:
		alpha[0][state] = self.init_prob(state)*self.emit_prob(state, observed_sequence[0])

	# Recursion: 
	for index in range(1, sequence_length):
		alpha.append({})
		for state_to in self._states:
			prob = 0
			for state_from in self._states:
				prob += alpha[index-1][state_from]*self.trans_prob(state_from, state_to)
			alpha[index][state_to] = prob*self.emit_prob(state_to, sequence[index])

	# Final:
	return alpha
```

---

## Decoding: The Viterbi Algorithm

The decoding task is to find out the hidden sequence

> ### **Problem 2. Decoding**:
> 
> when HMM $\lambda = (A, B)$ and $O$ is given, discover the best hidden state sequence $Q = q_1 q_2 ... q_T$


The idea is that we can already calculate the possibility that $O$ happens in each possible hidden sequence using the forward algorithm, and we only have to choose the biggest probability among them. However, this is impossible due to the exponentially large number. 

Thus, **Viterbi algorithm** is introduced to solve this problem. 

![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.8.png?raw=true)

The basic idea is to fill out the trellis with $v_t(j)$ while processing the observation sequence through time, where:

$v_t(j) = \max_{q_1, ..., q_{t-1}} P(q_1 ... q_{t-1}, o_1, o_2, ... o_t, q_t = j | \lambda)$


The "max" here shows that Viterbi fills each cell recursively. 

If we already know the probability of being in every state at time $t-1$, for a given state $q_j$ at time $t$, the value $v_t(j)$ is computed as

$v_t(j) = \max_{i=1}^N v_{t-1}(i) a_{ij}b_{j}(o_t)$


The main idea of this Viterbi algorithm is **backpointers**. 
As Viterbi tracks the path to the state which results to the highest probability, it use backpointers to do that work. 

![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.10.png?raw=true)

So, we can define the backpointers mathmatically like this:

$bt_t(j) = \argmax_{i=1}^N v_{t-1}(i)a_{ij}b_j(o_t)$

Now, we can define the Viterbi recursion as follows:

> **Initialization**:
> 
> $v_1(j) = \pi_jb_j(o_1)  \quad \quad 1\leq j\leq N$
> 
> $bt_1(j) = 0 \quad \quad   1\leq j\leq N$
> 
> **Recursion**:
> 
> $v_t(j) = \max_{i=1}^N v_{t-1}(i) a_{ij}b_{j}(o_t); \quad 1\leq j\leq N, 1 	< t \leq T$
> 
> $bt_t(j) = \argmax_{i=1}^N v_{t-1}(i)a_{ij}b_j(o_t); \quad 1\leq j\leq N, 1 	< t \leq T$
> 
> **Terminal**:
> 
> The best score: $p* = \max_{i=1}^N v_T(i)$
> 
> The start of backtrace: $q_T* = \argmax_{i=1}^N v_T(i)$
>  

Let's see how this is implemented in python coding:

```{p}
# Viterbi algorithms is different from forward algorithm in 2 sense:
# 1. Viterbi use "MAX" rather than summing up everything
# 2. Viterbi has backpointers

def viterbi(self, sequence):
# Before we start, we have to rule out 0 length sequence:
	sequence_length = len(observed_sequence)
	if sequence_length == 0:
		return []
	
	# Make a storage trellis:
	delta = {}

# Initialization:
	for state in self._states:
		delta[state] = self.init_prob(state)*self.emit_prob(state, sequence[0])
	# we also need a backpointer here:
	pre = []

# Recursion: 
	for index in range(1, sequence_length):
		# delta_bar is a set of probabilities of o_t
		delta_bar = {}
		# pre_state to store the path we passed:
		pre_state = {}

		for state_to in self._states:

			max_prob = 0
			max_state = None

			for state_from in self._states:

				# calculate the probability v_t: 
				prob = delta[state_from]*self.trans_prob(state_from, state_to)
				
				# choose the maximum probability of possible v_t: 
				if prob > max_prob:
					max_prob = prob 
					max_state = state_from
			
			delta_bar[state_to] = max_prob*self.emit_prob(state_to, sequence[index])

			pre_state[state_to] = max_prob*self.emit_prob(state_to, sequence[index])
		
		# rewrite delta to delete unnecessary o_t
		delta = delta_bar
		# append backpointer information in pre_state
		pre.append(pre_state)
	
	# find the max v_t and its state
	max_state = None
	max_prob = 0
	for state in self._states:
		if delta[state] > max_prob:
			max_prob = delta[state]
			max_state = state
	
	if max_state is None:
		return []
	
# Final:

	# find the hidden sequence using backpointers
	result = [max_state]
	for index in range(sequence_length - 1, 0, -1):
		max_state = pre[index -1][max_state]
		result.insert(0, max_state)

	return result
```

---
## HMM Training: The Forward-Backward Algorithm


> ### **Problem 3. Learning**:
> 
> when $O$ and $Q$ are given, learn the HMM parameters $A$ and $B$

The training algorithm for HMM is called the **forward-backward**, or **Baum-Welch** algorithm, which is a special case of the **Expectation-Maximization(EM)** algorithm. This algorithm got its name because it's using both **forward probability** and **backward probability** to train the HMM parameters. 

>### Expectation-Maximization algorithm
>
>an iterative method to find maximum likelihood estimates(MLE) or maximum a posterior(MAP) of parameters in probablistic model with latent variables (hidden variables). One instance of variational inference. 

This **forward-backward** algorithm takes the unlabeled sequence of observation O and a set of potential hidden states Q as inputs and trains both the transition probabilities A and the emission probabilities B. The process will be done iteratively based on its previous estimates to find out the best estimates.

As I mentioned before, this algorithm uses both forward and backward probability. The forward probability is the probability of $\alpha_t(j)$ which means the probability of being in $j$ state after seeing the first $t$ observations, given automaton $\lambda$.

$\alpha_t(j) = P(o_1, o_2, ..., q_t = j | \lambda)$

The backward probability is the probability of seeing the observations from time $t+1$ to the end, given that we are in state $i$ at time $t$, and given the automation $\lambda$:

$\beta_t(i) = P(o_{t+1}, o_{t+2}, ... o_T| q_t = i, \lambda)$

Backward probability calculates the probability from the final state to the $t+1$, thus named "backward". 

> **Initialization**:
> 
> $\beta_T(i) = 1, \quad 1 \leq i \leq N$
> 
> **Recursion**:
> 
> $\beta_t(i) = \sum_{j=1}^N a_{ij}b_j(o_{t+1})\beta_1(j), \quad 1 \leq i \leq N, 1 \leq t < T$
> 
> **Termination**:
> 
> $P(O|\lambda) = \sum_{j=1}^N \pi_jb_j(o_1)\beta_1(j)$

Let's now calculate the transition probabilities and the observation probabilities. 

> **Transition probability**: 
> 
> $\hat a_{ij} = \frac{Expected \;number \;of \;transition \;from \;state \;i \;to \;state \;j}{Expected \;number \;of \;transition \;from \;state \;i}$

The main idea in here is that if we know the probability of a given transition $i \rightarrow j$ take place in time $t$ for each $t$, we can sum all $t$s to find out the total count for the transition $i \rightarrow j$. 

Here, we define the probability $\xi_t$ as the probability of being in state $i$ at time $t$ and state $j$ at time $t+1$, given the observation sequence $O$ and the model $\lambda$:

$\xi_t(i,j) = P(q_t = i, q_{t+1} = j | O, \lambda)$

However, we can't get this directly, but we can get this through the rule of conditional probability:

$\xi_t(i,j) = \frac{P(q_t = i, q_{t+1} = j , O| \lambda)}{P(O|\lambda)}$

![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.12.png?raw=true)

The picture below shows that how we can calculate the numerator. As we need forward probability $\alpha_t(i)$ possibility from $o_1$ to $o_t$ and backward probability $\beta_{t+1}(j)$ from $o_{t+1}$ to the end. Between them, we know that there is $a_{ij}b_j(o_{t+1})$. So, we only have to multiply them all.

$P(q_t = i, q_{t+1} = j , O| \lambda) = \alpha_t(i) a_{ij}b_j(o_{t+1}) \beta_{t+1}(j)$

All we need to know now is the denominator. The probability of the $O$ given $\lambda$ is simply the forward (or backward) probability of the whole utterance.

$P(O|\lambda) = \sum_{j=1}^N \alpha_t(j)\beta_t(j)$

So, we can use the use of conditional probability to get $\xi_t(i,j)$ from $\bar \xi_t(i,j)$:

$\xi_t(i,j) = \frac{\alpha_t(i) a_{ij}b_j(o_{t+1}) \beta_{t+1}(j)}{\sum_{j=1}^N \alpha_t(j)\beta_t(j)}$

Now we can get this $\hat a_{i,j}$ using $\xi_t$.

$\hat a_{ij} = \frac{Expected \;number \;of \;transition \;from \;state \;i \;to \;state \;j}{Expected \;number \;of \;transition \;from \;state \;i}
			= \frac{\sum_{t=1}^{T-1} \xi_t(i,j)}{\sum_{t=1}^{T-1} \sum_{k=1}^N \xi_t(i, k)}$

We can now move on to the observation probability.

> **Observation probability**: 
>
> $\hat b_j(V_k) = \frac{Expected \;number \;of \;being \;in \;state \;j \;and \;observing \;V_k}{Expected \;number \;of \;being \;in \;state \;j}$

To compute this, we need the probability of beiing in state $j$ at time $t$, $\gamma_t(j)$:

$\gamma_t(j) = P(q_t = j|O. \lambda)$

Again, we can't get this directly.

$\gamma_t(j) = \frac{P(q_t = j, O|\lambda)}{P(O|\lambda)}$

![](https://github.com/jihyeon-ha/Note/blob/main/Note/figa.13.png?raw=true)

The picture below shows how to calcuate the numerator, and we already know the $P(O|\lambda)$. Thus $\gamma_t(j)$ will be:

$\gamma_t(j) = \frac{\alpha_t(j) \beta_t(j)}{\sum_{j=1}^N \alpha_t(j)\beta_t(j)}$

Now we can compute the observation probability. (The notation $\sum_{t=1 s.t.O_t = v_k}^T$ means *sum over all $t$ for which the observation at tiem $t$ was $v_l$*)

$\hat b_j(V_k) = \frac{\sum_{t=1 s.t.O_t = v_k}^T \gamma_t(j)}{\sum_{t=1}^T \gamma_t(j)}$

```{p}

# As we already defined forward probability in the forward algorithm, we need to define backward probability

def _backward(self, sequence):
	sequence_length = len(sequence)
	if sequence_length == 0:
		return []

# Initialization:
	beta = [{}]
	for state in self._states:
		beta[0][state] = 1

# Recursion:
	for index in range(sequence_length - 1, 0. -1):
		beta.insert(0, {})
		for state_from in self._states:
			prob = 0
			for state_to in self._states:
				prob = 0
				for state_to in self._states:
					prob += beta[1][state_to] * self.trans_prob(state_from, state_to) * emit_prob(state_to, sequence[index])
				beta[0][state_from] = prob

# Termination: 
	return beta

##################################################
# Now let's work on learning:

def learn(self, sequence, smoothing=0): 
	
# Define alpha and beta
	length = len(sequence)
	alpha = self._forward(sequence) 
	beta = self._backward(sequence)

# E - step
	gamma = []
	for index in range(length):
		prob_sum = 0
		gamma.append({})
		for state in self._states:
			prob = alpha[index][state]*beta[index][state]
			gamma[index][state] = prob
			prob_sum += prob

		if prob_sum == 0:
			continue
		
		for state in self._states:
			gamma[index][state] /= prob_sum

	xi = []
	for index in range(length - 1):
		prob_sum = 0
		xi.append({})
		for state_from in self._states:
			xi[index][state_from] = {}
			for state_to in self._states:

				prob = alpha[index][state_from] * beta[index + 1][state_to] * self.trans_prob(state_from, state_to) * self.emit_prob(state_to, sequence[index + 1])

				xi[index][state_from][state_to] = prob
				prob_sum += prob

		if prob_sum == 0:
			continue

		for state_from in self._states:
			for state_to in self._states:
				xi[index][state_from][state_to] /= prob_sum

# M - step:

	states_number = len(self._states)
	observed_number = len(self._observed)
	for state in self._states:

		# update start probability
		self._start_prob[state] = (smoothing + gamma[0][state]) / (1+ states_number * smoothing)

		# update transition probability
		gamma_sum = 0
		for index in range(length - 1):
			gamma_sum += gamma[index][state]

		if gamma_sum > 0:
			denominator = gamma_sum + states_number * smoothing 
			for state_to in self._states:
				xi_sum = 0
				for index in range(length - 1):
					xi_sum += xi[index][state][state_to]
				self._trans_prob[state][state_to] = (smoothing + xi_sum) / denominator
		else:	
			for state_to in self._states:
				self._trans_prob[state][state_to] = 0

		# update emission probability
		gamma_sum += gamma[length - 1][state]
		emit_gamma_sum = {}
		for symbol in self._symbols:
			emit_gamma_sum[symbol] = 0
		
		for index in range(length):
			emit_gamma_sum[sequence[index]] += gamma[index][state]

		if gamma_sum > 0:
			denominator = gamma_sum + symbols_number * smoothing
			for symbol in self._symbols:
				self._emit_prob[state][symbol] = \
					(smoothing + emit_gamma_sum[symbol]) / denominator
		
		else:
			for symbol in self._symbols:
				self._emit_prob[state][symbol] = 0

```

