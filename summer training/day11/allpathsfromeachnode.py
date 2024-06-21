
def least_cost(d1,l,x,e, c,m,l1):
    l.append(x)
    if x == e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d1[x]:
        if i[0] not in l:
            m,l1=least_cost(d1,l,i[0], e, c + i[1],m,l1)
    l.pop()
    return m,l1
d1={5:[(7,11),(3,10)],7:[(5,11),(4,12),(3,25)],4:[(7,12),(8,10),(2,13)],8:[(3,15),(4,10),(2,16)],3:[(3,10),(7,14),(8,15)],2:[(4,13),(8,16)]}
l=[]
for i in d1.keys():
    print("least cost",least_cost(d1,[],5,i,0,99999,[]))