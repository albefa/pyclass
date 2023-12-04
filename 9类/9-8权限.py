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


class Admin(User):
    """admin的类，继承User ，并拥有超级权限"""

    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]


class Privileges:
    """只有一个属性 """

    def __init__(self, privileges=None):
        """储存三个权限字符串"""
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\n你好，管理员,你的权限是： ")
        if self.privileges:
            for priviledge in self.privileges:
                print(f"-{priviledge}")
        else:
            print("-THis user has no privileges.")





a_admin = Admin('acv', 'BB', '20')
a_admin.descibe_name()
a_admin.privileges.show_priviledges()
print("增加权限")
a_admin_priviledges = [
    'can add post',
    'can delete post',
    'can ban user', ]
a_admin.privileges.privileges = a_admin_priviledges
a_admin.privileges.show_privileges()
