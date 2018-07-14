#black-chocolate
import random

'''
字符串操作
s = "Hello Python"
print(s.lower(),s.upper(),s.title(),s.isdigit(),s.islower(),
s.isupper(),s.isalpha(),s.strip(),s.rstrip(),s.lstrip(),s.count("He"),
s.find("Py"),s.replace("l","o",1))

s = input()
print(s.replace("123","321"))  
'''
'''
循环
number = int(input())
randber = random.randint(0,10)
while number != randber: 
    number = int(input())
    if number < randber:
        print("猜小了")
    else:
        print("猜大了")
print("猜的针对，真聪明")

for x in range(10):  #Python中的迭代器
    if x == 5:
        print("5")
        continue
print(x)
'''
'''
for x in range(5):  #Python中的迭代器
    print(x)
for x in range(1,3):
    print(x)
for x in range(1,6,2):
    print(x)
for x in range(5,0,-1):
    print(x)
for x in range(4,0):
    print(x)
for x in range(1,11,2):
    print(x)
for x in range(1,11):
    if x == 4:
        print("第4个包子掉地上了！")
        continue 
    print("吃第%d"%x+"个包子")
'''

for x in range(1,6):
    for a in range(1,6):
        print("*",end = "")
    for m in range(1,10):
        print(" ",end = "")
    for b in range(0,x):
        print("*",end = "")
    for m in range(1,10-x):
        print(" ",end = "")
    for c in range (0,6-x):
        print("*",end = "")
    for m in range(1,10):
        print(" ",end = "")
    for d in range(6-x,6):
        print("*",end = "")
    for y in range(1,5+6-x):
        print(" ",end="")
    for z in range(0,x*2-1):
        print("*",end="")
    print()

    
#black-chocolate