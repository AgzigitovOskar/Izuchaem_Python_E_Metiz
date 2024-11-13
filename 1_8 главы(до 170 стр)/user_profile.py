# Использование произвольного набора именованных аргументов стр_162

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics',
                            field_2 ='physics_2',
                            fdc = '1')
print(user_profile)