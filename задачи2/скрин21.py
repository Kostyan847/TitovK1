def wheremedian(nomer):
    n = sorted(nomer)
    l = len(nomer)
    m = l // 2
    if l % 2 == 0:
        mediana = (n[m - 1] + n[m]) / 2
    else:
        mediana = n[m]
    return mediana
nomer = [1,2,3,4,5]
mediana = wheremedian(nomer)
print(mediana)

