from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox


GUI =Tk() # หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400')


B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

##################
def Button2():
    text ='ตอนนี้ฉันมีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#################

GUI.mainloop()
