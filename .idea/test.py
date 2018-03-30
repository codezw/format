import docx
import tkinter
from tkinter import *
import tkinter.filedialog
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt

#运行
def run():
    #打开文件
    f = open(r'C:\Users\z\Desktop\RTK测试问题汇总及原因.docx','rb')
    doc = docx.Document(f)
    #paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
    style = doc.styles.add_style('test正文',WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(20)


    doc.save(r'C:\test.docx')
    

def fileopen():
    file = tkinter.filedialog.askopenfilename()
    if file != '':
        lb.config(text=file)
    else:
        lb.config(text='None')


#主窗口
root = Tk()
root.title('排版')
root.geometry('400x200')

#路径显示
lb = Label(root,text='')
lb.pack()

#选择文件
filechoose = Button(root,text='选择文件',command=fileopen)
filechoose.pack()

#样式选择
mbfont = Menubutton(root,text='字体',relief=RAISED)
mbsize = Menubutton(root,text='字号',relief=RAISED)
mbfont.place(x=50,y=80,anchor=NW)
mbsize.place(x=120,y=80,anchor=NW)

userChoice = IntVar()
userChoice.set(1)
filemenu1=Menu(mbfont,tearoff=False)
filemenu2=Menu(mbsize,tearoff=False)
filemenu1.add_radiobutton(label='黑体',variable=userChoice,value=1)
filemenu1.add_radiobutton(label='仿宋',variable=userChoice,value=2)
filemenu2.add_radiobutton(label='da',variable=userChoice,value=1)
mbfont.config(menu=filemenu1)


runpy = Button(root,text = '运行', command = run) #第一个参数root说明com按钮在root，text指按钮的名称
runpy.pack(side = BOTTOM)  #　次级窗口的位置摆放位置

root.mainloop()
