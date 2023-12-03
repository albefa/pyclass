def make_album(singer, called,number='10'):
    albums = {'singer': singer, 'called': called,'numbers':number,}
    return albums

musics = make_album('aa', 'bb',number='15')
print(musics)
musics = make_album('cc', '2x3')
print(musics)
musics = make_album('dd', '8x9',number='16')
print(musics)

