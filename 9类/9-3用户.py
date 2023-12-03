class User:
    """关于用户的类"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def descibe_name(self):
        """用户摘要"""
        full_name = self.first_name.title() + self.last_name.title()
        print("\n用户名： " + full_name)

    def greet_user(self):
        """问候用户"""
        full_name = self.first_name.title() + self.last_name.title()
        print(full_name + "您好！")


a_users = User('bob', 'tom')
a_users.descibe_name()
a_users.greet_user()

b_user = User('cc', 'silna')

b_user.descibe_name()
b_user.greet_user()
