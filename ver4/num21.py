def f21(x, y):
    if (x == 3 or x == 5) and y <= 76: return True
    if x == 5 and y > 76: return False
    if y <= 76: return False

    if x % 2 == 0:
        return f21(x + 1, y - 3) or f21(x + 1, y - 5) or f21(x + 1, y // 4)
    else:
        return f21(x + 1, y - 3) and f21(x + 1, y - 5) and f21(x + 1, y // 4)

def f19(x, y):
    if x == 3 and y <= 76: return True
    if x == 3 and y > 76: return False
    if y <= 76: return False

    if x % 2 == 0:
        return f19(x + 1, y - 3) or f19(x + 1, y - 5) or f19(x + 1, y // 4)
    else:
        return f19(x + 1, y - 3) and f19(x + 1, y - 5) and f19(x + 1, y // 4)

for y in range(77, 1000):
    if f21(1, y) and not f19(1, y):
        print(y)
