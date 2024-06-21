'''input:122
output:131 if it palindrome print palindrome if not print next close palindrome number
def palin(n):
    o=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return o==rev
def next_palin(n):
    while not palin(n):
        n=n+1
    return n
num=24
res=next_palin(num)
print(res)'''
'''input:abdbsdabca
output:bdb'''







