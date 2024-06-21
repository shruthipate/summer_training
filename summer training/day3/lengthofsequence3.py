'''ip="xyzabcdefklmnopqefgh"
op=7'''

s="abcde"
max_length=0
length=1
for i in range(1,len(s)):
    if ord(s[i])==ord(s[i-1])+1:
        length=length+1
    else:
        if length>max_length:
            max_length=length
        length=1
if length>max_length:
    max_length=length
print(max_length)
        