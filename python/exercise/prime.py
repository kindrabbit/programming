number = input('please input a number:')
number = int(number)
print("你输入的数字是：", number)
print("其中包含的质数有：")
for x in range(1, number):
    if x < 2:
        continue
    if x != 2 and x % 2 == 0:
        continue
    if x != 3 and x % 3 ==0:
        continue
    if x != 5 and x % 5 == 0:
        continue
    if x != 7 and x % 7 ==0:
        continue
    
    n = 10
    # print("x=" + str(x) + " n=" + str(n))
    while n < x:
        n += 1
        if x % n == 0:
            break

    if x == 2:
        print(x, end="")
    else:
        print(", ", x, end="")
