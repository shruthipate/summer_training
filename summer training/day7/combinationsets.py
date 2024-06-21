'''def com(l):
    t=[]
    n=len(l)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                t.append((l[i],l[j],l[k]))
    return t
l=[3,2,5,4,1,6,8]
x=com(l)
print(x)'''



    
    
''''def fun(l,k,current,res):
    if k==3:
        res.append(tuple(current))
        return
    for i in range(len(l)):
        fun(l,k + 1,current + [l[i]],res)
l = list(map(int,input().split(',')))
res = []
fun(l, 0, [], res)   
print(res)'''




def combi(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
combi(a,k)
    
    

    
    