# -------------------------------------------------------
# Gradient descent
# 
# ':=' mathematical assignment operator
# 
# Algorithm: 
# repeat until convergence {
#   θ_j := θ_j - α * ( d / d (θ_j)) J(θ_0, θ_1) for j = 0 and j = 1
# }
# 
# Learning Rate: α
# Derivative term: ( d / d (θ_j)) J(θ_0, θ_1) 
# 
# Correct Simultaneous update:
# temp0 := θ_0 - α * ( d / d (θ_0)) * J(θ_0, θ_1)
# temp1 := θ_1 - α * ( d / d(θ_1)) * J(θ_0, θ_1)
# θ_0 := temp0
# θ_1 := temp1
# 
# 
# -------------------------------------------------------