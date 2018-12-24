#coding:utf-8
#列表
friends =[]
friends.append('David')

letters = ['a', 'b', 'c', 'd', 'e']
#列表分片
print letters[1:4]

#微妙的变化，第一种情况，我们取回一个元素。第二种情况，取回包含这个元素的一个列表
print letters[1]
print type(letters[1])
print letters[1:2]
print type(letters[1:2])

#向列表中添加元素的3种方法:append()、extend()、insert()
letters.append('n')
letters.append('g')
print letters

letters.extend(['f','h','i','j','p','q','r'])
print letters

letters.insert(2,'z')
print letters

#使用append 增加一个列表
letters.append(['1','2','3'])
print letters

#删除remove() del pop()
print '--删除列表中元素--'
letters.remove('r')
print letters
letters.pop()
print letters
lettersGet=letters.pop(2)
print '取得的元素是',lettersGet,'剩下的列表是:'
print letters
del letters[2]
print letters

#搜索列表 in index()
if 'a' in letters:
    print "found 'a' in letters"
else:
    print "didn't find 'a' in letters"

print 'n 的索引位置是：',letters.index('n')

#循环处理
for letter in letters:
    print letter

#列表排序 先分片出一个备份 sort() reverse() sorted()
new_letters = letters[:]
new_letters.sort()
print 'letters排序后：',new_letters
new_letters.reverse()
print new_letters
new_letters.sort(reverse=True)
print new_letters
letters2 = letters[:]
print 'letters2:', letters2
new_letters2 = sorted(letters2)
print '函数sorted()之后', new_letters2
