# Задача №19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# list_nums = [1, 2, 3, 4, 5]
# k = 7
# print(list_nums)
# result = list_nums[(k % len(list_nums)):] + \
#     list_nums[:(k % len(list_nums))]
# print(result)


# list_1 = [1, 2, 3, 4, 5]
# k = 3
# i = 0
# while i < k:
# x = list_1.pop(0)
# list_1.append(x)
# i += 1
# print(list_1)

list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1[k:] + list_1[:k])

list_nums = [1, 2, 3, 4, 5]

num = int(input())
n = len(list_nums)

for i in range(0, num % n):
    list_nums.insert(0, list_nums.pop(-1))

print(list_nums)