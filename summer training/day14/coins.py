l=[1,3,4,5]
r=17
m=[-1]*(r+1)
m[0]=0
for i in l:
    for j in range(1,r+1):
        if j>=i:
            if m[j-i]!=-1:
                if m[j]!=-1:
                    m[j]=min(m[j],m[j-i]+1)
                else:
                    m[j]=m[j-i]+1

print(m[-1])