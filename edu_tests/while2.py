def rotate_and_find(text, target):
    l = len(text)
    count = 0
    if text == target: return(0)
    while l >= count:
        x = text[:-1]
        y = text[-1:]
        text = y + x
        count += 1
        if text == target:
            return(count)
        elif count == l:
            return(-1)

print(rotate_and_find('abc', 'abc'))