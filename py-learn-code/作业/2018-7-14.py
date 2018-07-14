'''
s="HelloPython"  
1、 max(s)   #    
2、 "python" in s  #  
3、 "AB">="123"  #   
4、 "AB" < "ABC"  #  
5、 "ABC" == "abc"  #   
6、 s[2:4]  #    
7、 s[:]   #    
8、 s[2:2]  #   
9、 s[len(s)-2]    
10、字符 'F' 的ASCII码为   #  
11. s.lower()   #
12. s.upper()   #
13. s.isdigit()   #
14. s.isalpha()   #
15. s.isupper()   #
16. s.rstrip()   #
17. s.find("h",5)   #
18. s.replace("h","H",1)   #
19.输入一个字符串，打印这个字符串的第一个字符,中间的一个字符和最后一个字符。
20.任意输入一个字符串，计算要输入的字符"a"的个数，并打印出来
  例: 请输入:  abcdabcabazzzzz  打印:  字符"a"的个数为:4    
'''

s = 'HelloPython'
print('1.', max(s))
print('2.', 'python' in s)
print('3.', 'AB' >= '123')
print('4.', 'AB' < 'ABC')
print('5.', 'ABC' == 'abc')
print('6.', s[2:4])
print('7.', s[:])
print('8.', s[2:2])
print('9.', s[len(s)-2])
print('10.', ord('F'))
print('11.', s.lower())
print('12.', s.upper())
print('13.', s.isdigit())
print('14.', s.isalpha())
print('15.', s.isupper())
print('16.', s.rstrip())
print('17.', s.find('h', 5))
print('18.', s.replace('h', 'H', 1))
str1 = input()
print('19.', str1[0], str1[len(str1)//2], str1[len(str1)-1])
str2 = input()
print('20.', '字符"a"的个数为:', str2.count('a'))