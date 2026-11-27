import sys
sys.setrecursionlimit(3000)
def f(x, y):
    if x == 3 and y <= 65: return True
    if x == 3 and y > 65: return False 
    if y <= 65: return False
    
    if x % 2 == 0:
        return f(x + 1, y - 3) or f(x + 1, y - 5) or f(x + 1, y // 4)
    else:
        return f(x + 1, y - 3) and f(x + 1, y - 5) and f(x + 1, y // 4)
for y in range(66, 1000):
    if f(1, y):
        print(y)