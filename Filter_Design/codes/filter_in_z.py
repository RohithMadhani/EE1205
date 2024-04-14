import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.282e-5 * s**4 / (s**8 + 0.169*s**7 + 3.816*s**6 + 0.4831*s**5 + 5.4249*s**4 + 0.4563*s**3 + 3.404*s**2 + 0.143*s + 0.796)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


