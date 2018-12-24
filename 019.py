#coding:utf-8
#对象1 
class Ball:
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

#实例化配置属性
myBall = Ball()
myBall.direction = 'down'
myBall.color = 'red'
myBall.size = 'small'

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print
#使用方法
myBall.bounce()
print "Now the ball's direction is",myBall.direction
