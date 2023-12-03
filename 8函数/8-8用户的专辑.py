def make_album(singer, called, number='10'):
    albums = {'singer': singer, 'called': called, 'numbers': number, }
    return albums

while True:
    print("\n请告我专辑名和作者")
    print("(输入q退出)")

    title = input("歌手名： ")
    if title =='q':
        break
    artist = input("专辑名：")
    if artist =='q':
        break
    forrmoted_album = make_album(title,artist)
    print("\n专辑名： "+ artist+" ; "+"歌手： "+title+"!")

#定义的函数，当时完成书写，否则容易出使用的时候容易错误