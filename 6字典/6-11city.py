#cityes中的典中典
cities ={'london':{'contury':'uk',
                   'people':'123M',
                   'famous':'lundongqiao',
                   },
         'tokyo':{'contury':'jp',
                  'people':'239M',
                  'famous':'tokyta',
                  },
         'oxford':{'contury':'uk',
                   'people':'56M',
                   'famous':'OXFun'},
         }
for name, city in cities.items():
    print("\nCity: " + name)
    print("\tContury: " + city['contury'].title())
    print("\tPeople: " + city['people'])
    print("\tFamous: " + city['famous'].title())