import tkinter as tk
from tkinter import ttk, messagebox
import os

class WordMaster:
    def __init__(self):
        self.words = self.loadData()

        self.win = tk.Tk()
        self.win.title("단어장")

        self.word = tk.StringVar()
        self.mean = tk.StringVar()

        # 입력창 및 라벨
        e_word = ttk.Entry(self.win, textvariable=self.word, width=15)
        e_word.grid(row=0, column=1, sticky='w', padx=10)

        l_meaning = tk.Label(self.win, text="뜻:")
        l_meaning.grid(row=1, column=0, sticky='w', padx=10)

        e_meaning = ttk.Entry(self.win, textvariable=self.mean, width=35)
        e_meaning.grid(row=1, column=1, columnspan=3, sticky='w', padx=10)

        # 버튼
        b_search = ttk.Button(self.win, text="검색", width=5, command=self.search)
        b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w')

        b_add = ttk.Button(self.win, text="추가", width=5, command=self.add)
        b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w')

        b_reset = ttk.Button(self.win, text="초기화", width=5, command=self.reset)
        b_reset.grid(row=2, column=0, ipadx=10, ipady=5, padx=10, sticky='w')

        b_end = ttk.Button(self.win, text="종료", width=5, command=self.end)
        b_end.grid(row=2, column=3, ipadx=10, ipady=5, padx=10, sticky='w')

        # 이벤트 바인딩
        e_word.bind("<Return>", self.searchHandler)
        e_meaning.bind("<Return>", self.resetHandler)

    def loadData(self):
        words = {}
        if not os.path.exists("words.txt"):
            return words

        with open("words.txt", "r", encoding="utf-8") as fp:
            for line in fp:
                word = line.strip().split(":")
                if len(word) == 2:
                    key, value = word
                    words[key.strip()] = value.strip()
        return words

    def add(self):
        w = self.word.get()
        m = self.mean.get()
        self.words[w] = m
        messagebox.showinfo("추가 확인", f"단어 '{w}'를 추가했습니다.")
        self.word.set("")
        self.mean.set("")

    def search(self):
        w = self.word.get()
        if w not in self.words:
            messagebox.showinfo("검색 오류", f"{w} 단어는 없습니다!")
            self.reset()
            return
        m = self.words[w]
        self.mean.set(m)

    def reset(self):
        self.word.set("")
        self.mean.set("")

    def end(self):
        with open("words.txt", "w", encoding="utf-8") as fp:
            for w in self.words.keys():
                m = self.words[w]
                fp.write(f"{w}:{m}\n")
        self.win.destroy()

    def searchHandler(self, event):
        self.search()

    def resetHandler(self, event):
        self.reset()

# 프로그램 실행
wm = WordMaster()
wm.win.mainloop()
