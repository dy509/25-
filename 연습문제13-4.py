import tkinter as tk
from tkinter import ttk

class MemberReg():
    hobby_list=['영화시청','음악감상','사진찍기','운동']

    def __init__(self):
        self.win=tk.Tk() #기본 윈도우 객체 생성
        self.win.title('회원가입')
        self.win.geometry('250x300')
        self.buildGUI() #화면 구성 메서드 호출 주석 해제 및 수정

    def buildGUI(self):
        self.__create_name_input_frame().grid(row=0,column=0,sticky='w')
        self.__create_grade_input_frame().grid(row=1,column=0,sticky='w')
        self.__create_hobby_input_frame().grid(row=2,column=0,sticky='w')
        self.__create_button_frame().grid(row=3,column=0,sticky='e')

    def __create_name_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame,text='이름')

        self.name=tk.StringVar()
        input_entry=ttk.Entry(frame,textvariable=self.name)

        self.text_label.grid(row=0,column=0)
        input_entry.grid(row=0,column=1)

        return frame

    def __create_grade_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame,text='학년')
        self.text_label.grid(row=0,column=0)

        sub_frame=ttk.Frame(frame)
        self.grade=tk.IntVar() # intVar() -> IntVar() 수정
        for i in range(1,5):
            grade_btn=ttk.Radiobutton(sub_frame,
                                      text=f'{i}학년', # f'학년' -> f'{i}학년' 수정
                                      value=i,
                                      variable=self.grade,)
            grade_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)

        return frame

    def __create_hobby_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame,text='취미')
        self.text_label.grid(row=0,column=0)

        sub_frame=ttk.Frame(frame)
        self.hobby=[]
        for i in range(4):
            self.hobby.append(tk.IntVar())
            hobby_btn=ttk.Checkbutton(sub_frame,
                                      text=self.hobby_list[i],
                                      variable=self.hobby[i])
            hobby_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)

        return frame

    def __create_button_frame(self):
        frame=ttk.Frame(self.win)

        input_btn=ttk.Button(frame,text='입력',
                             command=self.__input_btn_clicked)
        quit_btn=ttk.Button(frame,text='종료',
                             command=self.win.destroy)
        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame

    def __input_btn_clicked(self):
        print("이름:", self.name.get())
        print("학년:", self.grade.get())

        selected_hobbies = []
        for i in range(4):
            if self.hobby[i].get() == 1: # Checkbutton의 get()은 0 또는 1 반환
                selected_hobbies.append(self.hobby_list[i])
        print("취미:", ", ".join(selected_hobbies))


#주 프로그램부
member=MemberReg()
member.win.mainloop()