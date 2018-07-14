#youngniu
value=10
number=20
print("print函数的用法",value,number,sep="，",end="。",flush=False)
#youngniu

#black-chocolate
'''
基本输出函数：print
print("提示信息",value,value,....,sep="",end="\n",flush =False,file=sys.stdout)
"":提示信息
value:值
sep:分隔符(缺省的是一个空格)
end:结束标识（缺省的是换行符）
flush:缓冲  - 是否立即将流输出（True/False）
    -程序结束缓冲区中的内容
file :对象流  - 默认为sys.stdoutf

a = 10
b = 20
c = 30
c = "I'm a teacher"
print("输出",a,b,c,sep=",",end=".",flush=False)

字符串：
    序列的一种  - 按一定顺序进行排列
    ''               eg: 'I'm a teacher'出错
    ""               所见即所得
    '''  '''         所见即所得 
    """  """         所见即所得

字符串常用函数:
    len(str):   返回字符串的长度
    max(str):   返回字符串中最大的字符
    min(str):   返回字符串中最小的字符
    str(0): 将o转换为字符串类型（o可以为任何对象）
    d = """I'm a teacher"""
    f = len(d)
    print("输出",f)

字符串运算：
    + 用于字符串的连接
        str = "123" + '456'
    += 用于字符串并改变变量的绑定
        str = "123"
        str += "123"
    *   用于生产重复字符串
        str = "123"*3
    *= 用于生产重复字符串并改变变量的绑定
        str = "123"
        str *= 3
    in 和 not in 运算符：
        作用：用于序列、字典、集合、中判断某个值是否存在于该对象中
        存在返回True、不存在返回False
        例如：s="welcome to TEDU!"
            if 'to' in s:
                print("to 在字符串中")
            else:
                print("to 不在字符串中")
索引：
    Python字符串是不可改变的字符序列
    语法：
        字符串【整数值】
    说明：
        序列都可以用索引来访问序列中的对象
        序列正向索引从0开始1.2.3...len(str)-1
        序列反向索引从-1开始-2.-3...-len(str)
    例如：
        s = "ABCD"
        s[2]  #c
        s[-2] #c
    切片：（slice）
'''
    

#black-chocolate