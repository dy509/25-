import tkinter as tk # Tkinter 라이브러리를 tk라는 이름으로 임포트합니다. GUI(그래픽 사용자 인터페이스) 생성을 위해 사용됩니다.
from tkinter import ttk, messagebox # tkinter.ttk 모듈에서 ttk(테마를 적용한 위젯)을, messagebox 모듈에서 messagebox(팝업 메시지)를 임포트합니다.
import os # 운영체제(Operating System)와 상호작용하기 위한 os 모듈을 임포트합니다. 파일 존재 여부 확인 등에 사용됩니다.

class WordMaster: # 'WordMaster'라는 이름의 클래스를 정의합니다. 이 클래스는 단어장 애플리케이션의 모든 기능과 UI를 캡슐화합니다.
    def __init__(self): # 이 메서드는 '생성자(Constructor)'입니다. WordMaster 클래스의 객체(인스턴스)가 생성될 때 자동으로 호출됩니다.
        # 객체의 초기 상태를 설정하고 필요한 자원(단어 데이터, 윈도우 등)을 준비합니다.
        self.words = self.loadData() # 'self.words'라는 인스턴스 변수를 정의하고, loadData() 메서드를 호출하여 단어 데이터를 파일에서 불러와 초기화합니다.
                                     # self.words는 단어(key)-뜻(value) 쌍을 저장할 딕셔너리가 됩니다.

        self.win = tk.Tk() # Tkinter의 메인 윈도우(루트 윈도우) 객체를 생성하여 'self.win'에 할당합니다. 이 윈도우가 GUI의 기본 틀이 됩니다.
        self.win.title("단어장") # 생성된 윈도우의 제목을 "단어장"으로 설정합니다.

        self.word = tk.StringVar() # Tkinter의 문자열 변수(StringVar)를 생성하여 'self.word'에 할당합니다.
                                   # 이 변수는 '단어' 입력창(Entry)과 연결되어, 입력창의 내용을 파이썬 코드에서 쉽게 접근하고 변경할 수 있게 합니다.
        self.mean = tk.StringVar() # Tkinter의 문자열 변수를 생성하여 'self.mean'에 할당합니다.
                                   # 이 변수는 '뜻' 입력창(Entry)과 연결됩니다.

        # 입력창 및 라벨 (GUI 위젯 생성 및 배치 시작)
        # tk.Label(부모 윈도우, 텍스트 내용) : 텍스트를 표시하는 라벨 위젯을 생성합니다.
        # ttk.Entry(부모 윈도우, textvariable=연결변수, width=너비) : 텍스트를 입력받는 엔트리 위젯을 생성합니다.
        # .grid(row=행, column=열, sticky=정렬, padx=가로여백, pady=세로여백, ipadx=가로패딩, ipady=세로패딩, columnspan=열병합)
        # grid()는 위젯을 행과 열로 구성된 격자(Grid)에 배치하는 레이아웃 관리자입니다.

        l_word = tk.Label(self.win, text="단어:") # "단어:" 텍스트를 표시하는 라벨 위젯을 생성합니다.
        l_word.grid(row=0, column=0, sticky='w', padx=10) # 라벨을 0행 0열에 배치하고, 서쪽(w, west)으로 정렬하며, 좌우에 10픽셀의 여백을 줍니다.

        e_word = ttk.Entry(self.win, textvariable=self.word, width=15) # '단어'를 입력받을 엔트리 위젯을 생성합니다.
                                                                     # self.word 변수와 연결되며, 너비는 15글자입니다.
        e_word.grid(row=0, column=1, sticky='w', padx=10) # 엔트리를 0행 1열에 배치하고, 서쪽(w) 정렬 및 좌우 10픽셀 여백을 줍니다.

        l_meaning = tk.Label(self.win, text="뜻:") # "뜻:" 텍스트를 표시하는 라벨 위젯을 생성합니다.
        l_meaning.grid(row=1, column=0, sticky='w', padx=10) # 라벨을 1행 0열에 배치하고, 서쪽(w) 정렬 및 좌우 10픽셀 여백을 줍니다.

        e_meaning = ttk.Entry(self.win, textvariable=self.mean, width=35) # '뜻'을 입력받을 엔트리 위젯을 생성합니다.
                                                                       # self.mean 변수와 연결되며, 너비는 35글자입니다.
        e_meaning.grid(row=1, column=1, columnspan=3, sticky='w', padx=10) # 엔트리를 1행 1열에 배치하고, 3개의 열을 병합(columnspan=3)하며, 서쪽(w) 정렬 및 좌우 10픽셀 여백을 줍니다.

        # 버튼 (GUI 위젯 생성 및 배치 계속)
        # ttk.Button(부모 윈도우, text=버튼 텍스트, width=너비, command=클릭 시 실행될 함수)

        b_search = ttk.Button(self.win, text="검색", width=5, command=self.search) # "검색" 버튼을 생성하고, 클릭 시 self.search 메서드가 실행되도록 합니다.
        b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w') # 버튼을 0행 2열에 배치하고, 내부 패딩을 설정하며, 서쪽(w) 정렬합니다.

        b_add = ttk.Button(self.win, text="추가", width=5, command=self.add) # "추가" 버튼을 생성하고, 클릭 시 self.add 메서드가 실행되도록 합니다.
        b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w') # 버튼을 0행 3열에 배치하고, 내부 패딩을 설정하며, 서쪽(w) 정렬합니다.

        b_reset = ttk.Button(self.win, text="초기화", width=5, command=self.reset) # "초기화" 버튼을 생성하고, 클릭 시 self.reset 메서드가 실행되도록 합니다.
        b_reset.grid(row=2, column=0, ipadx=10, ipady=5, padx=10, sticky='w') # 버튼을 2행 0열에 배치하고, 내부 패딩과 좌우 여백을 설정하며, 서쪽(w) 정렬합니다.

        b_end = ttk.Button(self.win, text="종료", width=5, command=self.end) # "종료" 버튼을 생성하고, 클릭 시 self.end 메서드가 실행되도록 합니다.
        b_end.grid(row=2, column=3, ipadx=10, ipady=5, padx=10, sticky='w') # 버튼을 2행 3열에 배치하고, 내부 패딩과 좌우 여백을 설정하며, 서쪽(w) 정렬합니다.

        # 이벤트 바인딩 (특정 이벤트 발생 시 메서드 호출)
        # 위젯.bind("이벤트", 실행할 메서드) : 특정 위젯에 특정 이벤트가 발생했을 때 지정된 메서드를 호출하도록 연결합니다.
        e_word.bind("<Return>", self.searchHandler) # '단어' 입력창(e_word)에서 Enter 키(<Return>)를 누르면 self.searchHandler 메서드를 호출합니다.
        e_meaning.bind("<Return>", self.resetHandler) # '뜻' 입력창(e_meaning)에서 Enter 키(<Return>)를 누르면 self.resetHandler 메서드를 호출합니다.

    def loadData(self): # 단어 데이터를 'words.txt' 파일에서 불러오는 메서드입니다.
        words = {} # 단어를 저장할 빈 딕셔너리를 초기화합니다.
        if not os.path.exists("words.txt"): # 'words.txt' 파일이 현재 디렉토리에 존재하는지 확인합니다.
            return words # 파일이 없으면 빈 딕셔너리를 반환하고 메서드를 종료합니다.

        with open("words.txt", "r", encoding="utf-8") as fp: # 'words.txt' 파일을 읽기 모드('r')로 열고, UTF-8 인코딩을 사용합니다.
                                                             # 'with' 문을 사용하면 파일 작업 후 자동으로 파일을 닫아줍니다.
            for line in fp: # 파일의 각 줄을 반복문으로 읽어옵니다.
                word = line.strip().split(":") # 각 줄의 양쪽 공백을 제거하고(strip()), 콜론(:)을 기준으로 문자열을 분리합니다(split(":"))
                                               # 예: "apple:사과\n" -> ["apple", "사과"]
                if len(word) == 2: # 분리된 결과가 정확히 두 부분(단어와 뜻)으로 나뉘었는지 확인합니다.
                    key, value = word # 분리된 두 부분을 각각 key(단어)와 value(뜻)에 할당합니다.
                    words[key.strip()] = value.strip() # key와 value의 양쪽 공백을 제거한 후, 딕셔너리 'words'에 저장합니다.
        return words # 모든 단어를 읽어온 딕셔너리를 반환합니다.

    def add(self): # 단어를 단어장에 추가하는 메서드입니다.
        w = self.word.get() # '단어' 입력창에 입력된 텍스트를 가져와 'w' 변수에 저장합니다.
        m = self.mean.get() # '뜻' 입력창에 입력된 텍스트를 가져와 'm' 변수에 저장합니다.
        self.words[w] = m # 가져온 단어 'w'와 뜻 'm'을 'self.words' 딕셔너리에 추가하거나, 단어가 이미 있으면 뜻을 업데이트합니다.
        messagebox.showinfo("추가 확인", f"단어 '{w}'를 추가했습니다.") # 사용자에게 단어 추가 성공 메시지를 팝업으로 보여줍니다. (f-string 사용)
        self.word.set("") # '단어' 입력창의 내용을 비웁니다.
        self.mean.set("") # '뜻' 입력창의 내용을 비웁니다.

    def search(self): # 단어를 단어장에서 검색하는 메서드입니다.
        w = self.word.get() # '단어' 입력창에 입력된 텍스트를 가져와 'w' 변수에 저장합니다.
        if w not in self.words: # 가져온 단어 'w'가 'self.words' 딕셔너리에 없는지 확인합니다.
            messagebox.showinfo("검색 오류", f"{w} 단어는 없습니다!") # 단어가 없으면 오류 메시지를 팝업으로 보여줍니다.
            self.reset() # 입력창을 초기화합니다.
            return # 메서드를 종료합니다.
        m = self.words[w] # 딕셔너리에서 해당 단어 'w'의 뜻을 찾아 'm' 변수에 저장합니다.
        self.mean.set(m) # 찾은 뜻 'm'을 '뜻' 입력창에 표시합니다.

    def reset(self): # 입력창의 내용을 초기화(지우는)하는 메서드입니다.
        self.word.set("") # '단어' 입력창의 내용을 비웁니다.
        self.mean.set("") # '뜻' 입력창의 내용을 비웁니다.

    def end(self): # 애플리케이션을 종료하고 단어 데이터를 파일에 저장하는 메서드입니다.
        with open("words.txt", "w", encoding="utf-8") as fp: # 'words.txt' 파일을 쓰기 모드('w')로 열고, UTF-8 인코딩을 사용합니다.
                                                             # 기존 파일이 있으면 덮어씁니다.
            for w in self.words.keys(): # 'self.words' 딕셔너리의 모든 단어(key)를 반복합니다.
                m = self.words[w] # 각 단어 'w'에 해당하는 뜻 'm'을 딕셔너리에서 가져옵니다.
                fp.write(f"{w}:{m}\n") # 단어와 뜻을 "단어:뜻" 형식으로 파일에 쓰고, 각 줄의 끝에 줄 바꿈 문자('\n')를 추가합니다.
        self.win.destroy() # Tkinter 메인 윈도우를 파괴하여 애플리케이션을 완전히 종료합니다.

    # 이벤트 핸들러 메서드 (이벤트 바인딩을 통해 호출됨)
    def searchHandler(self, event): # '단어' 입력창에서 Enter 키 이벤트가 발생했을 때 호출되는 메서드입니다.
        self.search() # 실제 검색 로직을 수행하는 self.search() 메서드를 호출합니다. (event 매개변수는 무시해도 됨)

    def resetHandler(self, event): # '뜻' 입력창에서 Enter 키 이벤트가 발생했을 때 호출되는 메서드입니다.
        self.reset() # 입력창을 초기화하는 self.reset() 메서드를 호출합니다. (event 매개변수는 무시해도 됨)

# 프로그램 실행 부분
wm = WordMaster() # WordMaster 클래스의 객체(인스턴스)를 생성합니다.
                   # 이 순간, 위에서 정의된 __init__ 생성자 메서드가 자동으로 호출되어 단어장 GUI와 초기 데이터가 준비됩니다.
wm.win.mainloop() # Tkinter 이벤트 루프를 시작합니다.
                   # 이 줄이 실행되면 윈도우가 화면에 나타나고, 사용자의 입력(버튼 클릭, 키보드 입력 등)을 기다리며 이벤트에 반응하게 됩니다.
                   # 이 루프는 윈도우가 닫힐 때까지 계속 실행됩니다.
