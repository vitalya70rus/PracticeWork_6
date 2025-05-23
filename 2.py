class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

Users = \
[
User('abc', 111),
User('def', 222),
User('ghi', 333),
User('jkl', 444),
User('mno', 555)
]

target_login = "mno"
target_password = 555

found_user = None
for user in Users:
    if target_login == user.login and target_password == user.password:
        found_user = user
        break

if found_user:
    print(f"Пользователь найден!\nЛогин: {found_user.login}\nПароль: {found_user.password}")
else:
    print(f"Пользователь с заданными логином {target_login} и паролем {target_password} - не найден!")