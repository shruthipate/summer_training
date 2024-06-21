
#input:2 7 8
#output:5

def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def largep(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0

a=list(map(int,input().split()))
s=0
for i in range(len(a)-1):
    s=s+largep(a[i],a[i+1])
print(s)
    
    
    
    
    