def improve(update, close, guess=1): 
    #close is a function used to judge whether number guess is satisfying enough,returning a Bool
    #update is a function used to somehow update the guess number,returning a number
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-15):
    #return True if x and y are close enough
    return abs(x - y) < tolerance

def newton_update(f, df):
    #using newton's method to update the guess number,returning a number
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def apply_twice(f, x):
    return f(f(x))

def make_adder(x):
    return lambda k : x+k

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

mymax = curry2(max)
def comparexwith3(x):
    return x == mymax(x)(3)