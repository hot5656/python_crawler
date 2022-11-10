from tkinter import *

window = Tk()
# 標題
window.title("Text Box Tk")

T = Text(height=2, width=30)
T.pack()
T.insert(END, "SELECT * FROM stockPrice")

# 保持顯示 window
window.mainloop()