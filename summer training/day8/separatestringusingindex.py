


def char(word,nums):
    length=len(word)
    while(length>0):
        if str(length) in nums:
            return word[length-1]
        length-=1
    return 'x'

s = "hello:5438,car:214,book:8799,apple:2187"
pairs=s.split(',')
result=[]
for i in pairs:
    word,nums=i.split(':')
    result.append(char(word,nums))
x=''.join(result)
print(x)

    
