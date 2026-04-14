# Likely EELE-491 Exam Questions and Answers

## 1. Binary classification metrics

**Question:**
A classifier produces the following on a test set:

* TP = 18
* TN = 50
* FP = 6
* FN = 12

Compute:

1. Accuracy
2. Precision
3. Recall
4. F1-score

**Answer:**

$$ \text{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}=\frac{18+50}{18+50+6+12}=\frac{68}{86}=0.791 $$


$$
\text{Precision}=\frac{TP}{TP+FP}=\frac{18}{18+6}=\frac{18}{24}=0.75
$$

$$
\text{Recall}=\frac{TP}{TP+FN}=\frac{18}{18+12}=\frac{18}{30}=0.60
$$

$$
F1=2\cdot\frac{PR}{P+R}=2\cdot\frac{0.75\cdot0.60}{0.75+0.60}
=2\cdot\frac{0.45}{1.35}=0.667
$$

**Final answers:**
Accuracy = 0.791
Precision = 0.750
Recall = 0.600
F1 = 0.667

**Why this is likely:** HW2 explicitly emphasized confusion matrices, accuracy, precision, recall, and F1 for SVM classification and class imbalance. 

---

## 2. Overfitting / validation methods

**Question:**
Explain the difference between:

1. Resubstitution
2. Holdout validation
3. 5-fold cross-validation

Why is resubstitution usually overly optimistic?

**Answer:**

* **Resubstitution** evaluates the model on the same data it trained on.
* **Holdout validation** reserves part of the data for validation/testing and trains on the rest.
* **5-fold cross-validation** splits the data into 5 parts, trains on 4 and validates on 1, repeating until each fold has been used as validation once.

Resubstitution is overly optimistic because the model is tested on data it already saw during training, so it may reflect memorization rather than generalization.

**Why this is likely:** HW2 directly compared resubstitution, 20% holdout, and 5-fold cross-validation. 

---

## 3. Compare common classifiers

**Question:**
Briefly describe one strength of each:

* Linear SVM
* KNN
* Decision Tree
* Neural Network

**Answer:**

* **Linear SVM:** good when classes are approximately linearly separable and margin-based classification works well.
* **KNN:** simple, intuitive, and makes decisions based on nearby examples.
* **Decision Tree:** interpretable and easy to visualize.
* **Neural Network:** can model more complex nonlinear relationships.

**Why this is likely:** HW2 had students train and compare multiple model types including SVMs, KNNs, trees, and neural networks. 

---

## 4. MLP forward pass

**Question:**
Consider a one-hidden-layer neural network with logistic activations. Use:

$$
x=$$0.05,\ 0.10$$
$$

$$
W_1=
\begin{bmatrix}
0.15 & 0.25\
0.20 & 0.30
\end{bmatrix}
$$

$$
W_2=
\begin{bmatrix}
0.40 & 0.50\
0.45 & 0.55
\end{bmatrix}
$$

$$
b=$$0.35,\ 0.60$$
$$

Compute the hidden-layer output (h) and final output (y).

**Answer:**
This is the exact example from HW3.

Hidden-layer pre-activations:

$$
z_h = xW_1 + b_1
$$

$$
z_{h1}=0.05(0.15)+0.10(0.20)+0.35=0.3775
$$

$$
z_{h2}=0.05(0.25)+0.10(0.30)+0.35=0.3925
$$

Apply sigmoid:

$$
h_1=\sigma(0.3775)\approx 0.5933
$$

$$
h_2=\sigma(0.3925)\approx 0.5969
$$

So:

$$
h=$$0.5933,\ 0.5969$$
$$

Output-layer pre-activations:

$$
z_y = hW_2 + b_2
$$

$$
z_{y1}=0.5933(0.40)+0.5969(0.45)+0.60 \approx 1.1059
$$

$$
z_{y2}=0.5933(0.50)+0.5969(0.55)+0.60 \approx 1.2249
$$

Apply sigmoid:

$$
y_1=\sigma(1.1059)\approx 0.7514
$$

$$
y_2=\sigma(1.2249)\approx 0.7729
$$

**Final answer:**
$$
h=$$0.5933,\ 0.5969$$, \quad y=$$0.7514,\ 0.7729$$
$$

**Why this is likely:** HW3 explicitly used this exact forward-pass example and gave these numeric targets. It is a very fair exam-style problem. 

---

## 5. One-step backprop: likely lighter version

**Question:**
Why does backpropagation require the derivative of the activation function?

