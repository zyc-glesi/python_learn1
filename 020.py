#coding:utf-8
#对象2 -- 初始化
class Ball:
    def __init__(self,color,size,direction):
        self.color=color
        self.size=size
        self.direction=direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

#实例化属性
myBall = Ball("red","small","down")

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print
#使用方法
myBall.bounce()
print "Now the ball's direction is",myBall.direction

print myBall

