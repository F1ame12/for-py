import random
def random_str(length=8):
    """随机8位ascii码存入集合生成随机字符串"""
    #if (length is not type(0))
    char_list = []
    result_str = ''
    strRange = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(0, int(length)):
        num = random.randint(0, len(strRange)-1)
        char_list.append(strRange[num])
    return result_str.join(char_list)
a = range(5)
b = range(3)
print(list(a))
print(isinstance(b, range))

a = '*'
a *= 5

'''
str_test = input()
print('the input str\'s len is', len(str_test))
print('ths str max char is', max(str_test))
print('the str min char is', min(str_test))
print(str(123456))# 将其他数据类型转为字符串
str_test *= 3 #重复字符串
str_test += 'test' #连接字符串
print('now the str is', str_test)
str_list = []
str_list.append(str_test)
print('the list len is', len(str_list))
print('we create 3 random str is',random_str(),random_str(),random_str())
'''
