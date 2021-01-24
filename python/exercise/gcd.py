def gcd(x,y):
    if x > y:
        divisor = y
    else:
        divisor = x
    while divisor > 0:
        if x % divisor == 0 and y % divisor == 0:
            break
        divisor -= 1
    return divisor

print(gcd(15600,2400))