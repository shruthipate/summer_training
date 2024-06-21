'''input:5
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
output:true
       false
       true
-----------------
input:
1 car
1 cap
2 ca
3 ca
1 can
3 ca
2 cap
output:
false
true
true
true
----------------------'''
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
        found = False
        for i in res:
            if i[1] in i:
                found = True
                break
        if found:
            print("True")
        else:
            print("False")
print(res)







