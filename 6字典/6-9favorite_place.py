#喜欢的地点，每个人有1~3喜欢地点。典中列表
favorite_places ={'tom':['xichuan'],
                  'alice':['qinghia','guangxi','shanghai'],
                  'bob':['neimeng','xizang'],
                  'kaiwen':['nanjing','niuyue'],
                  }
for name,places in favorite_places.items():
    print("\n" + name.title())
    for place in places:
        print("\t"+ place.title())