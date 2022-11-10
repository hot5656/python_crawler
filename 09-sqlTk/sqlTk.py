from tkinter import *
from tkinter import ttk
import sqlite3


def View(sqltext,tree):
    global sqlite3
    # global sqltext

    for item in tree.get_children():
        tree.delete(item)
    con1 = sqlite3.connect("stockPrice.db1")
    cur1 = con1.cursor()
    cmd = sqltext.get(1.0, "end-1c")
    cur1.execute(cmd)
    rows = cur1.fetchall()
    for row in rows:
        # print(row) 
        tree.insert("", END, values=row)        
    con1.close()


window = Tk()
# 標題
window.title("sql Tk")

sqltext = Text(height=3, width=100)
sqltext.pack()
sqltext.insert(END, "SELECT * FROM stockPrice")


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

buttonQuery  = Button(text="查詢", command=View(sqltext,tree))
buttonQuery .pack(pady=10)

# 保持顯示 window
window.mainloop()