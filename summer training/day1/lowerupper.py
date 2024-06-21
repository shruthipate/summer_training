s="f46feLK9y56u#@&56hIjbn6KJhA"
uv,uc,lv,lc,d,sp=0,0,0,0,0,0
for i in s:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    
print(uv)
print(uc)
print(lv)
print(lc)
print(d)
print(sp)
        
        
        