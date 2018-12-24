#coding:utf-8
#字典----关系数组
phoneNumbers = {}
phoneNumbers ={'John':'555-1234','Mary':'555-6789','Bob':'333-9876'}
print phoneNumbers
phoneNumbers['Jenny'] = '888-5678'
print phoneNumbers
maryPhone=phoneNumbers.pop('Mary')
print maryPhone
phoneNumbers.clear()
print phoneNumbers

