# 先空白字典，后加入输入内容，再后打印出来(不能弄混列表和字典)
dream_places = {}
# 设置标志
place_active = True
while place_active:
    name = input("\n请输入的名字: ")
    place = input("a你喜欢去的地方: ")
    # 将答案存在字典中
    dream_places[name] = place
    # 是都继续调查
    repaet = input("还要继续调查么？（y/n）")
    if repaet == 'n':
        place_active = False
print("调查结束")
for name, place in dream_places.items():
    print(name.title() + " 喜欢去的地方是 " + place.title() + ".")
