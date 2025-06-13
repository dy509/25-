import tkinter as tk
from tkinter import ttk

class ConTempWin():
    def __init__(self):
        self.win=tk.Tk() #기본 윈도우 객체 생성
        self.win.title('온도변환기-1단계')
        self.__buildGUI() #화면 구성
        self.win.geometry('270x190')

    def __buildGUI(self):
        fahr_Label=ttk.Label(self.win, text='화씨')

        self.__fahr=tk.IntVar()
        fahr_entry=ttk.Entry(self.win,justify=tk.RIGHT,width=11,
                                textvariable=self.__fahr)

        cel_Label=ttk.Label(self.win,text='섭씨')

        self.__cels=tk.DoubleVar()
        cel_entry=ttk.Entry(self.win,justify=tk.RIGHT,width=11,
                                textvariable=self.__cels)

        f2c_btn=ttk.Button(self.win,text='화씨->섭씨',command=self.__f2c_handler)
        c2f_btn=ttk.Button(self.win,text='섭씨->화씨',command=self.__c2f_handler)
        reset_btn=ttk.Button(self.win,text='초기화',command=self.__reset_handler)
        quit_btn=ttk.Button(self.win,text='종료',command=self.win.destroy)

        fahr_Label.pack() #클래스에서 객체를 정의한 뒤에 팩함수로 배치치
        fahr_entry.pack()
        cel_Label.pack()
        cel_entry.pack()

        f2c_btn.pack()
        c2f_btn.pack()
        reset_btn.pack()
        quit_btn.pack()

    f2c_btn.pack()
        c2f_btn.pack()
        reset_btn.pack()
        quit_btn.pack()
