# def find_big(arr):
#
#     for item in arr:
#         print(item)
#
#
# arr = [3, 2, 6, 1, 7, 4, 5]
# find_big(arr)


# def find_big(arr):
#     max = arr[0]
#     for item in arr:
#         if item > max:
#             max = item
#
#     print(max)
#     return max
#
# arr = [3, 2, 6, 1, 7, 4, 5]
# find_big(arr)
#
# print(max(1,2,3,4,5,6,7))

def find_big(arr):
    i = 0
    arr_len = len(arr)
    while i < arr_len or i <= 1:
        print("第" + str(i) + "个比较:")
        print(arr[i], end=" 比较 ")

        max_num = arr[i]
        if i + 1 < arr_len:
            print(arr[i + 1], end=" ")
            if arr[i + 1] > max_num:
                max_num = arr[i + 1]

        print("大的数是", max_num)

        i = i + 2

arr = [3, 2, 6, 1, 7, 4, 5]
find_big(arr)