**Answer:**
Backpropagation uses the chain rule to determine how much each weight contributed to the final error. The derivative of the activation function tells us how a small change in the neuron input changes its output, which is required to compute the gradient for updating weights.

**Why this is likely:** Even if the professor skips a full backprop calculation, this concept is central to HW3 and HW4.  

---

## 6. Activation functions

**Question:**
For each activation below, state whether its output is bounded or unbounded, and where its gradient tends to become small:

* Sigmoid
* tanh
* ReLU
* swish

**Answer:**

* **Sigmoid:** bounded between 0 and 1; gradient is small for very negative or very positive inputs.
* **tanh:** bounded between -1 and 1; gradient is small for large-magnitude positive or negative inputs.
* **ReLU:** unbounded above, bounded below by 0; gradient is small at negative inputs because output is 0 there.
* **swish:** generally unbounded above; gradient can become small in large negative regions.

**Why this is likely:** HW4 Problem 1 directly asked students to reason about ranges and regions with small gradients for sigmoid, tanh, ReLU, and swish. 

---

## 7. Loss functions

**Question:**
A regression model has:

$$
y=$$-0.3,\ 0.5,\ 0.9$$, \quad \hat y=$$-0.1,\ 0.4,\ 1.5$$
$$

Compute the **MSE** and **MAE**.

**Answer:**
Errors:

$$
y-\hat y=$$-0.2,\ 0.1,\ -0.6$$
$$

Absolute errors:

$$
$$0.2,\ 0.1,\ 0.6$$
$$

Squared errors:

$$
$$0.04,\ 0.01,\ 0.36$$
$$

MAE:

$$
\text{MAE}=\frac{0.2+0.1+0.6}{3}=\frac{0.9}{3}=0.3
$$

MSE:

$$
\text{MSE}=\frac{0.04+0.01+0.36}{3}=\frac{0.41}{3}=0.1367
$$

**Final answer:**
MAE = 0.300
MSE = 0.1367

**Why this is likely:** HW4 directly assigned these same kinds of loss calculations. 

---

## 8. Classification loss

**Question:**
For binary classification, let:

$$
y=$$0,\ 0,\ 1$$, \quad \hat y=$$0.1,\ 0.7,\ 0.9$$
$$

Which prediction is the worst and why from a cross-entropy perspective?

**Answer:**
The worst prediction is the second one: true label is 0, but predicted probability of 1 is 0.7. Cross-entropy penalizes confident wrong predictions heavily. The third prediction is good because the true label is 1 and the prediction is 0.9.

**Why this is likely:** HW4 asked students to compute log loss/cross-entropy and reason about classification outputs. 

---

## 9. Optimizers

**Question:**
A parameter has:

* current value (w_1 = 1.0)
* gradient (\frac{\partial L}{\partial w_1}=0.5)
* learning rate (\alpha=0.1)

Compute the next weight using **gradient descent**.

**Answer:**
$$
w_2=w_1-\alpha\frac{\partial L}{\partial w_1}
$$

$$
w_2=1.0-0.1(0.5)=1.0-0.05=0.95
$$

**Final answer:**
$$
w_2=0.95
$$

**Why this is likely:** HW4 asked students to compare gradient descent, momentum, and Adam on one update. A full Adam problem could appear, but plain gradient descent is more likely for a timed exam. 

---

## 10. Momentum vs Adam conceptual

**Question:**
What is the main difference between momentum and Adam?

**Answer:**
Momentum keeps a running average of past gradients to smooth updates and accelerate movement in consistent directions. Adam goes further by also keeping a running estimate of squared gradients, which gives it adaptive step sizes for different parameters.

**Why this is likely:** HW4 spent significant attention on update rules and their components. 

---

## 11. CNN fundamentals

**Question:**
What is the purpose of:

1. A convolutional layer
2. A pooling layer

**Answer:**

1. A **convolutional layer** applies filters to local regions of the input to detect useful patterns such as edges, shapes, or textures.
2. A **pooling layer** reduces spatial size, which lowers computation and can make the representation more robust.

**Why this is likely:** HW4 included CNN architecture reasoning and performance comparisons, even though MATLAB implementation details are unlikely to appear on the exam. 

---

## 12. RNN vs LSTM

**Question:**
Why is an LSTM often preferred over a basic RNN?

**Answer:**
An LSTM is designed to preserve useful information over longer time spans using gating and cell-state mechanisms. This helps reduce the vanishing-gradient problem that basic RNNs often struggle with.

**Why this is likely:** HW4 had students generate and run a basic LSTM, so a conceptual sequence-model question is very plausible. 

