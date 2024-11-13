filename = 'pi_digits.txt'

# Чтение по строкам
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# Создание списка строк по содержимому файла
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())