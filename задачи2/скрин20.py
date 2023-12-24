a=[1, 2, 9, 21, 39, 67]
for i in range (len(a)):
    if a[i]!=a[-1] and a[i] < a[i+1]:
        print ("вверх")
    elif a[i]==a[-1] and a[i] > a[i-1]:
        print ("вверх")    
    else:
        print ("нет")
        break
