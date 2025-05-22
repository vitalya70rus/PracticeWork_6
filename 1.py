string_names = ("Дмитрий, Никита, Владислав, Андрей, Валерий, Алексей, Максим, Кирилл, Эдуард, Александр")
list_names = string_names.split(", ")
print(list_names)

a = 0
for name in list_names:
    if name[0] != 'А':
        a += 1
    elif name[0] == 'А':
        list_names.pop(a)
        a += 1
print(list_names)