#引入迭代器
import itertools as its
#密码组成元素
words = "1234567890"
#迭代[words] repeat位数（长度）
r = its.product(words,repeat=4)
#将密码保存文件中  打开[pass.txt]没有则创建，a是对文件的操作，表示追加
dic = open('for-py/py-learn-code/code-blackChocolate/learn/day_6wifi破解密码/pass.txt','a')
#将内容追加到文件
for i in r:
    #向文件中写入[i],""表示用分隔
    dic.write("".join(i))
    #换行
    dic.write("".join("\n"))
#关闭文件
dic.close()