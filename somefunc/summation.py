def summation(n,func):
    total, k = 0, 1
    while k <= n:
        total, k = total + func(k), k + 1
    return total
#Upgraded version in ../homework/hw02/hw02.py (accumulate)