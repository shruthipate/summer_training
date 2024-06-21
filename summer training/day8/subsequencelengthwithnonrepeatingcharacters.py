a="abfgresagtyuiofds"
d={}
s=""

i=0
m=0
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i+=1
    i=d[a[i]]
print(m)