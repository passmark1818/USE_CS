import sys
sys.setrecursionlimit(3000)
def f(n):
    if n < 10:
        return n
    else:
        return n**3 + f(n - 11)
print(f(900) - f(856))