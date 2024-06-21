"""
ip:  5
     0 1 0 0 1
     1 0 0 1 0 
     0 0 0 0 0 
     1 0 0 0 0 
     1 0 0 0 1

op:  5
"""


def fun(l,i,j,n,c): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return c
    if l[i][j]==1:
        l[i][j]=2
    c=fun(l,i-1,j,n,c)
    c=fun(l,i,j-1,n,c)
    c=fun(l,i+1,j,n,c)
    c=fun(l,i,j+1,n,c)
    return c
m=0
n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a)
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            k=fun(l,i,j,n,0)
            if(k>m):
                m=k
            count=count+1
print("ilands",count)
print(m)