x=input()
s=[]
for i in range(len(x)):
    if x[i]=="(" or x[i]=='[' or x[i]=='{':
        s.append(i)
    elif x[i]==']' and s[-1]=='[':
        s.pop()
    elif x[i]=='}' and s[-1]=='{':
        s.pop()
    elif x[i]==')' and s[-1]=='(':
        s.pop()
    else:
        print(i,"not balanced")
if(len(s)==0):
    print("balanced")