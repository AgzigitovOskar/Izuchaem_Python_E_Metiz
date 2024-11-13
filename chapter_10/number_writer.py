# Функции json.dump() и json.load()

import json


# json.dump() используется для сохранения списка чисел:
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)