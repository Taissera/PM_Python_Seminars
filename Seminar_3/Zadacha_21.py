# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#     {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]
# set_1 = set()
# for i in list_1:
#     for v in i.values():
#     # set_1.add(v.replace(' ', ''))
#     set_1.add(v.strip())
# print(set_1)
mas = [0, -1, 5, 2, 3]
count = 0
for i in range(len(mas)-1):
    if mas[i+1] > mas[i]:
        count += 1
print(count)