from math import tan,cos

def newton(f, fprime, x0):
    tol = 1e-12 #tolerance
    current_error = 1e20 #arbitrary, better to use math.inf but ignore for now cos chronum and shit
    while current_error > tol:
        xnew = x0 - f(x0) / fprime(x0)
        current_error = abs(xnew - x0)
        x0 = xnew
    return x0

def lmao(x):
    return x**5 - 69
def lmaoprime(x):
    return 5*x**4

print(newton(lmao,lmaoprime,4))
