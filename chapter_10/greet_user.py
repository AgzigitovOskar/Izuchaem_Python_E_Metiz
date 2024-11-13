# Сохранение и чтение данных, сгенерированных пользователем

import json

# приветствует пользователя по ранее сохраненному имени:
filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f"Welcome back, {username}!")