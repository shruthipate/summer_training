l=input()
count=1
l1=''
for i in range(len(l)-1):
    if(l[i]==l[i+1]):
        count=count+1
    else:
        l1=l1+l[i]+str(count)
        count=1
l1=l1+l[i]+str(count)
print(l1)
        