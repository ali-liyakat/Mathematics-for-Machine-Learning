from scipy.integrate import quad # "quadrature" = numerical integration (as opposed to symbolic)



# f(x) = x/2
# integration over limit 1,2 of f(x) = 3/4
def g(x):
    return x/2

print(quad(g, 1, 2) )


# fx = 2x
# integration over limit 3,4 of f(x) = 7

def f(x):
    return 2*x

print(quad(f, 3, 4))