# 首先，创建一个待验证用户列表
# 和一个用于储存已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace', 'tom']
confirmed_users = []
# 验证每一个用户，知道没有未验证的用户为止。
# 将验证每个经过验证的用户移动到已验证的用户列表中
while unconfirmed_users:
    current_users = unconfirmed_users.pop()  # 这表示删除列表并获取最后一个元素
    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)
# 显示所有已验证的用户
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 例子其实是将一个列表的数据转移到另外一个列表中，例子中并没有实现验证的步骤。
