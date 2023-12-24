a=input()
b=input()
if a==b:
    print('Draw')
else:
    if a=='paper':
        if b=='rock':
            print('1 Won!')
        else:
            print('2 Won!')
    if a=='rock':
        if b=='paper':
            print('2 Won!')
        else:
            print('1 Won!')
    if a=='scissors':
        if b=='paper':
            print('1 Won!')
        else:
            print('2 Won!')
