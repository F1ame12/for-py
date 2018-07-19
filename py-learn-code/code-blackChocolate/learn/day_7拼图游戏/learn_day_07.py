#GUI框架
import simpleguitk as sim

myPicture = sim.load_image("http://img.zcool.cn/community/0142135541fe180000019ae9b8cf86.jpg@1280w_1l_2o_100sh.png")
#鼠标事件
def mouseclick():
    print('点击了鼠标')
#点击按钮
def mybutton():
    print('点击了按钮')
#绘制画布的方法
def draw(canvas):
    canvas.draw_image(myPicture,[300,300],[600,600],[50,650],[98,98])
    

#创建框架窗体
frame = sim.create_frame('拼图游戏',600,700)
#设置框架面板的背景颜色
frame.set_canvas_background('Black')
#添加一个按钮
frame.add_button('我是按钮',mybutton,60)
#注册鼠标事件
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
#启动框架
frame.start()