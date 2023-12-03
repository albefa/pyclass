class User:
    """关于用户的类"""

    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def descibe_name(self):
        """用户摘要"""
        full_name = self.first_name.title() + self.last_name.title()
        print("\n用户名： " + full_name)

    def greet_user(self):
        """问候用户"""
        full_name = self.first_name.title() + self.last_name.title()
        print(full_name + "您好！")

    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登陆次数0"""
        self.login_attempts = 0

    def read_login_number(self):
        """"返回登陆次数"""
        print("登陆次数是：" + str(self.login_attempts))  # str文本模式


b_users = User('aa', 'bb', 20)
b_users.greet_user()
print("初始登陆次数")
b_users.read_login_number()
print("增加后次数")
b_users.increment_login_attempts()
b_users.read_login_number()
print("重置登陆次数")
b_users.reset_login_attempts()
b_users.read_login_number()
