'''n1=int(input())
n2=int(input())
l=[]
l2=[]
for i in range(1,n1+1):
    if n1%i==0:
        l.append(i)
print(l)
for j in range(1,n2+1):
    if n2%j==0:
        l2.append(j)
print(l2)'''


a=7
b=8
for i in range(2,(min(a,b)//2)+1):
    if a%i==0 and b%i==0:
        print("not co prime")
        break
else:
    print("coprime")
        