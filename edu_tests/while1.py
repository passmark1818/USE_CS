def shrink_string(text):
    while len(text) > 3:
        text = text[1:-1]
    return text
print(shrink_string("difjvbnfijvnb"))
        