a=[9, 3, 4]
b=[2, 7, 6]
c=[8, 10, 2]
l=1
m=1
n=1
def box(a,b,c,l,m,n):
    for i in a:
        l=l*i
    for i in b:
        m=m*i
    for i in c:
        n=n*i
    v=l+m+n
    print(v)
box(a,b,c,l,m,n)
