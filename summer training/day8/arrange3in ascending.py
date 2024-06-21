# input:1 4 2 7 4 6 9 7
#output:[1, 2, 4, 4, 6, 7, 7, 9]
a=list(map(int,input().split()))
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
        
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
        
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)
    