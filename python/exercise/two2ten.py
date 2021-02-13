"""
二进制转十进制算法
1、从右往左数，第1个数字编号为0，第2个为1，以此类推得到每个数字的编号
2、计算每个数乘以2的编号次方
3、然后将所有的结果求和

例如：100111
1、从右往左得到编号：1(5) 0(4) 0(3) 1(2) 1(1) 1(0)
2、计算每个数字乘以2的编号次方：1 * 2^5 、数字0无需计算、1 * 2^2、1 * 2^1、1 * 2^0
3、求和：1 * 2^5 = 32， 1 * 2^2 = 4， 1 * 2^1 = 2,  1 * 2^0 = 1，结果相加为：32 + 4 + 2 + 1 = 39

验证：
39 / 2 = 19  余 1
19 / 2 = 9   余 1
9  / 2 = 4   余 1
4  / 2 = 2   余 0
2  / 2 = 1   余 0

当数字小于等于1时，将剩余数字与余数自下往上相连组合为：100111

"""

def two2ten(num):
    result = 0
    times = 0
    no = 0
    while num >= 1:
        no = int(num % 10)
        num = int(num / 10)
        # 求幂
        # 当前次方的值，当次方是0的时候，为1
        power = 1
        time = times

        if time == 0:
            power = no * power

        while time > 0 and no > 0:
            power *= 2
            time -= 1

        power = no * power
        print(no, " * 2^", times, " = ", power)
        result += power

        # 判断条件
        times += 1

    return result

#
print("two2ten:", two2ten(100111))


def pow1(a, b):
    power = 1
    while b > 0:
        power *= a
        b -= 1
    return power

def two2ten1(num):
    result = 0
    times = 0
    no = 0
    while num >= 1:
        no = int(num % 10)
        num = int(num / 10)
        power = no * pow1(2, times)
        print(no, " * 2^", times, " = ", power)
        result += power
        # 判断条件
        times += 1

    return result


print("two2ten1:", two2ten1(100111))


# 换一个计算方式，分两步骤
def two2ten2(num):
    result = 0
    times = 0
    no = 0
    while num >= 1:
        no = int(num % 10)
        num = int(num / 10)

        # 求幂
        # 当前次方的值，当次方是0的时候，为1
        power = 1
        time = times
        # 当次方大于0的时候， 次方个2相乘
        while time > 0:
            power *= 2
            time -= 1

        # 当前数字乘以次方结果求和
        power = no * power
        print(no, " * 2^", times, " = ", power)

        result += power

        # 判断条件
        times += 1

    return result


print("two2ten2:", two2ten2(100111))
