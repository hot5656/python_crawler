import sqlite3

db = sqlite3.connect ('stockPrice.db1')
cursor = db.cursor()

while True:
  print('sql:', end='')
  cmd = input()
  if cmd == 'exit':
    break

  try:
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
      print(row)
  except: 
    print("The command isn't acceptable.")

db.close()
