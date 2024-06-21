
'''def decypted(s,n):
    text=""
    for i in s:
        if i.isalpha():
            char=chr((ord(i)-n-97)%26+97)
            text=text+char
        else:
            text=text+i
    return text
                     
s=input()
n=int(input())
at=decypted(s,n)
print(at)'''



a="bvec"
b=30
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
         d=d+chr(ord(i)-c+26)
print(d)
    
        
    
    
    

    
    