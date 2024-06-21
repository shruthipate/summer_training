#missing number
n=int(input())
a=[0,5,3,6,7,2,17]
for i in range(n+1):
    if(i not in a):
        print(i)
        break
    