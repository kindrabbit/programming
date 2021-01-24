data = [1,2,3,4,5,6,7,8,9,10]

#
#for item in data:
#    print(item)


# for x in range(1, 101):
#     print(x, end=' ')

# x = 1
# while (x <= 100):
#     print(x, end = " ")
#     x += 1

# 方法1，先等差求得总数，然后减去偶数和。偶数和是奇数和+100再除以2
# y = 100
# z = ((1+y)*y)/2
# a = (z-(y/2))/2
# print("奇数和:",  int(a))

# 方法2，利用等差数列求和公式
# number = ( (2 + 100) * 50 ) / 2
# print("偶数和:", number)

# 方法3，累加
count = 0
for number2 in range(1, 101):
    # if number2 % 3 != 0 and str(number2).endswith("3") != True:
    # if number2 % 3 != 0 and str(number2).find("3") < 0:
    if number2 % 10 != 3 and number2 % 3 != 0 and (number2 / 3 < 10 or number2 / 3 > 13):
        count = count + number2
        print(number2, count)
