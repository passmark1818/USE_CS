import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 15
    else:
        return 2 * f(n - 1) - n
print((f(2025) - f(2023) - 2) / 2 ** 2022)