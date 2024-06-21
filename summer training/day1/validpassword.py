n=input()
u,l,s,d=0,0,0,0
for i in n:
    if(i.isdigit()):
        d=1
    elif(i.islower()):
        l=1
    elif(i.isupper()):
        u=1
    else:
        s=1
m=4-(u+l+d+s)
if(len(n)+m)<8:
    print(8-len(n))
elif m == 0 and len(n) >= 8:
    print(-1) 
else:
    print(m)