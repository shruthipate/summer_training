jo=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=[5,6,5,4,11,2]
for i in range(1,len(jo)):
    for j in range(0,i):
        if(jo[j][1]<=jo[i][0]):
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]
        
print(max(b))
                
        
        