# lowest common multiple
def lcm(x, y):
    max_number = x
    if y > max_number:
        max_number = y

    while (True):
        if (max_number % y == 0 and max_number % x == 0):
            result = max_number
            return result
        max_number += 1
    return result

# print( lcm(20, 13) )
# print( lcm(5, 20) )
# print( lcm(15, 27) )

# num1 = int(input("输入第一个数字："))
# num2 = int(input("输入第二个数字："))
# print(num1, "和", num2, "的最小公倍数是", lcm(num1, num2))

def lcm2(x, y):
    if x < y:
        max_number = y
        min_number = x
    else:
        max_number = x
        min_number = y

    result = -1

    # 小的是大的因数，直接返回大的
    if max_number % min_number == 0:
        result = max_number
        return result

    divisor = min_number
    # 第二种情况，有共同的约数
    while divisor > 1:
        if max_number % divisor == 0 and min_number % divisor == 0:
            result = int(max_number / divisor) * min_number
            # 或者
            # result = int(max_number / divisor) * min_number
            return result
        divisor -= 1

    # 第三种情况，两者没有公因数
    result = min_number * max_number
    return result

# 24
print(lcm2(12, 8))
# 108
print(lcm2(27, 36))
# 336
print(lcm2(48, 28))
# 50
print(lcm2(50, 25))
# 36
print(lcm2(36, 9))
# 456
print(lcm2(76, 24))
print(lcm2(2, 7))