---

## 13. Tokenization

**Question:**
Why might engineering text use more tokens per sentence than everyday English?

**Answer:**
Engineering text often includes jargon, symbols, units, abbreviations, subscripts, code-like strings, and unusual character combinations. These are more likely to be split into multiple subword tokens, increasing token count compared with ordinary everyday language.

**Why this is likely:** HW5 focused heavily on tokenization of engineering text, math, units, jargon, and cost/context effects. 

---

## 14. Token cost / context window

**Question:**
Suppose a report has 6,000 input tokens and the API cost is $0.003 per 1,000 input tokens. What is the input cost to send the report once?

**Answer:**
$$
6000\text{ tokens} = 6 \times 1000
$$

$$
\text{Cost}=6 \times 0.003 = $0.018
$$

**Final answer:**
$$
$0.018
$$

**Why this is likely:** HW5 explicitly asked for context-window and token-cost calculations. 

---

## 15. Transformer attention

**Question:**
In the transformer attention equation

$$
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

what do (Q), (K), and (V) represent?

**Answer:**

* **Query (Q):** what the current token is looking for
* **Key (K):** what each token offers or contains
* **Value (V):** the information that gets combined into the output

The attention mechanism compares queries to keys to produce weights, then uses those weights to combine values.

**Why this is likely:** HW5 included transformer architecture and parameter reasoning; this is more exam-friendly than a giant full-parameter count. 

---

## 16. Transformer scaling term

**Question:**
Why do we divide by (\sqrt{d_k}) in scaled dot-product attention?

**Answer:**
As the key/query dimension gets larger, dot products can become large in magnitude. Dividing by (\sqrt{d_k}) keeps those scores from growing too much, which helps keep the softmax stable.

**Why this is likely:** This is a classic fair conceptual transformer question connected to the class material. 

---

## 17. Zero-shot vs few-shot

**Question:**
What is the difference between zero-shot and few-shot prompting?

**Answer:**

* **Zero-shot prompting** asks the model to perform a task with instructions only, without examples.
* **Few-shot prompting** includes a small number of examples showing the desired input-output pattern before asking the model to solve the new case.

**Why this is likely:** HW6 directly asked students to design an experiment comparing zero-shot and few-shot prompting. 

---

## 18. Prompt chaining

**Question:**
What is a prompt chain, and why can it be useful for engineering tasks?

**Answer:**
A prompt chain breaks a large task into smaller stages, where the output of one stage becomes the input to the next. This is useful for engineering tasks because it structures reasoning, reduces ambiguity, and makes it easier to separate analysis, diagnosis, and reporting.

**Why this is likely:** HW6 explicitly required a prompt-chain workflow for analyzing microcontroller power consumption. 

---

## 19. Tree-of-thought vs chain prompting

**Question:**
How is tree-of-thought prompting different from ordinary chain prompting?

**Answer:**
Chain prompting follows one reasoning path step by step. Tree-of-thought prompting explores multiple branches or candidate solutions, evaluates them, and may backtrack before choosing the best option. This can improve decision making when there are several plausible alternatives.

**Why this is likely:** HW6 directly asked students to explain how tree-of-thought differs from chain prompting. 

---

## 20. Multi-agent prompting

**Question:**
Give an example of a 3-agent workflow for an engineering proposal task.

**Answer:**
Example:

* **Agent 1: Problem Definition Agent** — defines the engineering problem, constraints, and motivation.
* **Agent 2: Technical Approach Agent** — proposes methods, models, or system design.
* **Agent 3: Reviewer/Critic Agent** — checks clarity, feasibility, risks, and completeness.

Information flows from problem framing, to solution design, to critique/refinement.

**Why this is likely:** HW6 ended with a multi-agent workflow for the EELE 491 final project. 

---

# Most likely “show your work” questions

If I had to narrow it to the most probable computational questions, I would bet on these five:

1. Confusion-matrix metrics
2. One MLP forward pass
3. One simple loss-function calculation
4. One gradient-descent parameter update
5. One token-cost or context-window calculation

Those are the cleanest fits for a fair 50-minute exam, and they map directly to repeated homework themes.    

# Less likely but still possible

These feel less likely, mainly because of time:

* full multi-step backprop numeric derivation,
* full Adam update with all bias-correction arithmetic,
* full transformer parameter-count problem,
* anything requiring MATLAB syntax or implementation details.

Those topics were in homework, but they are heavier than what usually fits a fair, timed, no-MATLAB exam.   


