import sys
sys.setrecursionlimit(3000)
def f(n):
    if n  < 10:
        return n
    else:
        return n ** 3 + f(n - 15)
print(f(1000) - f(940))