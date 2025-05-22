class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

user_1 = User('abc', 111)
user_2 = User('def', 222)
user_3 = User('ghi', 333)
user_4 = User('jkl', 444)
user_5 = User('mno', 555)

if user_1.login == 'abc' and user_1.password == 111:
    print(user_1.login)
    print(user_1.password)