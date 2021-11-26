number = input('please input a number:')
number = int(number)
print("你输入的数字是：", number)

# 直角三角形星
def print_star(x):
    for n in range(x + 1):
        for m in range(n):
            print("*", end=" ")
        print(" ")

# 正方形星
def print_star2(x):
    for n in range(x):
        for m in range(x):
            print("*", end=" ")
        print(" ")

# 等边三角形
def print_star3(x):
    if x % 2 == 0:
        x = x + 1

    rows = int((x + 1) / 2)
    print('你输入的数字:', x, '。换算得到的行数:', rows)
    for n in range(rows):
        # 每行星星数量等于x-总行数减去(当前行+1)的两倍
        # print('当前行的星星数量:', x - (rows - (n + 1)) * 2)
        space_number = rows - (n + 1)

        for a in range(space_number):
            print(".", end=" ")
        for b in range(x - space_number * 2):
            print("*", end=" ")
        for c in range(space_number):
            print(".", end=" ")
        print(" ")



# 等边三角形2
def print_star4(x):
    if x % 2 == 0:
        x = x + 1

    rows = int((x + 1) / 2)
    star = 1
    print('你输入的数字:', x, '。换算得到的行数:', rows)
    for n in range(rows):
        print('当前行的星星数量:', star)
        left = int((x - star) / 2)
        right = star + left
        # print("left", left, "right", right)
        for m in range(x):
            if m < left or m >= right:
                print('.', end=" ")
            else:
                print('*', end=" ")

        star = star + 2
        print(" ")



print("==================")
print("# 直角三角形星")
print_star(number)

print("==================")
print("# 正方形星")
print_star2(number)
# print("其中包含的质数有：")

'''
---*---
--***--
-*****-
*******
'''
print("==================")
print("# 等边三角形1")
print_star3(number)

print("==================")
print("# 等边三角形2")
print_star4(number)

