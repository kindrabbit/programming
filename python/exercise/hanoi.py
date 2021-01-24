# 汉诺塔hanoi tower
# 公式1：Tn = 2n + 1
# 公式2：Tn = 2的n次方-1
# 已知T1=1，T2=3, T3=7, T4=15

# 求T10要多少步骤

# 公式1：Tn = 2n + 1 求解
def hanoi(n):
    if n < 0:
        print("please input integer number.")
        return
    x = 0
    for i in range(n):
        x = 2 * x + 1
    return x

i = 1
while (i <= 10):
    print("共" + str(i) + "个盘子，需要", end="")
    print(hanoi(i), end="")
    print("步")
    i += 1

#公式2：Tn = 2的n次方-1求解
def hanoi2(n):
    x = 1
    for i in range(n):
        x = 2 * x
    x = x - 1
    return x
i = 1
while(i <= 10):
    print("共" + str(i) + "个盘子，需要", end="")
    print(hanoi2(i), end="")
    print("步")
    i += 1