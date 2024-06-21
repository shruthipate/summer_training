def sum_even(n):
    if n < 1:
        return 0
    elif n % 2 == 0:
        return n + sum_even(n - 1)
    else:
        return sum_even(n - 1)

result = sum_even(10)
print(result)






