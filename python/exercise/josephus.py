""" 约瑟夫变种问题
# 约瑟夫josephus ring环，是全部囚犯围成1个环状，从某个点算起，每隔2人杀1人，直到最后剩下2人可以活命。
# 标准环解法:
# 按圆环排列，按数量循环报数，报到是几号的则移除，然后重新继续报数
https://www.cnblogs.com/divablogs/p/7511950.html
https://blog.csdn.net/qq_41376740/article/details/79677823
"""


def josephus(num=41, kill_num=3, remain=1):
    # num 总人数
    # kill_num 报数第几的是要被杀的人
    # remain 最后可剩余几人
    people_list = list(range(1, num + 1))

    if num == 1 or kill_num == 1:
        print('No.%d is survival.' % people_list[-1])

    while True:
        if kill_num < len(people_list) and len(people_list) > remain:
            print('num < len No.%d had been killed.' % people_list[kill_num - 1])
            people_list = people_list[kill_num:] + people_list[:kill_num - 1]

        elif kill_num == len(people_list) and len(people_list) > remain:
            print('num = len No.%d had been killed.' % people_list[-1])
            people_list = people_list[:kill_num - 1]

        elif kill_num > len(people_list) and len(people_list) > remain:
            sub = kill_num
            while sub > len(people_list):
                sub = sub - len(people_list)
                if sub > 0 and sub <= len(people_list):
                    print('num > len No.%d had been killed.' % people_list[sub - 1])
                people_list = people_list[sub:] + people_list[:sub - 1]

        else:
            print('最后剩余的原始编号:', people_list)
            break


josephus(10, 2)

josephus(41, 2, 2)

josephus(41, 5, 2)

"""
# 这里有个变种问题，来自《具体数学》第7页。
# 一个数字圆环，每隔1个删除1个数字，直到最后剩下2个数字停止
## 1. 每一次都是删除双数，每一轮结束后从剩余里面的双数开始删除
## 2. 如果当前圆环数量是双数，则除以2是要删除的数量，即完成1轮
## 3. 如果当前圆环是单数，则数量+1除以2是删除的数量，即完成1轮
"""
def josephus2(num=41, kill_num=2, remain=2):
    people_list = list(range(1, num + 1))
    while remain <= len(people_list):
        if len(people_list) > kill_num and len(people_list) > remain:
            print("removed:", kill_num, people_list[kill_num - 1])
            people_list = people_list[kill_num:] + people_list[:kill_num - 1]
        elif kill_num == len(people_list) and len(people_list) > remain:
            print('>> No.%d had been killed.' % people_list[-1])
            people_list = people_list[:kill_num - 1]
        else:
            print("reminder:", people_list)
            break

# josephus2(41)

# list1 = [1,2,3,4,5]
# del list1[3-1]
# print(list1)
#
# list2 = [1,2,3,4,5]
# list2 = list2[:3-1] + list2[3:]
# print(list2)
#
# def josephus3(num=41, kill_num=2, remain=2):