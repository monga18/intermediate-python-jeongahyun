import tkinter as tkt
from tkinter.filedialog import *

window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)

photo = tkt.PhotoImage(file="C:\\Users\\LGPC\\Desktop\\KakaoTalk_20240326_192953043.png")
window.iconphoto(False, photo)

text_area = tkt.Text(window)
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)

def new_file():
    text_area.delete(1.0, tkt.END)  # 텍스트 창 내용을 지움

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt",
                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text_content = text_area.get(1.0, tkt.END)  # 텍스트 창 내용 가져오기
            file.write(text_content)

menuMaker = tkt.Menu(window)

first_menu = tkt.Menu(menuMaker, tearoff=0)
first_menu.add_command(label='새 파일', command=new_file)
first_menu.add_command(label='저장', command=save_file)
first_menu.add_separator()
first_menu.add_command(label='종료', command=window.destroy)
menuMaker.add_cascade(label='파일', menu=first_menu)

def maker():
    tkt.messagebox.showinfo("만든 이", "이 프로그램은 OpenAI ChatGPT를 기반으로 만들어졌습니다.")

second_menu = tkt.Menu(menuMaker, tearoff=0)
second_menu.add_command(label='만든 이', command=maker)
menuMaker.add_cascade(label='정보', menu=second_menu)

window.config(menu=menuMaker)

window.mainloop()
