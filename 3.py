def mul_to_int(a, b):
    p = a * b
    if float(p).is_integer():
        return int(p)
    return p
print(mul_to_int(1.5,2))
