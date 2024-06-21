# n=input()
# l=[('L',2),('R',3),('L',1)]
# s=""
# for i in range(3):
#     if l[i][0]=='L':
#         x1=l[i][1]
#         s=s+n[x1]
#     if l[i][0]=='R':
#         x1=l[i][1]
#         s=s+n[-x1]
# print(s)
# 

a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
print(str)
str=list(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no")