def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,x-1):
            if x % i == 0:
                return False
        return True

print is_prime(4)
print is_prime(5)
