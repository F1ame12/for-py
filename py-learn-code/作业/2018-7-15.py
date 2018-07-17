'''
x = [1,2,3,4,5,6]
1.x[5]
2.y = x[0::2]
3.x[::3]="AB"
4.len(x)
x = [10,False,"",None]
5.any(x)
x=[1,2,3,1,2,3]
6.x.index(2)
7.x.conut(3)
8.x.remove(3)
9.x.insert(4,100)
10.输入三个数，存入列表中，打印出哪个数是最大值，哪个数是最小值和平均值
11.求质数，输入任意整数，先判断你输入的数是否是质数（只能被1和自身整数的数），如果是质数则
加入到列表中，再次输入任何整数，在判断...直到输入的数小于等于0为止，最后打印出你输入的质数
12.猜数字游戏改成通过方法设定随机数范围
13.自学元祖
'''
x = [1,2,3,4,5,6]
print("1,",x[5])
print("2,",x[0::2])
x[::3] = "AB"
print("3,",x)
print("4,",len(x))
x = [10,False,"",None]
print("5,",any(x))
x = [1,2,3,1,2,3]
print("6,",x.index(2))
print("7,",x.count(3))
x.remove(3)
print("8,",x)
x.insert(4,100)
print("9",x)
def func10():
    x = int(input())
    y = int(input())
    z = int(input())
    list = [x,y,z]
    min = 10000
    max  = 0
    for i  in range(0,3):
        if list[i] > max:
            max = list[i] 
    for i in range(0,3):
        if list[i] < min:
            min = list[i]
    print("10,max= %d,"%max,end="")
    print("min= %d,"%min,end="")
    print("aver=",(list[0]+list[1]+list[2])//3)
    return 
func10()

def iszhishu(x):
    for i in range(2,x):
        if x % i == 0:
            return 0
    return 1

def func11():
    num = int(input())
    list = []
    while num > 0:
        flag =  iszhishu(num)
        if flag == 1:
            list.append(num)
        num = int(input())
    print("11,",list)
    return

func11()

import random
print("12,随机数")
def func12():
    number = int(input())
    randber = random.randint(0,number)
    while number != randber: 
        number = int(input())
        if number < randber:
            print("猜小了")
        else:
            print("猜大了")
    print("猜的针对，真聪明")
    return 

func12()


