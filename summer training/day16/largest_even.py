def larg_even(l1, l2):
    digit1 = []
    for char in l1:
        if char.isdigit():
            digit1.append(char)
    
    digit2 = []
    for char in l2:
        if char.isdigit():
            digit2.append(char)
    
    c = digit1 + digit2
    unique_digits = list(set(c))
    unique_digits.sort(reverse=True)
    for i in range(len(unique_digits)-1,-1,-1):
        if int(unique_digits[i]) % 2 == 0:  
            even_digit = unique_digits.pop(i)
            break
    else:
        return "No even digit found"
    largest_number = ''.join(unique_digits) + even_digit
    return largest_number

l1 = "tu5g2k1h8"
l2 = "g5g8gd6h3"
print(larg_even(l1, l2))
#or
a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(c)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print(-1)





















