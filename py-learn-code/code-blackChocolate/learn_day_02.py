#black-chocolate
import random

'''
s = "Hello Python"
print(s.lower(),s.upper(),s.title(),s.isdigit(),s.islower(),
s.isupper(),s.isalpha(),s.strip(),s.rstrip(),s.lstrip(),s.count("He"),
s.find("Py"),s.replace("l","o",1))
'''

s = input()
print(s.replace("123","321"))  

number = int(input())
randber = random.randint(0,10)
while number != randber: 
    number = int(input())
    if number < randber:
        print("猜小了")
    else:
        print("猜大了")
print("猜的针对，真聪明")
#black-chocolate