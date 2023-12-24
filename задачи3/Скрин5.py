a='+a+b+k+m+gm+'
l=[]
g=0
k=1
for i in range (len(a)):
    if a[i]!='+':
        if a[i-1]=='+' and a[i+1]=='+':
            l.append(g)
        else:
            l.append(k)
s=sum(l)
if s==0:
    print('True')
else: 
    print('False')
