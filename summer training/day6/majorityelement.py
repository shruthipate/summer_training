'''l=[4,8,2,4,4,8,4]
l.sort()
x=len(l)
print(l[x//2])'''
a=[1,1,2,1,1,3]
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)