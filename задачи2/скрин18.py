k = 'strochechka'
def lang(k):
    i = 0
    for char in k:
        if char == 'k':
            k = k[:i] + '4' + k[i + 1:]
        elif char == 'o':
            k = k[:i] + '3' + k[i + 1:]
        i += 1
    print(k)
    return k
lang(k)
