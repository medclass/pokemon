import random

from gamedesign import attack, kougeki, pokemon_base
from pokemon_name_hp import pokemon_data

# pokemonname = ["フシギダネ", "ヒトカゲ", "ゼニガメ", "バクフーン", "カメックス"]

# waza = {"たいあたり":30, "ひっかく":10, "はたく":20, "のしかかり": 50, "みずでっぽう":40, "はねる":0}
# attack = {"1":"たいあたり", "2":"はたく", "3":"はねる", "4":"のしかかり", "e":"逃げる", "その他":"技一覧"}
# #attack[1] で技名がわかります
# #waza[attack[1]] で威力がわかります





# class pokemon_base:

#  hitpoint = 0
#  def __init__(self,a):#hpの初期化
#   self.hitpoint = a
#   self.name = random.choice(pokemonname)
#  def hp(self):#hpを返す
#   return self.hitpoint
#  def set(self,a):#hpをセットする
#   self.hitpoint = a


# def kougeki(mamori: pokemon_base, waza_num: int):
#   print(attack[waza_num] + " で こうげき した！")
#   mamori.set(mamori.hp() - waza[attack[waza_num]])
#   print(mamori.name + " に " + str(waza[attack[waza_num]]) + " のダメージ！")
#   if mamori.hp() < 0:
#     print(mamori.name + " は たおれた！")
#   else:
#     print(mamori.name + " の HP は　" + str(mamori.hp()) + " に なった！")


##以下サンプルコード、コメントアウトを解除すると動きます。
# test = pokemon_base(30)#hp=30で初期化
# kougeki(test,2)
# kougeki(test,4)
##実行結果は下のようになります。
# > はたく で こうげき した！
# > ぽけもん に 20 のダメージ！
# > ぽけもん の HP は　10 に なった！
# > のしかかり で こうげき した！
# > ぽけもん に 50 のダメージ！
# > ぽけもん は たおれた！


lang = ""
while lang not in ["ja", "en"]:
    lang = input("言語モードの選択 / Select Language Mode : [ja/en]")

print({"en" : "let's battle", "ja" : "バトル開始！"}[lang])
print({"en" : "Choise Your Pokemon!", "ja" : "ポケモンを選んでね"}[lang])

pokenum = 0

print({"en" : "input pokenmon number if not random ",
    "ja" : "番号を入力してください，入力がない場合，ランダムに選ばれます"}[lang])
[print(f"{k}, {v[lang]}") for k, v in pokemon_data.items()]
pokenum = input()

if pokenum not in pokemon_data.keys():
    pokenum = random.choice(list(pokemon_data.keys()))
tekinum = random.choice(list(pokemon_data.keys()))


mikata = pokemon_base(hp=pokemon_data[pokenum]["hp"], name=pokemon_data[pokenum][lang])
teki = pokemon_base(hp=pokemon_data[tekinum]["hp"], name=pokemon_data[tekinum][lang])

while True:
    print("==========================================")
    print(attack)
    a = input({"en" : "which move：", "ja" : "どの攻撃をしますか？："}[lang])
    print("   ---   ")

    if a == "e":
        print({"en" : "enemy goes away", "ja" : "敵は逃げて行った"}[lang])
        break

    elif a == "その他":
        print("技一覧", attack.items())

    elif a in attack.keys():
        kougeki(teki,a)
        if teki.hp() <= 0:
            print({"en" : "You win!", "ja" : "あなたの勝利"}[lang])
            break
        kougeki(mikata,str(random.choice(list(attack.keys()))))
        if mikata.hp() <= 0:
            print({"en" : "You lose!", "ja" : "あなたの敗北"}[lang])
            break
