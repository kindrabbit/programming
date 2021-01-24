# 切1刀2块, 2刀4块，3刀7块， 4刀11块
# 每一刀是上次的所分的块数加上刀数
def pizza(n):
    if n < 0:
        print("pease input integer number")
        return
    # 没切之前是一个整体，赋值为1
    x = 1
    # 从1刀开始每加一刀都是上一次的结果+当前刀数
    n = n + 1
    for i in range(1, n):
        x = x + i
    return x

i = 1
while (i <= 12):
    print("切了" + str(i) + "刀,分成", end="")
    print(pizza(i), end="")
    print("块")
    i += 1