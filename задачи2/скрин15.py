
a='98, 2, 40, 86'
d=1
l=[]
def cjl(a,d):
   for i in range(len(a)):
       if a[i]!=" " and a[i]!=",":
           n=int(a[i])
           l.append(n)      
   print(l)   
   for i in l:
       d=d*i
   print(d)
cjl(a,d)
