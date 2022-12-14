class MysqlClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return f'user = {self.user}\npassword = {self.password}'


ob = MysqlClient(user='Vlad', password='Nikita')
print(ob)
