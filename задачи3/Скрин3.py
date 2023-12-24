k=[,2,3,4,5,6,7,8,9,10]
def black(k):
    if sum(k)>21:
        return(True)
    if sum(k)<=21:
        return(False)
print(black(k))
