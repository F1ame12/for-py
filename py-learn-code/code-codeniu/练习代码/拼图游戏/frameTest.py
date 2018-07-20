import simpleguitk as sim
import os
from PIL import Image

picturePath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","拼图游戏","张雪迎.png")
myPicture = sim.load_image('https://wx3.sinaimg.cn/mw690/b74f0e41ly1ft81oy4y7zj206q08a0st.jpg')


im = Image.open(picturePath)
#im.show()
L = im.convert('L')
L.show()