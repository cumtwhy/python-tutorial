from tkinter import *
# from tkinter import Frame, Tk, Label, StringVar, Entry, LEFT, DISABLED

root=Tk()
root.title("JavBus搜索服务")

f1=Frame(root) # 定义框架
Label(f1, text="请输入你要搜索的内容: ").pack(side=LEFT, padx=5, pady=10)
e1=StringVar() # 定义输入框内容
Entry(f1, width=20, textvariable=e1).pack(side=LEFT) # 基本的输入框
e1.set('输入框默认内容') # 设置一般输入框默认内容
print(e1)
f1.pack()

f2=Frame(root) # 定义框架
e2=StringVar()
Label(f2, text='禁用输入框: ').pack(side=LEFT, padx=5, pady=10)
Entry(f2, width=50, textvariable=e2, state=DISABLED).pack(side=LEFT) #禁用的输入框
e2.set('不可修改的内容') # 设置禁用的输入框内容
f2.pack()

root.mainloop()

