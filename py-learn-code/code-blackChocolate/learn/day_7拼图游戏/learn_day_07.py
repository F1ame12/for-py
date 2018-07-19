#GUI框架
import simpleguitk as sim
#随机数模块
import random

#获取网络照片
myPicture = sim.load_image("http://img.zcool.cn/community/0142135541fe180000019ae9b8cf86.jpg@1280w_1l_2o_100sh.png")

#定义画布的宽、高
WIDTH = 600
HEIGHT = 700

#定义图像块的边长
IMAGE_SIZE = WIDTH/3

#定义棋盘的行和列
ROWS = 3
COLS = 3

#定义步数
steps = 0

#定义一个列表存放图像块的坐标
all_coord_pos = [[100,100],[300,100],[500,100], \
                [100,300],[300,300],[500,300], \
                [100,500],[300,500],None]

#定义一个列表保存图像块
borad = [[None,None,None],[None,None,None],[None,None,None]]

#定义一个方法初始化图像块及拼接板
def init_board():
    #打乱图像块列表
    random.shuffle(all_coord_pos)
    #填充拼接板
    for i in range(ROWS):
        for j in range(COLS):
            #定义一个变量来接受坐标
            index = i * ROWS + j 
            square_content = all_coord_pos[index] 
            #如果坐标为None,这个图像块就是None
            if square_content is None:
                borad[i][j] = None
            else:
                borad[i][j] = Square(square_content)

#绘制画布的方法
def draw(canvas):
    #绘制缩略图
    canvas.draw_image(myPicture,[300,300],[600,600],[50,650],[98,98])
    #绘制图像块（图像块没有内容就绘制，有内容就不绘制）
    for i in range(ROWS):
        for j in range(COLS):
            if borad[i][j] is not None:
                borad[i][j].drawSquare(canvas,[i,j])
    #绘制步数
    canvas.draw_text('步数'+str(steps),[400,670],22,'white')

#定义一个图像块的类
class Square:
    #构造方法  初始化   content表示图像块的填充内容
    def __init__(self,content):
        self.content = content
    #定义个绘制图像块的方法
    def drawSquare(self,canvas,board_pos):
        #显示换行 \ 
        canvas.draw_image(myPicture,self.content,[IMAGE_SIZE,IMAGE_SIZE],\
                            [(board_pos[1]+0.5)*IMAGE_SIZE,\
                            (board_pos[0]+0.5)*IMAGE_SIZE],\
                            [IMAGE_SIZE,IMAGE_SIZE])

#鼠标事件
def mouseclick(pos):
    r = int(pos[1]//IMAGE_SIZE)
    c = int(pos[0]//IMAGE_SIZE)
    global steps
    if r < 3 and c <3:
        if borad[r][c] == None:
            return 
        else:
            #拿到图形块的模块
            current_square = borad[r][c]
            #判断各个方向
            #判断上面
            if r-1 >= 0 and borad[r-1][c] == None:
                #互换2个图形块的位置
                borad[r][c] = None
                borad[r-1][c] = current_square
                steps = steps + 1
            #判断下面
            if r+1 <= 2 and borad[r+1][c] == None:
                borad[r][c] = None
                borad[r+1][c] = current_square
                steps = steps + 1
            #判断左边
            if c-1 >= 0 and borad[r][c-1] == None:
                borad[r][c] = None
                borad[r][c-1] = current_square
                steps = steps + 1
            #判断右边
            if c+1 <= 2 and borad[r][c+1] == None:
                borad[r][c] = None
                borad[r][c+1] = current_square
                steps = steps + 1

#点击按钮
def mybutton():
   global steps
   steps = 0
   init_board()

#创建框架窗体
frame = sim.create_frame('拼图游戏',600,700)
#设置框架面板的背景颜色
frame.set_canvas_background('Black')
#添加一个按钮
frame.add_button('重新开始',mybutton,60)
#注册鼠标事件
frame.set_mouseclick_handler(mouseclick)
#设置画布绘图
frame.set_draw_handler(draw)
#初始化拼接板
init_board()
#启动框架
frame.start()