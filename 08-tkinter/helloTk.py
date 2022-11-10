from tkinter import *

window = Tk()
# 標題
window.title("Hello Tk")

hello_label = Label(text="Hello, world!")
hello_label.pack()

# 保持顯示 window
window.mainloop()