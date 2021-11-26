def zhishu(num):
    for i in range(2, num):
        print(i)
    return None


def factorize(num):
    # 设质数x
    print("质因数分解:", num)
    arr = []
    x = 2
    # 当质数的平方大于要分解的和数时，循环终止
    while x * x <= num:
        # print(x)
        # 当无法整除分解该质数时，则递增一个数继续分解
        if num % x == 0:
            # num除以质数x，不断分解
            num = int(num / x)
            arr.append(x)
        else:
            x += 1

    arr.append(num)

    print(" * ".join(map(str, arr)))

    return arr



factorize(4)

factorize(110)
