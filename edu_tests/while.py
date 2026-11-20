def clean_string(text):
    start = 0
    end = len(text) - 1
    while start <= end and text[start] == "#":
        start += 1
    while end >= start and text[end] == "#":
        end -= 1
    return text[start:end + 1]

print(clean_string("###Subnautica#Python###"))