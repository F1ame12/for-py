import simpleguitk as sim
import os

filePath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","拼图游戏","1.img")
myPicture = 

'''
author：niu
name:darw()
function:点击按钮
'''
def mybutton():
    print('click btn')

'''
author：niu
name:darw()
function:鼠标点击
'''
def mouseclick():
    print('click mouse')

'''
author：niu
name:darw()
function:绘制画布
'''
def draw():
    canvas.draw_image(myPicture,[100,100],[200,200],[50,250],[98,98])


#框架的设置
frame = sim.create_frame('拼图游戏',600,700)
frame.set_canvas_background('black')
frame.add_button('我是一个按钮',mybutton,60)
#mybutton()加了（）只会运行一次
#frame.add_button('我是一个按钮',mybutton(),60)

#框架上事件的设置
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()