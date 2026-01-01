import math

def function(x):
    return 3*x**4 + 2*x**3 + x**2 - 2*x - 1 #Given Equation

# Bisection method implementation
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None  # No root in this interval

    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2.0
        f_mid = f(midpoint)
        
        if f_mid == 0 or (b - a) / 2.0 < tol:
            return midpoint  # Root found or within tolerance
        elif f(a) * f_mid < 0:
            b = midpoint  # Root is in left half
        else:
            a = midpoint  # Root is in right half
        
        iter_count += 1
    
    return (a + b) / 2.0  # Approximate root

# Function to find all roots in a given interval and return an array of roots
def find_roots_in_interval(f, a, b, interval_step, tol=1e-6):
    roots = []
    x = a
    while x < b:
        next_x = min(x + interval_step, b)
        root = bisection_method(f, x, next_x, tol)
        if root is not None:
            rounded_root = round(root, 2)
            if rounded_root not in roots:  # Avoid duplicate roots
                roots.append(rounded_root)
        x = next_x
    return roots

# Example use case
if __name__ == "__main__":
    # Define the interval and tolerance
    left = 0
    Right = 3
    tol = 1e-6
    interval_step = 0.5  # Step size to divide the interval

    # Find all roots in the given interval
    roots = find_roots_in_interval(function, left, Right, interval_step, tol)
    if 1 > len(roots):
        print(f"Roots of the given function are: {roots}")
    else:
        print(f"Root found for 3x^4+2x^3+x^2-2x-1 in [0, 3] is {roots[0]}")