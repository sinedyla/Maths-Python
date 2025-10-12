def derive(f,x,a):
    lim = (f(x+a) - f(x)) / ((x + a) - x)
    return lim

def f(x):
    return x ** 2

print(derive(f,2,0.001))