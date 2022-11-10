from tkinter import *
from tkinter import ttk


window = Tk()
# 標題
window.title("Table Tk")

textSql = Text(height=3, width=100)
textSql.pack()
textSql.insert(END, "SELECT * FROM stockPrice")

button1 = Button(text="查詢")
button1.pack(pady=10)

tree = ttk.Treeview(column=("c1", "c2", "c3", "c4"), show='headings')
tree.column("#1", anchor=CENTER)
tree.heading("#1", text="日期")
tree.column("#2", anchor=CENTER)
tree.heading("#2", text="開盤")
tree.column("#3", anchor=CENTER)
tree.heading("#3", text="收盤價")
tree.column("#4", anchor=CENTER)
tree.heading("#4", text="成交筆數")
tree.pack()

# 保持顯示 window
window.mainloop()