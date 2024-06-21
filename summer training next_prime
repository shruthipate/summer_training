def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

num = 5
if is_prime(num):
    print(num)
else:
    print(next_prime(num))
