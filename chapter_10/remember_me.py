# Начнем с сохранения имени пользователя:
import json


# username = input("What is your name? ")
# filename = 'username.json'
#
# with open(filename, 'w') as f:
#     json.dump(username, f)
# print(f"We'll remember you when you come back, {username}!")
# _________________________________________

# # Программа загружает имя пользователя, если оно было сохранено ранее.
# # В противном случае она запрашивает имя пользователя и сохраняет его.
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")
#__________________________________________


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()







