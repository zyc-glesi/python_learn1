# coding:utf-8
# 对象3 -- 继承
# 假想我们要建立一个游戏，玩家一路上可以捡起不同的东西，比如食物、钱或衣服。可以建一个类，名为 GameObject。GameObject 类有 name 等属性（例如 coin、apple 或 hat）和 pickUp() 等方法（它会把硬币增加到玩家的物品集合中）。所有游戏对象都有这些共同的方法和属性。
# 然后，可以为硬币建立一个子类。Coin 类从 GameObject 派生。它要继承 GameObject 的属性和方法，所以 Coin 类会自动有一个 name 属性和 pickUp() 方法。Coin 类还需要一个 value 属性（这个硬币价值多少）和一个 spend() 方法（可以用这个硬币去买东西）。

class GameObject:
    def __init__(self,name):
        self.name = name
    def pickUp(self,player):
        pass
        #put code here to add the object
        #to the player's collection

#Coin 类是GameObject的子类
class Coin(GameObject):
    def __init__(self,value):
        GameObject.__init__(self,"coin")
        self.value = value

    def spend(self,buyer,seller):
        pass
        #put code here to remove the coin
        #from the buyer's money and
        #add it to the seller's money
