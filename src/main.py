import random
import secrets

pokemonname = ["フシギダネ", "ヒトカゲ", "ゼニガメ", "バクフーン", "カメックス"]

waza = {"たいあたり":30, "ひっかく":10, "はたく":20, "のしかかり": 50, "みずでっぽう":40, "はねる":0}
attack = {"1":"たいあたり", "2":"はたく", "3":"はねる", "4":"のしかかり", "e":"逃げる", "その他":"技一覧"}
#attack[1] で技名がわかります
#waza[attack[1]] で威力がわかります

class pokemon_base:
 name = random.choice(pokemonname)

 hitpoint = 0
 def __init__(self,a):#hpの初期化
  self.hitpoint = a
 def hp(self):#hpを返す
  return self.hitpoint
 def set(self,a):#hpをセットする
  self.hitpoint = a


def kougeki(mamori: pokemon_base, waza_num: int):
  print(attack[waza_num] + " で こうげき した！")
  mamori.set(mamori.hp() - waza[attack[waza_num]])
  print(mamori.name + " に " + str(waza[attack[waza_num]]) + " のダメージ！")
  if mamori.hp() < 0:
    print(mamori.name + " は たおれた！")
  else:
    print(mamori.name + " の HP は　" + str(mamori.hp()) + " に なった！")


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



print("let's battle")
mikata = pokemon_base(100)
teki = pokemon_base(100)
while True:
    
    print(attack)
    a = input("どの攻撃をしますか？")
    if a == "e":
        print("敵は逃げて行った")
        break

    elif a == "その他":
        print("技一覧", attack.items())

    else:
        kougeki(teki,a)
        kougeki(mikata,str(random.randint(1,4)))
        if teki.hp() <= 0:
            print("あなたの勝利")
            break
        if mikata.hp() <= 0:
            print("あなたの敗北")
            break

