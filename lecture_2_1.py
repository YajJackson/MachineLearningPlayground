# -------------------------------------------------------
# Linear regression with one variable

# m = Number of training examples
# x = 'input' variable/ features
# y = 'output' variable / 'target' variable

# Hypothesis: h(x) = θ_0 + θ_1(x) + θ_n(x^n-1) 

# Minimize (h(x) - y)^2
# where h(x) is the prediction,
# and y is the actual

# J is the cost function/ squared error function:
# J(θ_0, θ_1) = 1 / 2(m) Σ_i=1_m (h(x^i) - y^i)^2 

# Training set of housing prices
# Size in Feet^2 (x) | Price ($) in 1000's (y)
# -------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

set = [
  [2104, 1416, 1534, 852],
  [460, 232, 315, 178]
]

h = lambda x, m: m*x

cost = lambda s, m: sum(map(lambda x, y: (h(x, m) - y) **2, s[0], s[1])) / (2*len(s[0]))

num = 100
t = 1
i = .1
d = t + i

for n in range(num):
  if cost(set, t) > cost(set, d):
    t = d
    d += i
  else:
    d -= i

print(f'Coeficient: {t} \nCost: {cost(set, t)}')

r = np.arange(0, 3000, 1)
plt.plot(r, h(r, t), 'r--', set[0], set[1], 'bo')
plt.show()