def fun(d,x,cost):
    l.append(x)
    if(x==2):
        s.append(cost)
    if x in d:
        for i,c in d[x]:
            if i not in l:
                fun(d,i,cost+c)
    l.pop()
 
d={5:[(7,3),(3,1)],7:[(5,3),(4,4),(3,5)],4:[(7,4),(8,7),(2,8)],8:[(3,6),(4,7),(2,9)],3:[(5,1),(7,5),(8,6)],2:[(4,8),(8,7)]}
l=[]
s=[]
fun(d,5,0)
print(min(s))




