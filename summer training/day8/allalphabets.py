#check if all alphabets present 
st="the 4quick br$^own foENDx jumps over the lazy dog"
c=0
s=set(st)
'''s=set(str)
if len(s)==27:
    print("yes")
else:
    print("no")'''

for i in s:
    if i.islower():
        c=c+1
if(c==26):
    print("yes")
else:
    print("no")
    
        