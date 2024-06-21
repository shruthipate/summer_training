num=int(input())
count=0
for i in range(1,num+1):
    if(num%i)==0:
        count=count+1
if(count==2):
    print(i)
else:
    next=num+1
    while True:
        count=0
        for i in range(1,next+1):
            if(next%i)==0:
                count=count+1
        if(count==2):
            print(next)
            break
        next=next+1