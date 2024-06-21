'''ip:5
1 word
1 word
3 wo
4 word
2 word
op:1
  false'''
  
n=int(input())
l=[]
res=[]
for i in range(n):
    x,y=input().split(' ')
    l.append([x,y])
print(l)
for i in l:
    if i[0]=='1':
        res.append(i[1])
    if i[0]=='2':
        if i[1] in res:
            print("True")
        else:
            print("False")
    if i[0]=='3':
        c=0
        for i in res:
            if i[1] in i:
                c=c+1
                break
        print(c)
    if i[0]=='4':
         new_res = []
         for word in res:
             if word != i[1]:
                 new_res.append(word)
         res = new_res