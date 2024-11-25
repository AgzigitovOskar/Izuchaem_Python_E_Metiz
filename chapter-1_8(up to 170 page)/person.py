# def build_person(first_name, last_name):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
# musician = build_person('jimi', 'hendrix')
# print(musician)


def build_person(first_name, last_name, age=None):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician_age = build_person('jimi', 'hendrix', age=27)
musician = build_person('jimi', 'hendrix')
print(musician_age)
print(musician)