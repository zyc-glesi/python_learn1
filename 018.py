#coding:utf-8
#函数
def printMyAddress(myName):
    print myName+"加油"

printMyAddress('赵川')

#--------实参 和 形参--------------------
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price=float(raw_input('Enter a price:'))

totalPrice=calculateTax(my_price, 0.06)
print "price = ",my_price,"Total price = ",totalPrice

#---------局部变量 和 全局变量---------
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    my_price = 10000
    print '这是局部变量my_price：',my_price
    return total

my_price=float(raw_input('Enter a price:'))

totalPrice=calculateTax(my_price, 0.06)
print "price = ",my_price,"Total price = ",totalPrice
print '这是函数外的全局变量my_price:',my_price

def change():
    global my_price
    my_price = "20000"

change()

# 当使用+号的时候，要主意是否有int + str 的不合适。
print "程序外打印，被函数change内强制全局过的my_price："+my_price