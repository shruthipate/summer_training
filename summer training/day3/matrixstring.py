n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("no")
        break
else:
    print("yes")
        
    
    
    
    
    
    
    
    