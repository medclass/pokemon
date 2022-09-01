class Pokemon_class:
    pikachu = {"pikachu_name":"pikachu", "pikachu_hp":100}          #辞書型を使い、10個のポケモンの名前とhpを付けます
    squirtle = {"squirtle_name":"squirtle", "squirtle_hp":200}
    psyduck = {"psyduck_name":"psyduck", "psyduck_hp":150}
    mewtwo = {"mewtwo_name":"mewtwo", "mewtwo_hp":300}
    jigglypuff = {"jigglypuff_name":"jigglypuff", "jigglypuff_hp":150}
    gengar = {"gengar_name":"gengar", "gengar_hp":200}
    eevee = {"eevee_name":"eevee", "eevee_hp":150}
    dragonite = {"dragonite_name":"dragonite", "dragonite_hp":250}
    cubone = {"cubone_name":"cubone", "cubone_hp":300}
    charizard = {"charizard_name":"charizard", "charizard_hp":100}

#以下の内容はnameとhpのタイプです。
# test = Pokemon_class()
# print(test.pikachu)
# print(type(test.pikachu["pikachu_name"]))
# print(type(test.pikachu["pikachu_hp"]))
#結果
#{'pikachu_name': 'pikachu', 'pikachu_hp': 100}
#<class 'str'>
#<class 'int'>


pokemon_data = {
  "6" : {"ja" : "リザードン", "en" : "charizard", "hp" : 100},
  "7" : {"ja" : "ゼニガメ", "en" : "squirtle", "hp" : 200},
  "25" : {"ja" : "ピカチュウ", "en" : "pikachu", "hp" : 100},
  "39" : {"ja" : "プリン", "en" : "jigglypuff", "hp" : 300},
  "54" : {"ja" : "コダック", "en" : "psyduck", "hp" : 150},
  "94" : {"ja" : "ゲンガー", "en" : "gengar", "hp" : 200},
  "104" : {"ja" : "カラカラ", "en" : "cubone", "hp" : 200},
  "133" : {"ja" : "イーブイ", "en" : "eevee", "hp" : 150},
  "149" : {"ja" : "カイリュー", "en" : "dragonite", "hp" : 250},
  "150" : {"ja" : "ミュウツー", "en" : "mewtwo", "hp" : 300},
}
