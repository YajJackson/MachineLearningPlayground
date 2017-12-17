import matplotlib.pyplot as plt
# Linear regression with on variable

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


set = [
  [2104, 1416, 1534, 852],
  [460, 232, 315, 178]
]

plt.plot(set[0], set[1], 'ro')
plt.show()

