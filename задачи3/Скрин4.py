k='98hfgs64jf9b8ndh67k5g6g4f3m7'
l=0
k=k.split()
summ = 0
for i in k:
    if i.isdigit():
        summ+=int(i)
print(summ)
