"""
十进制转二进制，用数除以2得余数，最后得数小于等于1的时候 ，将得数与余数连在一起
  12
2 6 0
2 3 0
2 1 1

1 1
2 10
3 11
4 100
5 101
6 110
7 111
8 1000
9 1001
10 1010
11 1011
12 1100
"""


def ten2two(num):
    arr = []
    while True:
        # 当前数每次除以2
        # 得到余数
        arr.append(str(num % 2))
        num = num // 2
        if num == 0:
            break
    # 倒序输出
    return "".join(arr[::-1])

def tenTotwo(num):
    arr = []
    while num >= 1:
        # 当前数每次除以2
        # 得到余数
        reminder = int(num % 2)
        arr.insert(0, reminder)
        num = int(num / 2)
    return arr

# 方法1
print(ten2two(39))

# 方法2
print(tenTotwo(12))


def pow(num, p):
    result = 1
    for x in range(p):
        result = num * result
    return result

print(pow(2, 0))
