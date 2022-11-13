from tkinter import *
from tkinter import ttk
import sqlite3
# from datetime import datetime
import datetime
import matplotlib.pyplot as plt

def twDateToGlobal(twDate):
    year, month, date = twDate.split("/")
    print(datetime.date(int(year), int(month), int(date)))
    return datetime.date(int(year), int(month), int(date))


def Chart():
    cmd = "SELECT * FROM stockPrice"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    x = [twDateToGlobal(row[0]) for row in rows] # 日期
    y = [row[2] for row in rows] # 股價
    plt.plot_date(x, y, 'g')
    plt.xticks(rotation=70)
    plt.show()


def View():
    for item in tree.get_children():
        tree.delete(item)
    # con1 = sqlite3.connect("stockPrice.db1")
    # cur1 = con1.cursor()

    # start : 1.0 表第一行第0個字元
    # end   : end 表到最後, -1c 表刪除1個字元
    # END = "end"
    cmd = sqltext.get(1.0, "end-1c")
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        # print(row) 
        tree.insert("", END, values=row)        
    # con1.close()


db = sqlite3.connect("stockPrice.db1")
cursor = db.cursor()

window = Tk()
# 標題
window.title("sql Tk")

sqltext = Text(height=3, width=100)
sqltext.pack()
sqltext.insert(END, "SELECT * FROM stockPrice")

buttonQuery  = Button(text="查詢", command=View)
buttonQuery.pack(pady=10)
buttonChar  = Button(text="股價圖", command=Chart)
buttonChar.pack(pady=10)

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

# close db
db.close()