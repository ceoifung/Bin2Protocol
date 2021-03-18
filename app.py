from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Bin2Protocol | Copyright © 2021 | Powered by Ceoifung')
w = 600
h = 480
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the scree
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
l1_all = []
frame = 0
index = 0
frame_all = 0


'''
生成通信协议
'''
def create():
    content = (t_origin.get("0.0", "end")).split("\n")
    content.pop()  # 列表最后一个元素是空删除它
    res = content[0].split(" ")  # 不加任何参数
    crc = 0
    for re in res:
        crc += int(re, 16)
    crc = str(hex(crc//(len(res)+3))).replace('0x', '')
    test = ['ff', 'ff', '13', '02', str(hex(len(res)+2)).replace('0x', '')]
    tmp = [crc, 'ee', 'ee']
    test.extend(res)
    test.extend(tmp)
    t_dest.delete('1.0', 'end')
    t_dest.insert('0.0', test)


'''
处理bin文件的hex数据
'''
def print_hex(bytes):
    l = [hex(int(i)).replace('0x', '').zfill(2) for i in bytes]
    return " ".join(l)

'''
打开bin文件
'''
def open_file():
    global frame, l1_all, frame_all
    file = filedialog.askopenfilename(initialdir=os.getcwd())
    l1 = []
    if ".bin" in file:
        with open(file, "rb") as file:
            for line in file:
                l1.extend(print_hex(line).split(' '))
            frame = len(l1) // 128
            if len(l1)-frame*128 != 0:
                frame_all = frame+1
            else:
                frame_all = frame
           
            if frame > 0:
                btn_preview['state'] = 'disabled'
                btn_next['state'] = 'normal'
            for i in range(frame):
                l1_all.append(l1[i*128:128+i*128])
            l1_all.append(l1[frame*128: len(l1)])
            set_origin(l1_all[0])
            create()
            label['text'] = '帧数: '+str(frame_all) + \
                ' 当前帧: 1' + '\n帧长: '+str(len(l1_all[0]))
    else:
        set_origin('文件名不合法')


'''
设置源输入框的内容
'''
def set_origin(data):
    t_origin.delete('1.0', 'end')
    t_origin.insert('0.0', data)


'''
上一个源按钮
'''
def create_preview():
    global index, l1_all, frame_all
    btn_next['state'] = 'normal'
    # print(index-1)
    set_origin(l1_all[index-1])
    frm_len = len(l1_all[index-1])
    create()
    index -= 1
    label['text'] = '帧数: '+str(frame_all)+' 当前帧: ' + \
        str(index+1) + '\n帧长: '+str(frm_len)
    if index == 0:
        btn_preview['state'] = 'disabled'


'''
下一个源生成按钮
'''
def create_next():
    global index, l1_all, frame_all
    btn_preview['state'] = 'normal'
    set_origin(l1_all[index+1])
    frm_len = len(l1_all[index+1])
    create()
    index += 1
    label['text'] = '帧数: '+str(frame_all)+' 当前帧: ' + \
        str(index+1) + '\n帧长: '+str(frm_len)
    if index >= frame_all-1:
        btn_next['state'] = 'disabled'

t_origin = Entry(root)
t_origin = Text(root, width=100, height=20)
t_origin.place(relx=0.1, rely=0.05, relwidth=0.6, relheight=0.35)

btn_openfile = Button(root, text='打开bin文件', command=open_file)
btn_openfile.place(relx=0.72, rely=0.15, relwidth=0.2, relheight=0.1)

btn_preview = Button(root, text='上一个', command=create_preview)
btn_preview['state'] = 'disabled'
btn_preview.place(relx=0.72, rely=0.3, relwidth=0.2, relheight=0.1)

btn_next = Button(root, text='下一个', command=create_next)
btn_next['state'] = 'disabled'
btn_next.place(relx=0.72, rely=0.45, relwidth=0.2, relheight=0.1)

btn_create = Button(root, text='生成', command=create)
btn_create.place(relx=0.72, rely=0.6, relwidth=0.2, relheight=0.1)

label = Label(root, text="帧数: 0 当前帧: 0\n帧长: 0")
label.place(relx=0.70, rely=0.05, relwidth=0.25, relheight=0.1)

t_dest = Entry(root)
t_dest = Text(root, width=100, height=50)
t_dest.place(relx=0.1, rely=0.45, relwidth=0.6, relheight=0.5)

root.mainloop()

