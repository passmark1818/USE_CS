import sys
sys.setrecursionlimit(3200)
def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n - 1)
print(f(3000) - f(2000))