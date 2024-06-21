#N-Queens with rook
def queen(r):
    if(r==n):
        return
    for c in range(n):
        if(check(r,c)):
            m[r][c]=1
            break
    return queen(r+1)
def check(i,j):
    if(i==u):
        return 0
    if(j==v):
        return 0
    r=i
    c=j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
queen(0)
print(m)
