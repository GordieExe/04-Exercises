def f(x):
    return x**2 - 2

def compute_root(f, x0, x1, tol, max_it):
    f0 = f(x0)
    f1 = f(x1)

    # Check that the root is bracketed
    if f0 * f1 > 0:
        raise ValueError("Function does not change sign on the interval.")

    for it in range(1, max_it + 1):
        xm = 0.5 * (x0 + x1)
        fm = f(xm)

        # Check tolerance condition
        if abs(x1 - x0) < tol:
            return xm, fm, it

        # Decide which subinterval to keep
        if f0 * fm < 0:
            x1 = xm
            f1 = fm
        else:
            x0 = xm
            f0 = fm

    # If max iterations reached
    return xm, fm, max_it

x, f_x, num_it = compute_root(f, x0=0, x1=2, tol=1e-6, max_it=1000)

print("Approximate root:", x)
print("f(x) =", f_x)
print("Iterations:", num_it)
