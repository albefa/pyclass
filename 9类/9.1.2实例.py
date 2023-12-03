class Dog:
    """一次模拟小狗的常识"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令的时候发出坐下动作"""
        print(self.name.title() + " 坐下！")

    def roll_over(self):
        """模拟小狗被命令的时候发出翻滚动作"""
        print(self.name.title() + " 翻滚！")


my_dog = Dog('wille', 6)
your_dog = Dog('serwen', 8)

print("My dog name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + "!")
my_dog.sit()
my_dog.roll_over()

print("Your dog name is " + my_dog.name.title() + ".")
print("Your dog's age is " + str(my_dog.age) + "!")

your_dog.sit()
your_dog.roll_over()
