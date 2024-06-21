
def is_palindrome(n):
    num=str(n)
    if len(num)<=1:
        return True
    if num[0]==num[-1]:
        return is_palindrome(num[1:-1])
    else:
        return False

n=int(input())
if is_palindrome(n):
    print("pal")
else:
    print("not")