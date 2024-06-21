l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
while(i<len(l1) and j<len(l2)):
        if l1[i]<l2[j]:
            i=i+1
            l3.append(i)
        j=j+1
        l3.append(j)
print(l3)