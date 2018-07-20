import itertools as its
import os

words = '1234567890'

r = its.product(words,repeat=3)
file_path=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","wifi破解","pass.txt")
#将密码存到文件中   打开【pass。txt】没有这个文件则创建一个，a表示追加（对文件的操作）
dic = open(file_path,'a')

#将内容追加到文件
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()