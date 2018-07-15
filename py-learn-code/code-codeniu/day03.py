#1.
'''
str = input("输入字符串")
print("第一个字符为:%s"%str[0]+"中间的一个字符为:%s"%str[(len(str)-1)//2])
'''

#2.
friends = ['niu','zhan','sun']
for x in friends:
    print (x)

friends.append('new')
print("来个新来的")
for x in friends:
    print (x)

friends.insert(1,'boss')
print("来个boss在第二位")
for x in friends:
    print (x)

print("弹出第三个")
friends.pop(2)
for x in friends:
    print (x)

#3.字符统计
'''
str = list(input("输入字符串:"))
str1 = set(str)#set()函数:对列表进行去重

print("队列表进行去重:")
for x in str1:
    print(x)

for x in str1:
    print("字符%s出现的次数:"%x, str.count(x))
'''