#coding:utf-8
#循环2
for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
    print cool_guy, "is the coolest guy ever!"

#条件或者while循环
print "Type 3 to continue,anything else to quit."
sonmeInput = raw_input()
while sonmeInput == '3':
    print "Thank you for the 3. Very kind of you."
    print "Type 3 to continue,anything else to quit."
    sonmeInput = raw_input()

print "That's not 3,so I'm quitting now."
