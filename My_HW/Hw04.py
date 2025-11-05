import numpy as np

# Function definition
def f(x):
    return np.sin(x) * np.cos(x)

# Numerical integration using Trapezoidal Rule
def trapezoidal_rule(a, b, n):
    x_values = np.linspace(a, b, n + 1)  # Generate n+1 points
    y_values = np.abs(f(x_values))  # Take absolute values
    h = (b - a) / n  # Step size

    # Apply trapezoidal rule
    area = (h / 2) * (y_values[0] + 2 * sum(y_values[1:-1]) + y_values[-1])
    return area

# Define interval and number of subintervals
a, b = 0, 4 * np.pi
n = 1000  # More points increase accuracy

# Compute area
area = trapezoidal_rule(a, b, n)
print("Approximated Area:", area)
