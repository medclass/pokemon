import random

from gamedesign import attack_dict, kougeki, pokemon_base
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


# def kougeki(teki: pokemon_base, waza_num: int):
#   print(attack[waza_num] + " で こうげき した！")
#   teki.set(teki.hp() - waza[attack[waza_num]])
#   print(teki.name + " に " + str(waza[attack[waza_num]]) + " のダメージ！")
#   if teki.hp() < 0:
#     print(teki.name + " は たおれた！")
#   else:
#     print(teki.name + " の HP は　" + str(teki.hp()) + " に なった！")


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
    lang = input("言語モードの選択 / Select Language Mode : [ja/en] : ")

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
    [print(f"{k} : {v['name']}") for k, v in attack_dict.items()]
    a = input({"en" : "which move : ", "ja" : "どの攻撃をしますか？："}[lang])
    print("   ---   ")

    if a == "e":
        print({"en" : "enemy goes away", "ja" : "敵は逃げて行った"}[lang])
        break

    elif a == "その他":
        print("技一覧", attack_dict.items())

    elif a in attack_dict.keys():
        # 味方のターン
        kougeki(teki,a)

        if (lang == "ja"):
            print(f"{mikata.name} は {attack_dict[a]['name']} で こうげき した！")
            print(f"あいての {teki.name} に {attack_dict[a]['attack']} のダメージ！")
        elif (lang == "en"):
            print(f"{mikata.name} used {attack_dict[a]['name']}！")
            print(f"Rival's {teki.name} take {attack_dict[a]['attack']} damaged！")

        if teki.hp() <= 0:
            print({"en" : f"Rival's {teki.name} fainted!", "ja" : f"あいての {teki.name} は たおれた！"}[lang])
            print({"en" : "You win!", "ja" : "あなたの勝利"}[lang])
            break
        else:
            print({
                "en" : f"Rival's {teki.name} has {teki.hp()} HP！",
                "ja" : f"あいての {teki.name} の HP は {teki.hp()} に なった！"
            }[lang]
            )

        # 敵のターン
        print()
        teki_attack_num = random.choice(list(attack_dict.keys()))
        kougeki(mikata, teki_attack_num)

        if (lang == "ja"):
            print(f"あいての {teki.name} は {attack_dict[teki_attack_num]['name']} で こうげき した！")
            print(f"{mikata.name} に {attack_dict[teki_attack_num]['attack']} のダメージ！")
        elif (lang == "en"):
            print(f"Rival's {mikata.name} used {attack_dict[teki_attack_num]['name']}！")
            print(f"Your {teki.name} take {attack_dict[teki_attack_num]['attack']} damaged！")

        if mikata.hp() <= 0:
            print({"en" : f"{mikata.name} fainted!", "ja" : f"{mikata.name} は たおれた！"}[lang])
            print({"en" : "You lose!", "ja" : "あなたの敗北"}[lang])
            break
        else:
            print({
                "en" : f"Your {mikata.name} has {mikata.hp()} HP！",
                "ja" : f"{mikata.name} の HP は {mikata.hp()} に なった！"
            }[lang]
            )
