# num = float (input("请输入一个数字："))
# num_sqrt = num ** 0.5
# print (" %0.3f 的平方根是 %0.3f" % (num,num_sqrt))

def approximate(a, b):
    flag = 0.001
    # 求近似相等，两个数的绝对值除以小的那个
    # 当得数小于设定的差值时表示接近
    return abs(a - b) / min(a, b) < flag

print(
approximate(15, 15.001)
)


def square(num):
    x = 1
    # 牛顿连续逼近法，选一个猜测数x
    # 当x不是完全平方根且这个x的平方与num不近似时
    # x赋值为新的猜测数，新的猜测数为x+num/x的平均值
    while x * x != num and approximate(num, x * x) is not True:
        print("x=" + str(x) + " num=" + str(num))
        x = (x + num / x) / 2

    print(str(x) + " * " + str(x) + " ~= " + str(num))
    return x


print(square(15))