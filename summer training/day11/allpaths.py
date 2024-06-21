def fun(d,x):
    l.append(x)
    if(x==2):
        print(l)
    for i in d[x]:
        if(i not in l):
            fun(d,i)
    l.pop()
 
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(d,5)



