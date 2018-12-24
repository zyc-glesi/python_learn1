#coding:utf-8
#对象2 -- 初始化 __str()__ 默认输出
class Ball:
    def __init__(self,color,size,direction):
        self.color=color
        self.size=size
        self.direciton=direction

    def __str__(self):
        msg="Hi,I'm a "+self.size+" "+self.color+" "+self.direciton+" ball"
        return msg
myBall = Ball("red","small","down")
print myBall


#完整的热狗示例
class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments)>0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg + i +", "
        msg = msg.strip(", ")#这个大概是消除两边逗号？
        msg = self.cooked_string + " "+msg+"."
        return msg

    def cook(self,time):
        self.cooked_level = self.cooked_level + time #确保热狗越来越熟
        if self.cooked_level>8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level>5:
            self.cooked_string = "Well-done"
        elif self.cooked_level>3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def addCondiment(self, condiment):
        self.condiments.append(condiment)



myDog = HotDog()
print myDog
print "Cooking hot dog for 4 minutes..."
myDog.cook(4)
print myDog

print "Cooking hot dog for 3 more minutes..."
myDog.cook(3)
print myDog

print "What happens if I cook it for 10 more minutes..."
myDog.cook(10)
print myDog

print "Now, I'm going to add some stuff on my hot dong"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print myDog


